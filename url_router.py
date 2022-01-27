"""
Author: deepinwst
Email: wanshitao@donews.com
Date: 19-8-9 下午3:33
"""

from __future__ import unicode_literals
from importlib import import_module


def include(module):
    res = import_module(module)
    urls = getattr(res, "urls")
    return urls


def url_wrapper(urls):
    wrapper_list = []
    for url in urls:
        path, handlers = url
        if isinstance(handlers, (tuple, list)):
            for handle in handlers:
                pattern, handle_class = handle
                wrap = ('{0}{1}'.format(path, pattern), handle_class)
                wrapper_list.append(wrap)
        else:
            wrapper_list.append((path, handlers))
            print(wrapper_list)
    return wrapper_list
