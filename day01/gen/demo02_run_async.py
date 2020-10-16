# 利用python的协程技术，可以开发出类似同步代码的异步行为，因为协程不需要使用线程，减少了线程上下文切换的资源消耗。
import tornado.gen
import tornado.web
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient


# @gen.coroutine装饰器，用来表示该函数为一个协程函数
@gen.coroutine
def coroutine_visit():
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch("http://www.baidu.com")
    print(response.body.decode("utf-8"))


@gen.coroutine
def outer_visit():
    print("另一个协程函数")
    yield coroutine_visit()
    print("结束")


class CoroutineHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write("异步请求开始")
        print("异步请求开始")
        self.write("<br>")
        IOLoop.current().spawn_callback(coroutine_visit)
        self.write("异步请求完成")
        print("异步请求完毕")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/hello", CoroutineHandler)
    ])
    app.listen(8003)
    tornado.ioloop.IOLoop.current().start()
