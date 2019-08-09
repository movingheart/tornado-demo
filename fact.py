import tornado.ioloop
import tornado.web
import json
from concurrent.futures import ThreadPoolExecutor, as_completed


class FactorialService(object):
    def __init__(self):
        self.cache = {}

    def calc(self, n):
        if n in self.cache:
            return self.cache[n],True
        s = 1
        for i in range(1, n):
            s *= i
        self.cache[n] = s
        return s,False

    def son(self, i):
        print("thread i:", i)
        return i
    
    def multi_cal(self, n):
        executor = ThreadPoolExecutor(max_workers=3)
        all_tasks = [executor.submit(self.son, (i,)) for i in range(n)]
        
        for future in as_completed(all_tasks):
            data = future.result()
            print("thread done:", data)


class FactorialHandler(tornado.web.RequestHandler):
    service = FactorialService()

    def get(self):
        n = int(self.get_argument("n") or 1)
        fact, cached = self.service.calc(n)
        result = {
                "n": n,
                "fact": fact,
                "cached": cached
                }
        self.set_header("Content-Type", "application/json;charset=UTF-8")
        self.service.multi_cal(n)
        self.write(json.dumps(result))


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/fact", FactorialHandler),
        ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
