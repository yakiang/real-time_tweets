import tornado.web
import tornado.httpserver
import tornado. ioloop

from controller import Home, RealSocket


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', Home),
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
