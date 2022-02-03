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
            url = url + dic['number'] + "?json"

            print(url)
            req = requests.get(url)
            
            print(req, "a small string")

           #with this out of the code; you got to the [] for num facts
            data = req.json()
            num_facts = []  

            fact = data.get('text')
            # number_fact = data.get('number')

                # num_facts.append(fact)
                # print("num facts:", num_facts)
            message = str(fact)
        else: 
            message = "PLEASE PICK A NUMBER."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        # self.send_header('Content-type', 'application/json')
        self.end_headers() 

        self.wfile.write(message.encode())
        return 


if __name__ == "__main__":

    anything = handler() 
    anything.do_Get()
