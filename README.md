# Connexion Tornado
Extension to use Connexion with Tornado Web framework.

## Installation

In a console run:

    pip install connexion-tornado

## Usage

Minimal example of how to use the Connexion-Tornado integration:

```python
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
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a Pull Request