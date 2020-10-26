import tornado.web
import tornado.websocket
import logging
import uuid
import datetime
import random


class BaseHandler(tornado.web.RequestHandler):
    pass


# 视图
class IndexHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render(self.settings["template_path"] + "/index.html")


class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    # 存储所有在线用户
    waiters = set()


    def __init__(self, application, request, username=None, client_id=None, **kwargs):
        self.username = username
        self.client_id = client_id
        super().__init__(application, request, **kwargs)

    def open(self):
        self.waiters.add(self)
        self.client_id = random.randint(0, 10000)
        print("当前在线用户有:", self.waiters)

    def on_close(self):
        print("用户:" + str(self) + "下线啦!")
        self.waiters.remove(self)
        print("当前在线用户有:", self.waiters)

    def on_message(self, message):
        # 收到客户端的消息时会被调用
        logging.info("获取到消息:", message)
        parsed = tornado.escape.json_decode(message)
        print(parsed)
        self.username = parsed["username"]
        chat = {
            "id": str(uuid.uuid4()),
            "body": parsed["body"],
            "type": "message",
            "client_id": self.client_id,
            "username": self.username,
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        chat["html"] = tornado.escape.to_basestring(
            self.render_string(self.settings["template_path"] + "/message.html", message=chat)
        )
        ChatSocketHandler.send_updates(chat)

    @classmethod
    def send_updates(cls, chat):  # 向所有客户端发送聊天消息
        logging.info("sending message to %d waiters", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
            except Exception as e:
                logging.error("Error sending message", exc_info=True)
