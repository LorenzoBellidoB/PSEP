from pprint import pprint
from pip._vendor import requests

url = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(url)

pprint(response.json())
    
