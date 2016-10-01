import time
import ConfigConstants

import paho.mqtt.client as mqtt

from Configuration import Configuration
from paho.mqtt.client import MQTTv311


def on_connect(clientArg, userdata, rc):
    print "Connected with result code " + str(rc)
    clientArg.subscribe("#")


def on_message(clientArg, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def on_publish(clientArg, obj, mid):
    print "Publish mid: " + str(mid)


def on_subscribe(clientArg, obj, mid, granted_qos):
    print "Subscribed: " + str(mid) + " " + str(granted_qos)


def on_log(clientArg, obj, level, string):
    print "LOG: MQTTReader#: " + string


client = mqtt.Client(protocol=MQTTv311)
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_log = on_log

config_file_path = ConfigConstants.FILE_NAME
config = Configuration(config_file_path)
ip_address = config.read_mqtt_publisher_ip_address()
port = config.read_server_port()

client.connect(ip_address, port, 60)
# client.connect_srv(ip_address)
# client.subscribe("#")

print "Connected on: " + str(ip_address) + ":" + str(port)

client.loop_forever()

# while True:
#     client.loop()
#     time.sleep(0.1)
