import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

class WSHandler(tornado.websocket.WebSocketHandler):

	def check_origin(self, origin):
		return True

	def open(self):
		print 'user is connected.\n'

	def on_message(self, message):
		print 'received message: %s' %message

		string_array = message.split("::")
		time = string_array[0]

		try:
			temperature = string_array[1]
		except:
			temperature = "0"


		file_out = open("temp.txt", "w")

		file_out.seek(0)
		file_out.truncate()

		file_out.write(temperature)
		file_out.close()

		self.write_message(message + ' OK')

	def on_close(self):
		print 'connection closed\n'

application = tornado.web.Application([(r'/server', WSHandler),])

if __name__ == "__main__":
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8860)
	tornado.ioloop.IOLoop.instance().start()