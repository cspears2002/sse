#! /usr/bin/python

from flask import Flask, request, Response, render_template

# from tornado.wsgi import WSGIContainer
# from tornado.httpserver import HTTPServer
# from tornado.ioloop import IOLoop

app = Flask(__name__)

def event_stream():
  count = 0
  while count < 1000:
    print 'data: {0}\n\n'.format(count)
    yield 'data: {0}\n\n'.format(count)
    count += 1

@app.route('/my_event_source')
def sse_request():
  return Response(
          event_stream(),
          mimetype='text/event-stream')

@app.route('/')
def page():
  return render_template('index.html')


if __name__ == '__main__':

  print "Please open a web browser to http://127.0.0.1:5000."

  # Spin up the app
  app.run()
  # http_server = HTTPServer(WSGIContainer(app))
  # http_server.listen(5000)
  # IOLoop.instance().start()