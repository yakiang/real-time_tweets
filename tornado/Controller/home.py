import tornado.web


class HomePage(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render('home.html')
