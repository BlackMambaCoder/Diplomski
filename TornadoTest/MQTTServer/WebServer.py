import tornado.ioloop
import tornado.web
import time
import json
import ConfigConstants
import os
import requests

from Configuration import Configuration
from MongoAPI import MongoAPI

# from TemperatureMessageORM import TemperatureMessage


class HomeRoomTemperature(tornado.web.RequestHandler):

    DEBUG_TAG = "TornadoServer# "

    def data_received(self, chunk):
        pass

    def get(self, temperature):
        print self.DEBUG_TAG + "HomeRoomTemperature: " + str(temperature)

        # db = MySQLdb.connect(host="localhost", db="home", user="root", passwd="root")

        # TemperatureMessage.create_table()
        # self.writeTempToDB(temperature)
        # topic = "home/room/temperature"
        # self.write_temp_to_txt_file(temperature, topic)
        self.store_temp_to_db(temperature)

    def write_temp_to_txt_file(self, temperature, topic):
        print self.DEBUG_TAG + "Temperature writing to file"

        json_object = {
            "time": int(time.time()),
            "topic": topic,
            "value": float(temperature),
            "unread": 1
        }

        json_string = json.dumps(json_object)

        temp_file = open("temp.txt", "w")

        temp_file.write(json_string)

        temp_file.close()

        print self.DEBUG_TAG + "Temperature written to file"

    def store_temp_to_db(self, temperature):
        print self.DEBUG_TAG + "Store temperature to mongo db"
        db_api = MongoAPI()
        return db_api.store_temp(temperature)

    # def write_temp_to_db(self, temperature):
    #     for temp in TemperatureMessage.filter(topic="home/room/temperature"):
    #         print self.DEBUG_TAG + "Entry exists in DB"
    #         print self.DEBUG_TAG + str(temp.temperature)
    #
    #         temp.temperature = temperature
    #         temp.unread = False
    #         temp.save()
    #
    #         break
    #     else:
    #         print self.DEBUG_TAG + "Entry doesn't exist in DB"
    #
    #         temp = TemperatureMessage(
    #             topic="home/room/temperature",
    #             temperature=temperature
    #         )
    #     temp.save()


class RaspBerryGetConfig(tornado.web.RequestHandler):
    DEBUG_TAG = "RaspGetCfg# "

    def data_received(self, chunk):
        pass

    def post(self, *args, **kwargs):
        print self.DEBUG_TAG + "RaspberryGetConfig"

        response = requests.get("http://192.168.0.103:7720/update_config/")

        status_code = response.status_code

        if status_code == 200:
            response_content = response.content
            print self.DEBUG_TAG +\
                  "Response Content: " + \
                  str(response_content)

            self.write(response_content)

            print self.DEBUG_TAG + "Response sent back"

        if status_code != 200:
            response_reason = response.reason
            print self.DEBUG_TAG + "Error: " + str(status_code)
            print self.DEBUG_TAG + "Reason: " + str(response_reason)


class RaspBerrySetConfig(tornado.web.RequestHandler):
    DEBUG_TAG = "RaspSetCfg# "

    def data_received(self, chunk):
        pass

    def post(self, *args, **kwargs):
        print "RaspberrySetConfig"

        post_value_json = json.loads(self.request.body)

        threshold = post_value_json["threshold"]
        period = post_value_json["period"]

        print self.DEBUG_TAG + "Threshold: " + str(threshold)
        print self.DEBUG_TAG + "Period: " + str(period)

        response = requests.post(
            "http://192.168.0.103:7720/update_config/",
            data={"period": period, "threshold": threshold}
        )

        status_code = response.status_code

        if status_code == 200:
            print self.DEBUG_TAG + "Code: " + str(200)
            self.write("SET")

        if status_code != 200:
            print self.DEBUG_TAG + "Code: " + str(status_code)
            self.write("Error: " + str(status_code))


class RaspBerryGetCurrentData(tornado.web.RequestHandler):
    DEBUG_TAG = "RaspGetCurrData# "

    def data_received(self, chunk):
        pass

    def post(self, *args, **kwargs):
        print self.DEBUG_TAG + "Post request"

        response = requests.get("http://192.168.0.103:7720/get_data/")

        status_code = response.status_code

        if status_code == 200:
            response_content = response.content
            print self.DEBUG_TAG +\
                  "Response Content: " + \
                  str(response_content)

            self.write(response_content)

            print self.DEBUG_TAG + "Response sent back"

        if status_code != 200:
            response_reason = response.reason
            print self.DEBUG_TAG + "Error: " + str(status_code)
            print self.DEBUG_TAG + "Reason: " + str(response_reason)



application = tornado.web.Application([
    (r"/home_room_temperature/([^/]+)", HomeRoomTemperature),
    (r"/rasp_get_config", RaspBerryGetConfig),
    (r"/rasp_config", RaspBerrySetConfig),
    (r"/room_temp", RaspBerryGetCurrentData)
])

if __name__ == "__main__":
    application.listen(8820)
    tornado.ioloop.IOLoop.instance().start()
