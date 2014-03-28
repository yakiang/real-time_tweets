from twython import TwythonStreamer


class StreamTweets(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            message = '{"tweet": "%s"}' % data['text'].encode('utf-8')
            self.socket.write_message(message)

    def on_error(self, status_code, data):
        print data.__str__()

    def on_timeout(self):
        print 'time out'

    def set_socket(self, socket):
        self.socket = socket
