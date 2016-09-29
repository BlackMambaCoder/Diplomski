import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import time

class WSHandlerServer(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self, *args, **kwargs):
        print "user is connected.\n"

        file_read_temp = open("temp.txt", "rt")
        temperature = file_read_temp.read()
        file_read_temp.close()

        self.write_message(temperature)

    def on_message(self, message):
        print "Received message: %s" % message

        while True:
            file_read_temp = open("temp.txt", "rt")
            temperature = file_read_temp.read()
            file_read_temp.close()

            # if temperature > 30.0:
            time.sleep(5)
            self.write_message(temperature)
                # break

    def on_close(self):
        print "Connection closed\n"


application = tornado.web.Application([(r'/', WSHandlerServer),])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(9986)
    tornado.ioloop.IOLoop.instance().start()
