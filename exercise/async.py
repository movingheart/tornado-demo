#!/usr/bin/env python


from tornado.httpclient import HTTPClient


def syncchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body


############################################
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future


def async_fetch_future(url):
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch(url)
    fetch_future.add_done_callback(
        lambda f: my_future.set_result(f.result())
    )
    return my_future


if __name__ == "__main__":
    # print(syncchronous_fetch("http://www.baidu.com"))
    print(async_fetch_future("http://www.baidu.com").result())
