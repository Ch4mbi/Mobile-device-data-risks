# Seguridad en dispositivos IoT --  Pentesting en entorno controlado
Proyecto universitario llevado a cabo entre 01/11/2025 - 22/1/2026
[Autor: Ch4mbi](https://github.com/Ch4mbi)

## Descripción
Analisis de vulnerabilidades en dispositivos IoT junto con una serie de ataques sobre una API Node.js con MongoDB (Base de datos noSQL) en un entorno controlado. Se abarca desde teoría (amenazas, malware,...) hasta la ejecución de scripts.

## Contenido
- Vulnerabilidades móviles
- Vulnerabilidades IoT
- Malware y sniffing
- Gestión de MDM
- Ataques prácticos
- Estrategias de mitigación
- Gobernanza

## Ataques
| Script | Tipo de ataque | Descripción |
| --- | --- | --- |
| [bruta.js](https://github.com/Ch4mbi/Mobile-device-data-risks/blob/main/C%C3%B3digos-Ataques/bruta.js) | Fuerza bruta | Combinaciones usuario/contraseña de una lista escrita |
| [regex.py](https://github.com/Ch4mbi/Mobile-device-data-risks/blob/main/C%C3%B3digos-Ataques/regex.py) | Bypass con $regex | Adivina la contraseña carácter a carácter en base a las respuestas del servidor |
| [inyección.py](https://github.com/Ch4mbi/Mobile-device-data-risks/blob/main/C%C3%B3digos-Ataques/inyeccion.py) | Inyección noSQL | Prueba operadores $ne, $gt, $in, $regex |
| [carga.py](https://github.com/Ch4mbi/Mobile-device-data-risks/blob/main/C%C3%B3digos-Ataques/inyeccion.py) | DoS | Envio de peticiones "masivo" |
| [enumeracion.py](https://github.com/Ch4mbi/Mobile-device-data-risks/blob/main/C%C3%B3digos-Ataques/enumeracion.py) | Enumeración de usuarios | Descubre usuarios validos con $regex + $in |
| [login.py](https://github.com/Ch4mbi/Mobile-device-data-risks/blob/main/C%C3%B3digos-Ataques/login.py) | Bypass de autenticación | Salta el login con $not + $eq sin contraseña |

### Requisitos de reproducción del escenario
- Node.js
- Node (node-fetch@2)
- MongoDB (local)
- Angular

## Medidas propuestas de mitigación
- Validación de entradas a las API
- Máximo de intentos fallidos
- Cifrado de las comunicaciones
- 2FA
- MDM para gestionar de manera centralizada dispositivos
- Zero Trust

[Análisis vulnerabilidades en dispositivos móviles](https://github.com/Ch4mbi/Mobile-device-data-risks/blob/main/An%C3%A1lisis%20vulnerabilidades%20y%20ataques%20a%20dispositivos%20m%C3%B3viles.md)
