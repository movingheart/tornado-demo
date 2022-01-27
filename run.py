"""
Author: deepinwst
Email: wanshitao@donews.com
Date: 19-8-9 下午3:32
"""

from __future__ import unicode_literals
import tornado.httpserver
import tornado.ioloop
import tornado.web
from url_router import include, url_wrapper
from controllers.test.index import IndexHandler
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

application = tornado.web.Application(url_wrapper([
    (r'/(\w+)', IndexHandler),
    (r'/test/', include('controllers.test.urls'))
]), debug=True)


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
