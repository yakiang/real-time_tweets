from uuid import uuid1

import tornado.web


class HomePage(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html', session=uuid1())
