from twython import TwythonStreamer


class StreamTweets(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            # with open('tweets.txt', 'a') as f:
                # f.write('\n\n' + data.__str__().encode('utf-8'))
            message = '''{
                "text": "%s",
                "user": "%s"
                }
                ''' % (data['text'].encode('utf-8'), 
                       data['user']['screen_name'].encode('utf-8'))
            self.socket.write_message(message)

    def on_error(self, status_code, data):
        print data
        message = '{"error": "%s"}' % status_code.__str__()
        self.socket.write_message(message)

    def on_timeout(self):
        message = '{"error": "timeout"}'
        self.socket.write_message(message)

    def set_socket(self, socket):
        self.socket = socket
