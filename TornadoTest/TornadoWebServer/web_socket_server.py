import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import time
import json


class WSHandlerServer(tornado.websocket.WebSocketHandler):

    def data_received(self, chunk):
        pass

    web_socket_port = 9900
    # mqttc = None

    DEBUG_TAG = "WebSocket# "

    def check_origin(self, origin):
        return True

    def open(self, *args, **kwargs):
        print self.DEBUG_TAG + "User is connected.\n"

    def on_message(self, message):
        print self.DEBUG_TAG + "Received message: %s" % message

        while True:
            if self.read_temp_from_txt_file():
                print self.DEBUG_TAG + "Temperature is sent."
                print self.DEBUG_TAG + "Waiting for client response ..."
                break
            time.sleep(0.5)

    # Reads temperature from file
    def read_temp_from_txt_file(self):
        temp_file = open("temp.txt", "r")
        line = temp_file.readline()
        temp_file.close()

        print self.DEBUG_TAG + "Read temperature line"

        json_object = json.loads(line)

        if bool(json_object["unread"]):
            print self.DEBUG_TAG + "Unread is true"
            json_object["unread"] = int(False)

            self.update_temp_in_file(json_object)

            print self.DEBUG_TAG \
                  + "Temperature " \
                  + str(json_object["value"]) \
                  + " is sent"

            self.write_message(json_object)

            return True

        print self.DEBUG_TAG + "Unread is false"
        return False

    def update_temp_in_file(self, json_object):
        print self.DEBUG_TAG + "Updating temp file"

        json_string = json.dumps(json_object)

        temp_file = open("temp.txt", "w")
        temp_file.write(json_string)
        temp_file.close()

    def on_close(self):
        print "WebSocket# Connection closed\n"
        # self.mqttc = None


application = tornado.web.Application([(r'/', WSHandlerServer),])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(WSHandlerServer.web_socket_port)
    tornado.ioloop.IOLoop.instance().start()
