import ConfigConstants
import tornado.websocket

import paho.mqtt.client as mqtt

from Configuration import Configuration
# from paho.mqtt.client import MQTTv311


class MQTTWebSocket(tornado.websocket.WebSocketHandler):
    web_socket_port = 9002
    mqttc = None

    def check_origin(self, origin):
        return True

    def open(self, *args, **kwargs):
        print "WebSocket# User is connected.\n"
        rc = self.mqttc.run()
        print "WebSocket# RC: " + str(rc)

    def on_message(self, message):
        print "WebSocket# Received message: %s" % message

        self._mqttc.publish(ConfigConstants.TOPIC_HOME_ROOM_AIR_CONDITIONER, "on")

        # while True:
        #     self.write_message("received")

    def on_close(self):
        print "WebSocket# Connection closed\n"
        self.mqttc = None


# application = tornado.web.Application([(r'/', WSHandlerServer), ])
#
# if __name__ == "__main__":
#     http_server = tornado.httpserver.HTTPServer(application)
#     http_server.listen(WSHandlerServer.web_socket_port)
#     tornado.ioloop.IOLoop.instance().start()

    def mqtt_on_connect(self, clientArg, obj, flags, rc):
        print "MQTTReader# Connected with result code " + str(rc)
        # clientArg.subscribe("home/room/temperature")

    def mqtt_on_message(self, clientArg, obj, msg):
        print("MQTTReader# Received message: " + msg.topic + " " + str(msg.payload))
        # self.web_socket.write_message(str(msg.payload))
        self.write_message(str(msg.payload))

    def mqtt_on_publish(self, clientArg, obj, mid):
        print "MQTTReader# Publish mid: " + str(mid)

    def mqtt_on_subscribe(self, clientArg, obj, mid, granted_qos):
        print "Subscribed: " + str(mid) + " " + str(granted_qos)

    def mqtt_on_log(self, clientArg, obj, level, string):
        print "LOG: MQTTReader#: " + string

    def mqtt_run(self):
        self._mqttc.connect(
            self.config.read_mqtt_publisher_ip_address(),
            self.config.read_server_port(),
            60
        )

        self._mqttc.subscribe("home/room/temperature", 0)

        # self._mqttc.loop_forever()

        # rc = 0
        # while rc == 0:
        #     rc = self._mqttc.loop()
        #
        # return rc

    # def __init__(self, clientid=None):
    _mqttc = mqtt.Client()
    _mqttc.on_message = mqtt_on_message
    _mqttc.on_connect = mqtt_on_connect
    _mqttc.on_publish = mqtt_on_publish
    _mqttc.on_subscribe = mqtt_on_subscribe
    _mqttc.on_log = mqtt_on_log

    config = Configuration(ConfigConstants.FILE_NAME)


# mqttc = MQTTReaderClass()
# rc = mqttc.run()
#
# print "MQTTReader# rc: " + str(rc)
