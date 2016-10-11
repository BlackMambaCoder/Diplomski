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

DEBUG_TAG = "piHttp# "

while True:
    print DEBUG_TAG + "Read temperature"
    temperature = tempSensor.read_temp()
    temperature = float(temperature) / 1000.0
    print DEBUG_TAG + "Temperature: " + str(temperature)

    print DEBUG_TAG + "Read temperature measure from config file"
    temp_measure = str(config.read_temp_measure())

    if temp_measure == "F":
        print DEBUG_TAG + "Temperature measure is Fahrenheit"
        temperature = temperature * 9.0 / 5.0 + 32.0

    print DEBUG_TAG + "Read temperature threshold"
    temp_threshold = float(config.read_temp_level())

    print DEBUG_TAG + "Temperature threshold: " + str(temp_threshold)

    if temperature > temp_threshold:
        print DEBUG_TAG + "Sending temperature: " + str(temperature)

        url = "http://192.168.0.108:8820/home_room_temperature/" + str(temperature)
        resp = requests.get(url)

        if resp.status_code == 200:
            print DEBUG_TAG + "Temperature is sent successfully"

        if resp.status_code != 200:
            print DEBUG_TAG + "Temperature sending failed"
            print DEBUG_TAG + "Response reason: " + resp.reason

    period_measure = str(config.read_update_period_measure())
    period_interval = float(config.read_update_period_interval())

    if period_measure == "ms":
        period_interval /= 1000.0

    elif period_measure == "s":
        pass

    else:
        period_interval = 1.0

    print DEBUG_TAG + "Wait for " + str(period_interval) + "s"

    time.sleep(period_interval)
