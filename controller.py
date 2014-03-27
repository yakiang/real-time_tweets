import tornado.web
import tornado.websocket

from model import GetTweets


class Home(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html')

    def post(self):
        pass


class RealSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        pass

    def on_close(self):
        pass

    def on_message(self):
        pass
