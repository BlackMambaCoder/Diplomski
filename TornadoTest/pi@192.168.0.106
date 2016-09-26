import requests
import DS18B20TempSensor

tempSensor = DS18B20TempSensor.DS18B20TempSensor()

while True:
    temperature = tempSensor.read_temp()

    url = "http://192.168.0.108:8700/write_temp/" + str(temperature)
    resp = requests.get(url)
