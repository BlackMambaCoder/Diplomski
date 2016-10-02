from bottle import route, run

import ConfigConstants
import Configuration
import TemperatureMessageORM


@route('/read_temp')
def read_temp():
    temperature = 0.0
    # file_read_temp = open("temp.txt", "rt")
    # temperature = file_read_temp.read()
    # file_read_temp.close()

    return temperature


@route('/write_temp/<temperature>')
def write_temp(temperature):

    # file_write_temp = open("temp.txt", "w")
    #
    # file_write_temp.seek(0)
    # file_write_temp.truncate()
    # file_write_temp.write(temperature)
    #
    # file_write_temp.close()

    print "Temperature: " + str(temperature)

    return "temp written"

# file_path = ConfigConstants.FILE_NAME
#
# config = Configuration.Configuration(file_path)
# port = config.read_bottle_server_port()
# ip_address = config.read_bottle_server_ip_address()

run(host="192.168.0.108", port=8810)
