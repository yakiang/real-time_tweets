import json

import tornado.websocket

from Model.thread import GetTweets


sessions = {}
    

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
