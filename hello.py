import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_cookie("mycookie"):
            self.set_cookie("mycookie", "myvalue")
            self.write("Hello, world.<br> Your cookie was not set!")
        else:
            self.write("Your cookie was set!")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
        ], debug=True)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
