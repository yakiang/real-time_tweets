import json

import tornado.websocket

from Model.thread import TweetsThread


# A dict storing the user's socket and its corresponding thread object.
# Each user (or socket) can have only one thread object at the same time.
sockets = {}


class RealSocket(tornado.websocket.WebSocketHandler):
    ''' Manipulate threads according to sockets
    '''
    def open(self):
        print 'socket opened'

    def on_close(self):
        self.stop_thread()
        print 'socket closed'

    def on_message(self, data):
        ''' Receives new keyword to monitor here
        '''
        message = json.loads(data)
        hashtag = message.get('hashtag').strip().encode('utf-8')

        if hashtag:
            # If user if monitoring something else before, stop it
            if self in sockets:
                self.stop_thread()
            self.start_thread(hashtag)

    def start_thread(keyword):
        ''' Create, store and start a new thread.
        '''
        newThread = TweetsThread(keyword, self)
        newThread.daemon = True
        sockets[self] = newThread
        newThread.start()

    def stop_thread(self):
        ''' Stop the thread object
        '''
        sockets[self].stream.disconnect()
        del sockets[self]
