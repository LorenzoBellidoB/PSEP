from pip._vendor import requests
#coding: latin1

url = "https://jsonplaceholder.typicode.com/todos/10"

# Petición GET
response = requests.delete(url)
print(response.status_code)
print(response.json())