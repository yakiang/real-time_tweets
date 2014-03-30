import json

import tornado.websocket

from Model.thread import TweetsThread
from Model.session import session


class RealSocket(tornado.websocket.WebSocketHandler):
    ''' Manipulate sockets and its thread
    '''
    def open(self):
        session.set_thread(self)
        print 'socket opened'

    def on_close(self):
        self.stop_thread()
        session.remove_socket(self)
        print 'socket closed'

    def on_message(self, data):
        ''' Receives new keyword to monitor here
        '''
        message = json.loads(data)
        hashtag = message.get('hashtag')

        if hashtag:
            self.stop_thread()
            self.start_thread(hashtag.strip().encode('utf-8'))

    def start_thread(self, keyword):
        ''' Create, store and start a new thread.
        '''
        newThread = TweetsThread(keyword)
        session.set_thread(self, newThread)
        newThread.start()

    def stop_thread(self):
        ''' Stop the thread object
        '''
        thread = session.sockets_threads_dict[self]
        if thread:
            thread.stream.disconnect()
            session.set_thread(self)
