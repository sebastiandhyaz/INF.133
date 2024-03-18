import requests

url = "http://localhost:8000/pizza"
headers = {'Content-type': 'application/json'}

mi_pizza = {
    "tamaño": "Grande",
    "masa": "Delgada",
    "toppings": ["Jamon", "Queso"]
}

mi_hamburguesa = {
    "tamaño": "Mediana",
    "masa": "Gruesa",
    "toppings": ["Queso", "Tomate"]
}
response = requests.post(url, json=mi_pizza, headers=headers)
response2 = requests.post(url, json=mi_hamburguesa, headers=headers)
print(response.json())
print(response2.json())