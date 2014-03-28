import json

import tornado.websocket

from Model.thread import GetTweets


SOCKET_STREAM_DICT = {}
    

class RealSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'socket opened'

    def on_close(self):
        self.disconnect_stream()
        print 'socket closed'

    def on_message(self, data):
        message = json.loads(data)
        hashtag= message.get('hashtag')

        if hashtag:
            if self in SOCKET_STREAM_DICT:
                self.disconnect_stream();

            newStream = GetTweets(hashtag, self)
            newStream.daemon = True
            SOCKET_STREAM_DICT[self] = newStream
            newStream.start()

    def disconnect_stream(self):
        SOCKET_STREAM_DICT[self].stream.disconnect()
        del SOCKET_STREAM_DICT[self]
