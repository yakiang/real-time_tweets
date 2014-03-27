import json
from uuid import uuid1

import tornado.web
import tornado.websocket
import redis

from model import GetTweets


class HomePage(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html', session=uuid1())


class RealSocket(tornado.websocket.WebSocketHandler):
    def initialize(self):
        self.db = redis.StrictRedis(host='localhost', port=6379, db=0)

    def open(self):
        print 'socket opened'

    def on_close(self):
        print 'socket closed'

    def on_message(self, data):
        message = json.loads(data)
        hashtag, session = message.get('hashtag'), message.get('session')
        if hashtag:
            if self.db.hget(session, 'socket'):
                prevStream = self.db.hget(session, 'stream')
                prevStream.stream.disconnect()
                del prevStream

            self.db.hset(session, 'socket', self)
            newStream = GetTweets(hashtag, session)
            newStream.daemon = True
            self.db.hset(session, 'stream', newStream)

            print self.db.hget(session, 'socket')
            newStream.start()
