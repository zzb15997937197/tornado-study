'''
定义路由!
'''
from wechat.views.index_handler import IndexHandler

import tornado.web


class IndexApplication(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/index', IndexHandler),
        ]
        super(IndexApplication, self).__init__(handlers)
