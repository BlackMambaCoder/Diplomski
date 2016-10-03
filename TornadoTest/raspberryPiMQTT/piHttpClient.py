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

config = Configuration(ConfigConstants.FILE_NAME)

while True:
    temperature = tempSensor.read_temp()
    temperature = float(temperature) / 1000.0
    temp_measure = str(config.read_temp_measure())

    if temp_measure == "F":
        temperature = temperature * 9.0 / 5.0 + 32.0

    temp_threshold = float(config.read_temp_level())


    if temperature > temp_threshold:
        print "piHttp# Sending temperature: " + str(temperature)

        url = "http://192.168.0.108:8810/home_room_temperature/" + str(temperature)
        resp = requests.get(url)

    period_measure = str(config.read_update_period_measure())
    period_interval = float(config.read_update_period_interval())

    if period_measure == "ms":
        period_interval /= 1000.0

    elif period_measure == "s":
        pass

    else:
        period_interval = 1.0

    time.sleep(period_interval)
