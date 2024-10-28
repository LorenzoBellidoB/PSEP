from pip._vendor import requests

num = int(input("Introduce una publicacion: "))
while num != 0:
    if num < 0 | num > 200:
        print("Error, no existe esa publicacion")
    else:
        url = "https://jsonplaceholder.typicode.com/posts/" + str(num)
        response = requests.get(url)
        print(response.json())
        num = int(input("Introduce una publicacion: "))
    