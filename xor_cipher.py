import random

def xor_cipher(texto):
    clave = ''.join(random.choice('01') for _ in range(len(texto)))
    cifrado = ''.join(chr(ord(texto[i]) ^ int(clave[i])) for i in range(len(texto)))
    return cifrado, clave

texto = input("Texto: ")
cifrado, clave = xor_cipher(texto)
descifrado = xor_cipher(cifrado)[0] 
print(f"Clave: {clave}")
print(f"Cifrado: {cifrado}")
print(f"Descifrado: {descifrado}")