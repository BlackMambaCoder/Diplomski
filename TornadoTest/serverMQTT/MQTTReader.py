import time
import ConfigConstants

import paho.mqtt.client as mqtt

from Configuration import Configuration


def on_connect(client, userdata, rc):
    print "Connected with result code " + str(rc)
    client.subscribe("#")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

config_file_path = ConfigConstants.FILE_NAME
config = Configuration(config_file_path)
ip_address = config.read_mqtt_publisher_ip_address()
port = config.read_server_port()

client.connect(ip_address, port, 60)

print "Connected on: " + str(ip_address) + ":" + str(port)

client.loop_forever()

# while True:
#     client.loop()
#     time.sleep(0.1)
