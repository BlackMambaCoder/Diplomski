import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import time
import MQTTReaderClass

from bottle import route, run

from Configuration import Configuration

import ConfigConstants


class WSHandlerServer(tornado.websocket.WebSocketHandler):
    web_socket_port = 9002
    mqttc = None

    def check_origin(self, origin):
        return True

    def open(self, *args, **kwargs):
        print "WebSocket# User is connected.\n"

    def on_message(self, message):
        print "WebSocket# Received message: %s" % message

        # while True:
        #     self.write_message("received")

    def on_close(self):
        print "WebSocket# Connection closed\n"
        self.mqttc = None

    @route('/read_temp')
    def read_temp(self):
        file_read_temp = open("temp.txt", "rt")
        temperature = file_read_temp.read()
        file_read_temp.close()

        return temperature

    @route('/write_temp/<temperature>')
    def write_temp(self, temperature):
        # file_write_temp = open("temp.txt", "w")
        #
        # file_write_temp.seek(0)
        # file_write_temp.truncate()
        # file_write_temp.write(temperature)
        #
        # file_write_temp.close()

        self.write_message(str(temperature))

        print "Temperature: " + str(temperature)

        return "temp written"

config_file_path = ConfigConstants.FILE_NAME
config = Configuration(config_file_path)

host_ip_address = config.read_bottle_server_ip_address()
host_port = config.read_bottle_server_port()

application = tornado.web.Application([(r'/', WSHandlerServer),])
run(host=host_ip_address, port=8802)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(WSHandlerServer.web_socket_port)
    tornado.ioloop.IOLoop.instance().start()
