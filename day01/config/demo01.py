from abc import ABC

import tornado.ioloop
import tornado.web
import tornado.options

'''
tornado.web  是tornado框架的核心web模块。
tornado.ioloop 是tornado框架的核心io循环模块。
ioloop是通过循环，等待客户端连接，以保持长连接的特性。

'''

tornado.options.options.define("port", default=8008, type=int)


class MainHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write("Hello, world")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
    ])
    # 使用options定义全局的参数
    app.listen(tornado.options.options.port)
    # # 使用options解析配置文件
    # tornado.options.parse_config_file("config")
    tornado.ioloop.IOLoop.current().start()
