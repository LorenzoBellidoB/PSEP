from pip._vendor import requests

num = int(input("Introduce un usuario: "))
while num != 0:
    if num < 0:
        print("Error")
    else:
        url = "https://jsonplaceholder.typicode.com/todos/" + str(num)
        response = requests.get(url)
        print(response.json())
        num = int(input("Introduce un usuario: "))
    