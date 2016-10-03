import tornado.ioloop
import tornado.web
import time
import json

from TemperatureMessageORM import TemperatureMessage


class HomeRoomTemperature(tornado.web.RequestHandler):

    DEBUG_TAG = "TornadoServer# "

    def data_received(self, chunk):
        pass

    def get(self, temperature):
        print self.DEBUG_TAG + "HomeRoomTemperature: " + str(temperature)

        # db = MySQLdb.connect(host="localhost", db="home", user="root", passwd="root")

        # TemperatureMessage.create_table()
        # self.writeTempToDB(temperature)
        topic = "home/room/temperature"
        self.write_temp_to_txt_file(temperature, topic)

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

        # temp_file.write(str(int(time.time())))
        # temp_file.write(":")
        # temp_file.write(topic)
        # temp_file.write(":")
        # temp_file.write(str(temperature))
        # temp_file.write(":")
        # temp_file.write(str(True))
        # temp_file.write(":")

        # temp_file.write("\n")

        temp_file.close()

        print self.DEBUG_TAG + "Temperature written to file"

    def write_temp_to_db(self, temperature):
        for temp in TemperatureMessage.filter(topic="home/room/temperature"):
            print self.DEBUG_TAG + "Entry exists in DB"
            print self.DEBUG_TAG + str(temp.temperature)

            temp.temperature = temperature
            temp.unread = False
            temp.save()

            break
        else:
            print self.DEBUG_TAG + "Entry doesn't exist in DB"

            temp = TemperatureMessage(
                topic="home/room/temperature",
                temperature=temperature
            )
        temp.save()


class RaspBerryGetConfig(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def post(self, *args, **kwargs):
        print "RaspberryGetConfig"
        self.write("RaspConfig")
        # self.get_argument("jsonObject")


class RaspBerrySetConfig(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def post(self, *args, **kwargs):
        print "RaspberrySetConfig"

        post_value_json = json.loads(self.request.body)

        threshold = post_value_json["threshold"]
        period = post_value_json["period"]

        print "Post value: " + str(post_value_json["threshold"])
        self.write("RaspConfigIsSet")

application = tornado.web.Application([
    (r"/home_room_temperature/([^/]+)", HomeRoomTemperature),
    (r"/rasp_get_config", RaspBerryGetConfig),
    (r"/rasp_config", RaspBerrySetConfig)
])

if __name__ == "__main__":
    application.listen(8820)
    tornado.ioloop.IOLoop.instance().start()
