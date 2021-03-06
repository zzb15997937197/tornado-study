from abc import ABC

'''
 options的parse_config_file的使用
'''
import tornado.ioloop
import tornado.web
import tornado.options

'''
tornado.web  是tornado框架的核心web模块。
tornado.ioloop 是tornado框架的核心io循环模块。
ioloop是通过循环，等待客户端连接，以保持长连接的特性。

'''

tornado.options.define("port", default=8000, type=int)
tornado.options.define("list", default=[], multiple=True)


class MainHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write("Hello, world")


if __name__ == "__main__":
    # 使用options解析配置文件时，需要先通过options定义配置文件里的参数，用来接收从config文件中取出来的参数
    tornado.options.parse_config_file("config")
    app = tornado.web.Application([
        (r"/", MainHandler),
    ])
    port = tornado.options.options.port
    print("端口为:", port)
    print("列表为:", tornado.options.options.list)
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
