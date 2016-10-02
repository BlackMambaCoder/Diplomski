import tornado.ioloop
import tornado.web
from TemperatureMessageORM import TemperatureMessage


class HomeRoomTemperature(tornado.web.RequestHandler):

    DEBUG_TAG = "TornadoServer# "

    def data_received(self, chunk):
        pass

    def get(self, temperature):
        print "HomeRoomTemperature: " + str(temperature)

        # db = MySQLdb.connect(host="localhost", db="home", user="root", passwd="root")

        # TemperatureMessage.create_table()

        for temp in TemperatureMessage.filter(topic="home/room/temperature"):
            print self.DEBUG_TAG + "Entry exists in DB"
            print self.DEBUG_TAG + str(temp)

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
    application.listen(8851)
    tornado.ioloop.IOLoop.instance().start()
