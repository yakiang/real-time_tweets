from threading import Thread

from stream import StreamTweets


class TweetsThread(Thread):
    ''' Each thread corresponds to a stream object.
    '''

    APP_KEY = 'WUTmfyk9II1fzkPz1Zsg'
    APP_SECRET = 'OFaDKdG4P3OYVpuAG5Cso6DgcApKF51VOkr0ADq38'
    OAUTH_TOKEN = '446119470-jkYNeCyluDeP4QxK1sp0IimXnF2AJah74X0q9t1p'
    OAUTH_TOKEN_SECRET = 'sPxoYPqVp3UxkUuGPQ0MFusu0A4ynA0rH42rnHzwSEPId'
    stream = StreamTweets(APP_KEY, APP_SECRET,
                          OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    def __init__(self, hashtag, socket):
        self.track = hashtag
        Thread.__init__(self)

    def run(self):
        ''' What a thread really does
        '''
        self.stream.statuses.filter(track=self.track)
