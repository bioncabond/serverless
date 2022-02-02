from http.server import BaseHTTPRequestHandler
from urllib import parse 
import requests 

class handler(BaseHTTPRequestHandler):

    def do_GET(self):      
        #grab the url path 
        url_path = self.path 
        
        #take the path and split it up into different components (see docs for more info) 
        url_components = parse.urlsplit(url_path) 
        query_string_list = parse.parse_qsl(url_components.query) 
        dic = dict(query_string_list) 

        #grab a specific word from the api we are calling from 
        #EXAMPLE: https://serverless-khaki-alpha.vercel.app/api/define?word=python 
        #find if I asked for a word; look in the query string and see if word is in there (word = python)

        if "word" in dic:
            url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
            r = requests.get(url + dic['word'])
            data = r.json()
            definitions = []
            for word_data in data:
                definition = word_data["meanings"][0]["definitions"][0]["definition"]
                definitions.append(definition)
            message = str(definitions)        
        else:
            message = "Please give me a word to define"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers() 

        self.wfile.write(message.encode())
        return 