'''
定义路由!
'''
from mywebchat.views.all_handler import IndexHandler, ChatSocketHandler
import os

import tornado.web


class IndexApplication(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/index', IndexHandler),
            (r'/chat_socket', ChatSocketHandler)
        ]
        settings = dict(
            # 初始参数设置
            cookie_secret="YOU_CANT_GUESS_MY_SECRET",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True, )
        print(settings)
        super(IndexApplication, self).__init__(handlers, **settings)
