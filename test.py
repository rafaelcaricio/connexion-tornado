import tornado.web
import tornado.ioloop

from connexion_tornado import TornadoApp


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


app = TornadoApp()
app.add_api(yaml="""
swagger: "2.0"
info:
  title: "Hello World API"
  version: "1.0"
paths:
  /:
    get:
      summary: Hello to everyone
      description: ""
      operationId: test.MainHandler#get
      produces:
        - text/plain;
      responses:
        200:
          description: greeting response
          schema:
            type: string
          examples:
            "text/plain": "Hello Example"
""")
app.listen(8888)

tornado.ioloop.IOLoop.current().start()
