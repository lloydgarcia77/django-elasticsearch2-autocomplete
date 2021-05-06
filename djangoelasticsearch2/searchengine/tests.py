from django.test import TestCase
import json, requests 
# Create your tests here.



response = requests.get('https://jsonplaceholder.typicode.com/comments') 
json_reponse = json.loads(response.text) 


for x in json_reponse:
    name = x['name']
    email = x['email']
    postid = x['postId']
    body = x['body']
