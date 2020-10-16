import tornado.ioloop
import tornado.web
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

'''
tornado.web  是tornado框架的核心web模块。
tornado.ioloop 是tornado框架的核心io循环模块。
ioloop是通过循环，等待客户端连接，以保持长连接的特性。

'''


@gen.coroutine
def coroutine_visit():
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch("http://www.baidu.com")
    print(response.body.decode("utf-8"))


class CoroutineHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("执行协程函数")
        print("start a coroutine")
        # IOLoop.current().run_sync(lambda: coroutine_visit())
        # .spawn_callback()函数只有在IOLoop运行时，才能够被调用
        IOLoop.current().spawn_callback(coroutine_visit)
        self.write("<br>")
        self.write("结束协程函数")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/hello", CoroutineHandler)
    ])
    app.listen(8002)
    tornado.ioloop.IOLoop.current().start()
