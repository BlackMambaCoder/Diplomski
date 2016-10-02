import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import time
import MQTTReaderClass

class WSHandlerServer(tornado.websocket.WebSocketHandler):
    web_socket_port = 9002
    mqttc = None

    def check_origin(self, origin):
        return True

    def open(self, *args, **kwargs):
        print "WebSocket# User is connected.\n"

        self.mqttc = MQTTReaderClass.MQTTReaderClass(self)
        rc = self.mqttc.run()
        print "WebSocket# RC: " + str(rc)

    def on_message(self, message):
        print "WebSocket# Received message: %s" % message

        # while True:
        #     self.write_message("received")

    def on_close(self):
        print "WebSocket# Connection closed\n"
        self.mqttc = None


application = tornado.web.Application([(r'/', WSHandlerServer),])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(WSHandlerServer.web_socket_port)
    tornado.ioloop.IOLoop.instance().start()
