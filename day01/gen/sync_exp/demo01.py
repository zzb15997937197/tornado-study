'''
模拟同步过程,该文件为服务的调用方
'''

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.httpclient import HTTPClient
from tornado.options import define, options

define('port', default=8010, help='run port', type=int)


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        print("获取当前用户")
        self.write("当前用户")


class AbcHandler(BaseHandler):
    def get(self):
        self.write('ok')


class SyncHandler(BaseHandler):
    def get(self):
        """同步代码"""
        client = HTTPClient()
        response = client.fetch("http://127.0.0.1:8002/sync?id=3")
        self.write(response.body)


if __name__ == '__main__':
    tornado.options.parse_command_line()

    app = tornado.web.Application(
        handlers=[
            (r'/abc', AbcHandler),
            (r'/sync', SyncHandler),
        ],
        template_path='templates',
        static_path='static',
        debug=True,
    )
    app.db = {}
    app.listen(options.port)
    print("端口:", options.port)
    tornado.ioloop.IOLoop.instance().start()
