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
            r = requests.get(url + dic['number'])
            data = r.json()
            num_facts = []  
            for num_data in data:
                facts = num_data["text"]
                num_facts.append(facts)
            message = str(num_facts)     
        else: 
            message = "Please pick a whole number."

        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers() 

        self.wfile.write(message.encode())

        return 


