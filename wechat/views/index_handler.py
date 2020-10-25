import tornado.web


class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render("../templates/index.html")
