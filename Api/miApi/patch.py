from pip._vendor import requests
#coding: latin1

url = "https://jsonplaceholder.typicode.com/todos/10"

# Petici�n GET
response = requests.get(url)
print(response.json())

# Crear Diccionario de datos a modificar
todo = {"title": "Wash car"}

# Relizamos petici�n PUT
response = requests.patch(url, json=todo)
print(response.json())
print(response.status_code)