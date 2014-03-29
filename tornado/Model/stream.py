from twython import TwythonStreamer


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
            self.socket.write_message(message)

    def on_error(self, status_code, data):
        message = '{"error": "%s"}' % data.__str__()
        self.socket.write_message(message)

    def on_timeout(self):
        message = '{"error": "timeout"}'
        self.socket.write_message(message)

    def set_socket(self, socket):
        self.socket = socket
