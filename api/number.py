from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):      
        url_path = self.path 
        url_components = parse.urlsplit(url_path) 
        query_string_list = parse.parse_qsl(url_components) 
        dic = dict(query_string_list) 
        
        if "number" in dic: 
            url = 'http://numbersapi.com/'
            r = requests.get(url)


            #set that json payload we are looking at to a variable (data)
            data = r.json()
            # print(f"{data}") 
            num_facts = []  
            for num_data in data:
                definition = num_data["text"][0]
                num_facts.append(definition)
            message = str(num_facts)     
        else: 
            message = "Please pick a whole number."

        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers() 

        self.wfile.write(message.encode())

        return 


