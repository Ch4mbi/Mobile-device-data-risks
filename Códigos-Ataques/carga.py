import requests

for i in range(1000):
    requests.post("http://localhost:3000/api/login",
                  json={"username": "admin", "admin123": "test"})
    print(f"Petición {i}")