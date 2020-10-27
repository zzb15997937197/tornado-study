import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado import gen

from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on given port", type=int)

# 定义一个空的字典
clients = dict()


class IndexHandler(tornado.web.RequestHandler):

    # 异步访问
    @tornado.web.asynchronous
    def get(self):
        print("访问系统首页,端口号为:", options.port)
        self.render("index.html")


class MyWebSocketHandler(tornado.websocket.WebSocketHandler):

    # 有新的连接时open()函数将会被调用,将客户端的连接统一放到clients
    def open(self, *args, **kwargs):
        self.id = self.get_argument("id")
        self.stream.set_nodelay(True)
        clients[self.id] = {"id": self.id, "object": self}
        print(clients)
        print("建立连接...")

    # 服务器收到消息
    def on_message(self, message):
        print("端口号为:", options.port)
        print("client %s received a message: %s" % (self.id, message))

    # 关闭连接时被调用
    def on_close(self):
        if self.id in clients:
            del clients[self.id]
        print("client %s is closed" % self.id)

    def check_origin(self, origin):
        return True


import threading
import time
import datetime


def send_time():
    while True:
        for key in clients.keys():
            msg = str(datetime.datetime.now())
            clients[key]["object"].write_message(msg)
            print("write to client %s:%s" % (key, msg))
        time.sleep(1)


app = tornado.web.Application([
    (r"/call", IndexHandler),
    (r"/websocket", MyWebSocketHandler)
])

if __name__ == "__main__":
    threading.Thread(target=send_time).start()
    parse_command_line()
    app.listen(options.port)
    print("端口号为:", options.port)
    tornado.ioloop.IOLoop.instance().start()
