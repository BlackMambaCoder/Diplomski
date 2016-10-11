import tornado.ioloop
import tornado.web
import time
import json
import ConfigConstants
import os

from DS18B20TempSensor import DS18B20TempSensor
from Configuration import Configuration


class FileUpdateController(tornado.web.RequestHandler):

    DEBUG_TAG = "TornadoServer# "
    config = Configuration(ConfigConstants.FILE_NAME)

    def data_received(self, chunk):
        pass

    def get(self):

        print self.DEBUG_TAG + "Get request"

        period = float(self.config.read_update_period_interval())
        threshold = float(self.config.read_temp_level())

        print self.DEBUG_TAG + "Values read"

        json_object = {"threshold": threshold, "period": period}

        json_string = json.dumps(json_object)

        print self.DEBUG_TAG + "Generated json object string"
        print self.DEBUG_TAG + str(json_string)

        self.write(json_string)

        print self.DEBUG_TAG + "Json Object send"

    def post(self):
        body = self.request.body
        print self.DEBUG_TAG + "Body: " + str(body)

        body_values = body.split("&")
        threshold = str(body_values[0]).split("=")[1]
        period = str(body_values[1]).split("=")[1]
        print self.DEBUG_TAG + "Threshold: " + threshold
        print self.DEBUG_TAG + "Period: " + period

        self.config.write_temp_level(str(threshold))
        self.config.write_period_interval(str(period))
        print self.DEBUG_TAG + "Written to file"


class CurrentData(tornado.web.RequestHandler):
    DEBUG_TAG = "CurrentData# "

    def data_received(self, chunk):
        pass

    def get(self):
        sensor = DS18B20TempSensor()

        print self.DEBUG_TAG + "Read temperature"
        temperature = sensor.read_temp()

        temperature = float(temperature)/1000.0

        config = Configuration(ConfigConstants.FILE_NAME)
        temp_measure = str(config.read_temp_measure())

        if temp_measure == "F":
            temperature = temperature * 9.0 / 5.0 + 32.0

        print self.DEBUG_TAG + "Set temperature to json object"
        temp_json = {"temperature": temperature}

        print self.DEBUG_TAG + "Convert temp json object to string"
        temp_json_str = json.dumps(temp_json)

        self.write(temp_json_str)
        print self.DEBUG_TAG + "Temperature written back"


application = tornado.web.Application([
    (r"/update_config/", FileUpdateController),
    (r"/get_data/", CurrentData)

])

if __name__ == "__main__":
    application.listen(7720)
    tornado.ioloop.IOLoop.instance().start()
