from http.server import BaseHTTPRequestHandler
from urllib import parse,request
# import requests 

class handler(BaseHTTPRequestHandler):

    def do_GET(self):      
        #grab the url path 
        url_path = self.path 
        
        #take the path and split it up into different components (see docs for more info) 
        url_components = parse.urlsplit(url_path) 
        query_string_list = parse.parse_qsl(url_components) 
        dic = dict(query_string_list) 
        #api_key = d15c3cde055c42d0a0e536fa32f3ccdc

        #grab a specific word from the api we are calling from 
        #EXAMPLE: https://serverless-khaki-alpha.vercel.app/api/define?word=python 
        #find if I asked for a word; look in the query string and see if word is in there (word = python)

        if "food" in dic: 
            #url w/o the seach key then we concat the thing we are looking for 
            url = 'https://api.spoonacular.com/recipes/716429/information?apiKey=d15c3cde055c42d0a0e536fa32f3ccdc&includeNutrition=true.'  
            r = request.get(url + dic['food'])


            #set that json payload we are looking at to a variable (data)
            data = r.json() 
            definitions = []  
            for word_data in data:
                definition = word_data["meanings"][0]["definitions"][0]["definition"]
                definitions.append(definition)
            message = str(definitions)     
        
        else: 
            message = "Please give me a food to get for you."
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers() 

        self.wfile.write(message.encode())
        return 
