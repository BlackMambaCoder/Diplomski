import ConfigConstants

import paho.mqtt.client as mqtt

from Configuration import Configuration
from MongoAPI import MongoAPI
# from paho.mqtt.client import MQTTv311


class MQTTReaderClass:
    DEBUG_TAG = "MQTTReader# "

    def __init__(self):
        self._mqttc = mqtt.Client()
        self._mqttc.on_message = self.on_message
        self._mqttc.on_connect = self.on_connect
        self._mqttc.on_publish = self.on_publish
        self._mqttc.on_subscribe = self.on_subscribe
        self._mqttc.on_log = self.on_log

        self.config = Configuration(ConfigConstants.FILE_NAME)

    def on_connect(self, clientArg, obj, flags, rc):
        print self.DEBUG_TAG + "Connected with result code " + str(rc)
        # clientArg.subscribe("home/room/temperature")

    def on_message(self, clientArg, obj, msg):
        print(self.DEBUG_TAG + "Received message: " + msg.topic + " " + str(msg.payload))
        self.store_temp_to_db(msg.payload)

    def on_publish(self, clientArg, obj, mid):
        print self.DEBUG_TAG + "Publish mid: " + str(mid)

    def on_subscribe(self, clientArg, obj, mid, granted_qos):
        print self.DEBUG_TAG + "Subscribed: " + str(mid) + " " + str(granted_qos)

    def on_log(self, clientArg, obj, level, string):
        print self.DEBUG_TAG + "LOG: " + string

    def run(self):
        self._mqttc.connect(
            "192.168.0.108",
            1883,
            60
        )

        self._mqttc.subscribe("home/room/temperature", 0)

        self._mqttc.loop_forever()

    def store_temp_to_db(self, temperature):
        print self.DEBUG_TAG + "Store temperature to mongo db"
        db_api = MongoAPI()
        return db_api.store_temp(temperature)

