
from Configuration import Configuration
from paho.mqtt.client import MQTTv311

import paho.mqtt.publish as publish

import time
import os
import glob
import ConfigConstants


class DS18B20TempSensor:

    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    def __init__(self):
        self.base_dir = '/sys/bus/w1/devices/'
        self.device_folder = glob.glob(self.base_dir + '28*')[0]
        self.device_file = self.device_folder + '/w1_slave'

        self.config_file = ConfigConstants.FILE_NAME

        self.config = Configuration(self.config_file)

    def read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()

        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()

        equals_pos = lines[1].find('t=')

        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]

            temperature = float(temp_string) / 1000.0

            print "DS18B20# Temperature: " + str(temperature)

            if self.config.read_temp_measure() == "C":
                return str(temperature)

            if self.config.read_temp_measure() == "F":
                return str(temperature * 9.0 / 5.0 + 32.0)

        return 'Error'

if __name__ == "__main__":

    config_file_path = ConfigConstants.FILE_NAME
    config = Configuration(config_file_path)

    # client = mqtt.Client(protocol=MQTTv311)
    # ip_address = config.read_mqtt_publisher_ip_address()
    # port = config.read_server_port()
    #
    # client.connect(host=ip_address, port=port, 60)


    # config_file = ConfigConstants.FILE_NAME
    # config = Configuration(config_file)

    tempSensor = DS18B20TempSensor()
    while True:
        print "****************************************"
        # # Wait some time as long as it's described
        # # in the config file.
        # sleepPeriod = config.read_update_period_interval()
        # sleepMeasure = config.read_update_period_measure()
        #
        # print "MQTT# SleepPeriod: " + str(sleepPeriod)
        # print "MQTT# SleepMeasure: " + sleepMeasure
        #
        # if sleepMeasure == ConfigConstants.MEASURE_MILLI_SECONDS:
        #     sleepPeriod = float(sleepPeriod) / 1000.0
        #     print "MQTT# Sleep period: " + str(sleepPeriod) + sleepMeasure + "."
        #     time.sleep(sleepPeriod)
        #
        # elif sleepMeasure == ConfigConstants.MEASURE_SECONDS:
        #     print "MQTT# Sleep period: " + str(sleepPeriod) + sleepMeasure + "."
        #     time.sleep(sleepPeriod)
        #
        # # If there is an error about the time period measure,
        # # wait at least 10 seconds, but do not interrupt the
        # # system.
        # else:
        #     print "MQTT# Sleep period ERROR. Sleep for 2s."
        #     time.sleep(2)

        print "MQTT-Temperature# Wait 0.5s"
        time.sleep(0.5)

        temp = tempSensor.read_temp()
        print "MQTT# Temperature: " + str(temp)

        # If an error occurs, send error message, but
        # do not interrupt the whole process
        if temp == 'Error':
            print "Sending Error"
            publish.single(
                "home/room/temperature",
                temp,
                hostname=config.read_mqtt_subscriber_ip_address(),
                port=config.read_server_port(),
                protocol=MQTTv311
            )
            continue

        temp = float(temp)

        # Publish temperature if it's higher than given level.
        if temp > tempSensor.config.read_temp_level():
            print "Sending temperature: " + str(temp)
            publish.single(
                "home/room/temperature",
                temp,
                hostname=config.read_mqtt_subscriber_ip_address(),
                port=config.read_server_port(),
                protocol=MQTTv311
            )
            continue
