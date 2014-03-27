from twython import TwythonStreamer


class GetTweets(TwythonStreamer):

    APP_KEY = 'WUTmfyk9II1fzkPz1Zsg'
    APP_SECRET = 'OFaDKdG4P3OYVpuAG5Cso6DgcApKF51VOkr0ADq38'
    OAUTH_TOKEN = '446119470-jkYNeCyluDeP4QxK1sp0IimXnF2AJah74X0q9t1p'
    OAUTH_TOKEN_SECRET = 'sPxoYPqVp3UxkUuGPQ0MFusu0A4ynA0rH42rnHzwSEPId'
    stream = TwythonStreamer(APP_KEY, APP_SECRET,
                      OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    def __init__(self, hashtag):
        self.track = hashtag
        self.stream.statuses.filter(track=self.track)

    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code






