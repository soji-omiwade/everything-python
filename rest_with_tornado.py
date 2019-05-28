""" this file was created by Barry Rowe
    - 05/24/2019
"""
import tornado.web
import tornado.ioloop

counter = 0

class MyHandler(tornado.web.RequestHandler):
    def get(self):        
        self.write(str(counter).encode('utf-8'))
        
    def post(self):
        global counter
        counter+=1
        self.write("post")
        
    def delete(self):
        global counter
        counter = 0
        self.write("delete")
        
def main():
    app = tornado.web.Application([
       (r"/", MyHandler)
    ])    
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
        
if __name__=="__main__":
    main()