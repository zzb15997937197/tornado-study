'''
使用get_secure_cookie()和set_secure_cookie()替换原来的get_cookie()和set_cookie()方法
'''
import tornado.web
from tornado.web import Application
import uuid
import tornado.ioloop

dict_sessions = {}


class BaseHandler(tornado.web.RequestHandler):

    # current_user为 RequestHandler里方法
    def get_current_user(self):
        print([x for x in dict_sessions])
        session_id = self.get_secure_cookie("session_id")
        if session_id is None:
            return "无用户"
        return dict_sessions[session_id]


class MainHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("hello" + name)


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
        # 登录规则，名字长度为3个才允许登录
        name = self.get_argument("name")
        if len(name) < 3:
            self.redirect("/login")
            session_id = str(uuid.uuid4())
            dict_sessions[session_id] = name
            self.set_cookie("session_id", session_id)
            print(self.get_cookie("session_id"))
            print("登录成功!")
        else:
            print("name无效,请输出长度大于3的name!")


if __name__ == "__main__":
    app = Application([
        (r"/hello", MainHandler),
        (r"/login", LoginHandler)
    ],
        cookie_secret="SECRET_DONT_LEAK",
        login_url="/login")
    app.listen(8008)
    tornado.ioloop.IOLoop.current().start()
