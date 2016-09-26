import paho.mqtt.publish as publish
from paho.mqtt.client import MQTTv311
import time
import os
import glob
import time

class DS18B20TempSensor():

    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

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
            temp_c = float(temp_string) / 1000.0
            #temp_f = temp_c * 9.0 / 5.0 + 32.0

            return str(temp_c)#, temp_f

        return 'Error'

if __name__ == "__main__":
    tempSensor = DS18B20TempSensor()
    while True:
        temp = tempSensor.read_temp()
        print "Sending temperature: " + temp
        publish.single("home/room/temperature", temp, hostname="192.168.0.106", port=1883, protocol=MQTTv311)
        time.sleep(1)
