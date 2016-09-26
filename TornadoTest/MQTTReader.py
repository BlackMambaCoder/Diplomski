import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
    print "Connected with result code " + str(rc)
    client.subscribe("home/room/temperature")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.0.106", 1883, 60)

while True:
    client.loop()
    time.sleep(0.1)
