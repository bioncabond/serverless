from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):      
        url_path = self.path 
        url_components = parse.urlsplit(url_path) 
        query_string_list = parse.parse_qsl(url_components) 
        dic = dict(query_string_list) 
        api_key = 'd15c3cde055c42d0a0e536fa32f3ccdc'

        #grab a specific word from the api we are calling from 
        #EXAMPLE: https://serverless-khaki-alpha.vercel.app/api/define?word=python 
        #find if I asked for a word; look in the query string and see if word is in there (word = python)

#
        # if "food" in dic: 
        #     #url w/o the search key then we concat the thing we are looking for 
        #     # url = 'https://https://api.spoonacular.com/recipes/716429/information?apiKey={api_key}'
        #     url = 'https://api.spoonacular.com/information?apiKey={api_key}&food/search?food=apple'  
        #     r = requests.get(url)


        #     #set that json payload we are looking at to a variable (data)
        #     data = r.json()
        #     print(f"{data}") 
        #     definitions = []  
        #     for food_data in data:
        #         definition = food_data["searchResults"][0]
        #         definitions.append(definition)
        #     message = str(definitions)     
        
        # else: 
        #     message = "Please give me a food to get for you."
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


