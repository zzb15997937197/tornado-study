'''
该文件同步模拟的服务的被调用方 ,端口为: 8002
'''
import tornado.ioloop
import tornado.options
import tornado.web
import time
from tornado.options import define, options

define('port', default=8002, help='run port', type=int)


class SyncHandler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(3)
        self.write("同步代码")


if __name__ == '__main__':
    tornado.options.parse_command_line()

    app = tornado.web.Application(
        handlers=[
            (r'/sync', SyncHandler),
        ],
        template_path='templates',
        static_path='static',
        debug=True,
    )
    app.db = {}
    print("端口:", options.port)
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
