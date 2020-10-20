'''
RequestHandler的常用函数学习:
1) 接入点函数
2) 输入函数
3) 输出函数

'''
import tornado.web
import tornado.ioloop
from tornado.web import RequestHandler, Application
import tornado.options
import tornado.httpserver

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
        print(self.get_query_argument("username"))

        # RequestHandler的request属性的使用
        # 获取ip地址
        print("ip:", self.request.remote_ip)
        # 获取请求的主机地址
        print("host:", self.request.host)
        # 完整请求的uri
        print("uri:", self.request.uri)
        #   打印结果:
        # ip: ::1    ::1 表示就是localhost ,如果使用127.0.0.1访问就能打印出实际的 127.0.0.1
        # host: localhost:8008
        # uri: /hello?username=%E5%BC%A0&password=123456&address=1&address=2
        # 查询的参数
        print("query_uri:", self.request.query)
        # query_uri: username=%E5%BC%A0&password=123456&address=1&address=2
        # headers, 以字典形式表达httpheaders
        print("headers", self.request.headers)
        headers = self.request.headers
        for i in headers:
            print(i, headers.get(i))
        # cookies, 客户端提交的cookies字典
        cookies = self.request.cookies
        for i in cookies:
            print("cookies:", i, ",", cookies.get(i))
        # files 以字典方式表达客户端要上传的文件，每个文件名对应一个HTTPFile
        files = self.request.files
        print(files)
        # {'file1': [{'filename': '1.txt', 'body': b"hands_on_case_menu_t_parent_menu_tree_ite_0bd197e0_fk_hands_on_\tparent_menu_tree_item_id\tmeiya_edu_saas_admin\thands_on_case_menu_tree_item\tid\r\n\r\n\r\ndjango.db.utils.IntegrityError: Problem installing fixtures: The row in table 'hands_on_case_items_result' with primary key '17' has an invalid foreign key: hands_on_\r\ncase_items_result.case_item_id contains a value '61' that does not have a corresponding value in hands_on_case_items.id.\r\n", 'content_type': 'text/plain'}]}
        self.set_status(0, "成功!")
        self.write({"code": 0, "msg": "成功!"})
        self.set_header("Content_Type", "application/json")
        # 响应json形式:
        # {
        #     "code": 0,
        #     "msg": "成功!"
        # }

    def post(self, *args, **kwargs):
        # post测试 get_arguments()方法用来获取url上以及body里的form_data里的参数, get_body_argument用来获取form_data里的参数
        print(self.get_arguments("address"))
        print(self.get_body_argument("address"))
        self.write("ok")

    def delete(self, *args, **kwargs):
        pass


if __name__ == "__main__":
    app = Application([
        (r"/hello", profileHandler, dict(database="example.db"))
    ])
    app.listen(8008)
    tornado.ioloop.IOLoop.current().start()
