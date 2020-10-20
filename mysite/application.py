import tornado.web
from mysite.views.index import IndexHandler


class Application(tornado.web.Application):

    def __init__(self):
        handles = [
            (r"/", IndexHandler)
        ]
        super(Application, self).__init__(handles)
