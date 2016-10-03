import tornado.ioloop
import tornado.web
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
        self.write_temp_to_txt_file(temperature)

    def write_temp_to_txt_file(self, temperature):
        print self.DEBUG_TAG + "Temperature writing to file"

        temp_file = open("temp.txt", "w")
        temp_file.write(str(temperature))
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


application = tornado.web.Application([
    (r"/home_room_temperature/([^/]+)", HomeRoomTemperature)
])

if __name__ == "__main__":
    application.listen(8800)
    tornado.ioloop.IOLoop.instance().start()
