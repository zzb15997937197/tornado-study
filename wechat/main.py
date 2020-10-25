import tornado.ioloop
from wechat.application import IndexApplication
from tornado.options import options, define, parse_command_line, parse_config_file

define("port", default=8888, help="run port")

if __name__ == "__main__":
    # 获取application
    app = IndexApplication()
    # 绑定端口
    app.listen(options.port)
    # 启动应用
    tornado.ioloop.IOLoop.current().start()
