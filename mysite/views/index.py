import tornado.web


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        return self.render("../templates/index.html")
