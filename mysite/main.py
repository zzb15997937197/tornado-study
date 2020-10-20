from mysite.application import Application
import tornado.ioloop
import mysite.config

if __name__ == "__main__":
    app = Application()
    app.listen(mysite.config.options["port"])
    tornado.ioloop.IOLoop.current().start()
