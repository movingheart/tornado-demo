"""
Author: deepinwst
Email: wanshitao@donews.com
Date: 19-8-9 下午3:41
"""

import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self, name):
        greeting = self.get_argument('greeting', 'hello')
        self.write(greeting + ' {}, frendly user!'.format(name))


class Reverse(tornado.web.RequestHandler):
    def get(self, input_str):
        self.write(input_str[::-1])


class Calculator(tornado.web.RequestHandler):
    def get(self, a, b):
        s = sum([int(a), int(b)])
        self.write("Result:{}".format(s))
