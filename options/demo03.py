import tornado.ioloop

import tornado.web


# 使用options.parse_commandline() 来解析命令行的参数

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")
        print("调用成功!")


def make_app():
    return tornado.web.Application(
        [
            (r"/hello", MainHandler),
        ]
    )


def main():
    app = make_app()
    app.listen(8008)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
