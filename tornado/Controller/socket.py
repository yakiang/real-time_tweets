import json

import tornado.websocket

from Model.thread import GetTweets


sockets = {}
    

class RealSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'socket opened'

    def on_close(self):
        self.disconnect_stream()
        print 'socket closed'

    def on_message(self, data):
        message = json.loads(data)
        hashtag= message.get('hashtag').encode('utf-8')

        if hashtag:
            if self in sockets:
                self.disconnect_stream();

            newStream = GetTweets(hashtag, self)
            newStream.daemon = True
            sockets[self] = newStream
            newStream.start()

    def disconnect_stream(self):
        sockets[self].stream.disconnect()
        del sockets[self]
