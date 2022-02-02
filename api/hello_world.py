#lets print/run something in this file 
from http.server import BaseHTTPRequestHandler
####we dont need date/time### 

class handler(BaseHTTPRequestHandler):

    def do_GET(self): 
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers() 

        #before we grabbes the datetime string 
        #.encode()? will convert 

        message = "Hello World!" 
        self.wfile.write(message.encode())