import time
import Config.ConfigConstants
import paho.mqtt.client as mqtt

from Config.Configuration import Configuration


config_file_name = Config.ConfigConstants.FILE_NAME
config = Configuration(config_file_name)

ipAddress = config.read_server_ip_address()
port = config.read_server_port()


def on_connect(client_arg, userdata, rc):
    print "Connected with result code " + str(rc)
    client_arg.subscribe("home/room/temperature")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(ipAddress, port, 60)


while True:
    client.loop()
    # time.sleep(0.1)
