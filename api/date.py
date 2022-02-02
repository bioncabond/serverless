#set up for the api to handle http request 
from http.server import BaseHTTPRequestHandler
#allows us to manipulate datetime formatting 
from datetime import datetime


#extends the http request handler. 
class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return
