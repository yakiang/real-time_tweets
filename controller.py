import json
from uuid import uuid1

import tornado.web
import tornado.websocket

from model import GetTweets


sessions = {}


class HomePage(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html', session=uuid1())


class RealSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'socket opened'

    def on_close(self):
        print 'socket closed'

    def on_message(self, data):
        message = json.loads(data)
        hashtag, session = message.get('hashtag'), message.get('session')
        if hashtag:
            if session in sessions:
                prevStream = sessions[session]
                prevStream.stream.disconnect()
                del prevStream

            newStream = GetTweets(hashtag, self)
            newStream.daemon = True
            newStream.start()
