'''
RequestHandler称为接入点函数

'''
import tornado.web
import tornado.ioloop
from tornado.web import RequestHandler, Application
import tornado.options

tornado.options.define("username")
tornado.options.define("password")


class profileHandler(RequestHandler):

    # 重写ReuqestHandler里的initialize()方法，该方法的参数由application定义的Url映射以dict方式给出的。
    def initialize(self, database):
        self.database = database

    def get(self, *args, **kwargs):
        database = self.database
        tornado.options.parse_config_file(database)
        print(tornado.options.options.username + "," + tornado.options.options.password)
        username = self.get_argument("username")
        # get_argument()和get_arguments()只获取url上的参数
        # 获取url单个参数
        pw = self.get_argument("password")
        print("username", username, ",password", pw)
        # 获取url上get请求上查询的相同字符串参数以及post请求提交参数的集合
        # localhost:8008/hello?username=张&password=123456&address=1&address=2
        # adress : ['1','2']
        print(self.get_arguments("address"))
        self.write("ok")

    def post(self, *args, **kwargs):
        # post测试 get_arguments()方法
        print(self.get_arguments("address"))
        self.write("ok")

    def delete(self, *args, **kwargs):
        pass


if __name__ == "__main__":
    app = Application([
        (r"/hello", profileHandler, dict(database="example.db"))
    ])
    app.listen(8008)
    tornado.ioloop.IOLoop.current().start()
