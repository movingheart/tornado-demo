"""
Author: deepinwst
Email: wanshitao@donews.com
Date: 19-8-9 下午3:40
"""

from .index import IndexHandler, Reverse, Calculator

urls = [
    (r"hello/(\w+)", IndexHandler),
    (r"reverse/(\w+)", Reverse),
    (r"cal/(\d+)/(\d+)", Calculator)
]