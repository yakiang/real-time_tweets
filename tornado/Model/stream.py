import threading

from twython import TwythonStreamer

from session import session


class StreamTweets(TwythonStreamer):
    ''' A stream object is used to get streaming data from twitter
    '''

    def on_success(self, data):
        ''' Streaming data keeps coming here
        '''
        if 'text' in data.__str__():
            message = '''{
                "text": "%s",
                "user": "%s"
            }
            ''' % (data['text'].encode('utf-8'),
                   data['user']['screen_name'].encode('utf-8'))

            self.send_message(message)

    def on_error(self, status_code, data):
        message = '{"error": "%s"}' % data.__str__()
        self.send_message(message)

    def on_timeout(self):
        message = '{"error": "timeout"}'
        self.send_message(message)

    def send_message(self, message):
        ''' Get the corresponding socket,
        which is used to write message back to the user
        '''
        thread = threading.current_thread()
        socket = session.get_socket_by_thread(thread)
        socket.write_message(message)
