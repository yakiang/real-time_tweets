import json

import tornado.websocket

from Model.thread import TweetsThread


# A dict storing the user's socket and its corresponding thread object.
# Each user (or socket) can have only one thread object at the same time.


class RealSocket(tornado.websocket.WebSocketHandler):
    ''' Manipulate threads according to sockets
    '''
    def __init__(self):
        self.globalSessions = self.application.sessions

    def open(self):
        print 'socket opened'

    def on_close(self):
        self.stop_thread()
        print 'socket closed'

    def on_message(self, data):
        ''' Receives new keyword to monitor here
        '''
        message = json.loads(data)
        hashtag = message.get('hashtag')

        if hashtag:
            # If user is monitoring something else before, stop it
            if self in self.globalSessions:
                self.stop_thread()

            self.start_thread(hashtag.strip().encode('utf-8'))

    def start_thread(self, keyword):
        ''' Create, store and start a new thread.
        '''
        newThread = TweetsThread(keyword, self)
        newThread.daemon = True
        self.globalSessions.append(newThread)
        newThread.start()

    def stop_thread(self):
        ''' Stop the thread object
        '''
        threadIndex = self.globalSessions.index(self) + 1
        thread.stream.disconnect()
        del self.globalSessions[threadIndex-1]
        del self.globalSessions[threadIndex]
