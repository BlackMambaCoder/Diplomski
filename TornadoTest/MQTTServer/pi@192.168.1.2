
from DS18B20TempSensor import DS18B20TempSensor
from Configuration import Configuration
from paho.mqtt.client import MQTTv31

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

import time
import os
import glob
import ConfigConstants


def publish_single(topic, value):
    config_broker = Configuration(ConfigConstants.FILE_NAME)

    publish.single(
        topic,
        value,
        hostname="192.168.1.5",
        port=1883,
        protocol=MQTTv31
    )

if __name__ == "__main__":

    config_file_path = ConfigConstants.FILE_NAME
    config = Configuration(config_file_path)

    client = mqtt.Client(protocol=MQTTv31)
    ip_address = config.read_broker_server_ip_address()
    port = config.read_broker_port()

    client.connect(host="192.168.1.5", port=1883, keepalive=60)

    tempSensor = DS18B20TempSensor()
    while True:
        print "****************************************"
        # Wait some time as long as it's described
        # in the config file.
        sleepPeriod = config.read_update_period_interval()
        sleepMeasure = config.read_update_period_measure()

        print "MQTT# SleepPeriod: " + str(sleepPeriod)
        print "MQTT# SleepMeasure: " + sleepMeasure

        if sleepMeasure == ConfigConstants.MEASURE_MILLI_SECONDS:
            sleepPeriod = float(sleepPeriod) / 1000.0
            print "MQTT# Sleep period: " + str(sleepPeriod) + sleepMeasure + "."

        elif sleepMeasure == ConfigConstants.MEASURE_SECONDS:
            print "MQTT# Sleep period: " + str(sleepPeriod) + sleepMeasure + "."

        # If there is an error about the time period measure,
        # wait at least 10 seconds, but do not interrupt the
        # system.
        else:
            print "MQTT# Sleep period ERROR. Sleep for 2s."
            sleepPeriod = 2.0

        # print "MQTT-Temperature# Wait 0.5s"
        # time.sleep(0.5)

        time.sleep(sleepPeriod)

        temp = tempSensor.read_temp()
        print "MQTT# Temperature: " + str(temp)

        # If an error occurs, send error message, but
        # do not interrupt the whole process
        if temp == 'Error':
            print "Sending Error"
            publish_single(
                "home/room/temperature",
                temp
            )
            # publish.single(
            #     "home/room/temperature",
            #     temp,
            #     hostname=config.read_mqtt_subscriber_ip_address(),
            #     port=config.read_server_port(),
            #     protocol=MQTTv311
            # )
            continue

        temp = float(temp) / 1000.0

        if config.read_temp_measure() == "F":
            temp = temp * 9.0 / 5.0 + 32.0

        # Publish temperature if it's higher than given level.
        if temp > config.read_temp_level():
            print "Sending temperature: " + str(temp)
            publish_single(
                "home/room/temperature",
                temp
            )
            # publish.single(
            #     "home/room/temperature",
            #     temp,
            #     hostname=config.read_mqtt_subscriber_ip_address(),
            #     port=config.read_server_port(),
            #     protocol=MQTTv311
            # )
