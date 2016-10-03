import requests
import DS18B20TempSensor
import time
import ConfigConstants

from Configuration import Configuration

tempSensor = DS18B20TempSensor.DS18B20TempSensor()

# file_path = ConfigConstants.FILE_NAME
# config = Configuration(file_path)
#
# ip_address = config.read_bottle_server_ip_address()
# port = config.read_bottle_server_port()

while True:
    temperature = tempSensor.read_temp()

    print "piHttp# Sending temperature: " + str(temperature)

    url = "http://192.168.0.108:8800/home_room_temperature/" + str(temperature)
    resp = requests.get(url)
    time.sleep(0.5)
