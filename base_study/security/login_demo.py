'''
使用get_secure_cookie()和set_secure_cookie()替换原来的get_cookie()和set_cookie()方法
案例实现:  身份验证框架
1) 用户大于等于3个即可登录。

'''
import tornado.web
from tornado.web import Application
import uuid
import tornado.ioloop

dict_sessions = {}


class BaseHandler(tornado.web.RequestHandler):

    # current_user为 RequestHandler里的属性，为只读，因此需要使用get_current_user()方法为其赋值。
    def get_current_user(self):
        print(dict_sessions)
        session_id = self.get_secure_cookie("session")
        if session_id is None:
            return
        session = session_id.decode("utf-8")
        if session not in dict_sessions:
            return
        return dict_sessions[session]


class MainHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        # tornado.escape.xhtml_escape()方法用来转义字符串或者方法，self.current_user表示的是方法
        # 转义<,>,",',&, 对xml或者html有效
        name = tornado.escape.xhtml_escape(self.current_user)
        print("转义前:" + self.current_user, "转义后:", name)
        self.write("hello,用户:" + name + "!")


class LoginHandler(BaseHandler):

    # 获取登录页面表单
    def get(self, *args, **kwargs):
        self.write('<!DOCTYPE html>'
                   '<html lang="en">'
                   '<head>'
                   '<meta charset="UTF-8">'
                   '<title>Title</title>'
                   '</head>'
                   '<body>'
                   '<form action="/login" method="post">'
                   'name: <input type="text" name="name">'
                   '<input type="submit" value="登录">'
                   '</form>'
                   '</body>'
                   '</html>')

    # 验证用户是否允许登录，不允许登录那么跳转至登录页面
    def post(self, *args, **kwargs):
        # 登录规则，名字长度大于或等于3个才允许访问，否则需要输入用户名和密码
        name = self.get_argument("name")
        if len(name) < 3:
            self.redirect("/login")
            session_id = str(uuid.uuid4())
            self.set_secure_cookie("session", session_id)
            dict_sessions[self.get_secure_cookie("session").decode("utf-8")] = name
            print(self.get_cookie("session"))
            print(self.get_secure_cookie("session"))
        else:
            self.write("允许访问!")


if __name__ == "__main__":
    app = Application([
        (r"/hello", MainHandler),
        (r"/login", LoginHandler)
    ],
        cookie_secret="SECRET_DONT_LEAK",
        login_url="/login")
    app.listen(8008)
    tornado.ioloop.IOLoop.current().start()
