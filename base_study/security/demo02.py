'''
使用get_secure_cookie()和set_secure_cookie()替换原来的get_cookie()和set_cookie()方法
'''
import tornado.web
from tornado.web import Application
import uuid
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):

    # get_secure_cookie()获取了最原始的cookie,get_cookie()方法获取到加密后的cookie
    def get(self, *args, **kwargs):
        if not self.get_secure_cookie("session"):
            self.set_secure_cookie("session", str(uuid.uuid4()))
        else:
            print(self.get_secure_cookie("session"))
            print(self.get_cookie("session"))
            self.write("your session was set!")


if __name__ == "__main__":
    app = Application([
        (r"/hello", MainHandler)
    ], cookie_secret="SECRET_DONT_LEAK")
    app.listen(8008)
    tornado.ioloop.IOLoop.current().start()
