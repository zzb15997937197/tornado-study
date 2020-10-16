# 利用python的协程技术，可以开发出类似同步代码的异步行为，因为协程不需要使用线程，减少了线程上下文切换的资源消耗。
import tornado.gen
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


if __name__ == "__main__":
    # 启动IOLooP->调用被lambda封装的协程函数-> 停止IOLoop
    # IOLoop.current().start()
    print("start a coroutine")
    # run_sync() 阻塞当前函数的执行
    IOLoop.current().run_sync(lambda: coroutine_visit())
    # spawn_callback() 不会等待当前函数的执行，因此 前后的print()语句都会被打印出来。
    # IOLoop.current().spawn_callback(coroutine_visit)
    print("end a coroutine")
