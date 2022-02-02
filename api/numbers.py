from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):      
        url_path = self.path 
        url_components = parse.urlsplit(url_path) 
        query_string_list = parse.parse_qsl(url_components.query) 
        dic = dict(query_string_list) 
              
        if "number" in dic: 
            url = 'http://numbersapi.com/'
            r = requests.get(url + dic["number"]) 
           
           #with this out of the code; you got to the [] for num facts
            data = r.json()
            num_facts = []  

            for num_data in data:
                fact = num_data["text"][0]
                num_facts.append(fact)
            message = str(num_facts)     
        
        else: 
            message = "PLEASE PICK A NUMBER."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers() 

        self.wfile.write(message.encode())
        return 


