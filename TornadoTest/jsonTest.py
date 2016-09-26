import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import json
import Constants

class WSHandler(tornado.websocket.WebSocketHandler):
	ledOn = False

	def check_origin(self, origin):
		return True

    def open(self):
        print 'user is connected.\n'
        self.ledOn = False

    def on_message(self, message):
        # Received message: check if it's from pi
        message_data = json.loads(message)
        if message_data[Constants.SOURCE_ATTR] == Constants.TYPE_PI:
            # send to client

        print 'received message: %s' %message
        self.write_message(message + ' OK')

	def on_close(self):
		print 'connection closed\n'

application = tornado.web.Application([(r'/server', WSHandler),])

if __name__ == "__main__":
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8860)
	tornado.ioloop.IOLoop.instance().start()