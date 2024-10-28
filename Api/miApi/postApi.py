#coding: latin1

from pip._vendor import requests

url = "https://jsonplaceholder.typicode.com/todos"

todo = {"userId": 1, "title": "Buy milk", "complete": False}
response = requests.post(url, json=todo)

print(response.json())

print("Codigo de estado: ", response.status_code)

userId= input("Introduce el número de usuario: ")
title= input("Introduce el título: ")
completed= True if (input("¿Tarea completada?"))== "Si" else False

user = {"userId": userId, "title": title, "complete": completed}
response = requests.post(url, json=user)

print(response.json())