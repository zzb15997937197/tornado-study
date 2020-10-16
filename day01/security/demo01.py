'''
通过RequestHandler get_cookie()和set_cookie()方法，能够方便的对cookie()进行读写。
'''
import tornado.web
from tornado.web import Application
import uuid
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        if not self.get_cookie("session"):
            self.set_cookie("session", str(self.get_cookie()))
        else:
            print(self.get_cookie("session"))
            self.write("your session was set!")


if __name__ == "__main__":
    app = Application([
        (r"/hello", MainHandler)
    ], cookie_secret="SECRET_DONT_LEAK")
    app.listen(8008)
    tornado.ioloop.IOLoop.current().start()
