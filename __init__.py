import tornado.web
import tornado.httpserver
import tornado. ioloop

from controller import HomePage, RealSocket


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', HomePage),
            (r'/socket', RealSocket)
        ]

        settings = {
            'template_path': 'View/templates',
            'static_path': 'View/static'
        }

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
