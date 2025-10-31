import random

def xor_cipher(texto, clave):
    return ''.join(chr(ord(texto[i]) ^ int(clave[i])) for i in range(len(texto)))

texto = input("Texto: ")
clave = ''.join(random.choice('01') for _ in range(len(texto)))

cifrado = xor_cipher(texto, clave)
descifrado = xor_cipher(cifrado, clave)

print(f"Clave: {clave}")
print(f"Cifrado: {cifrado}")
print(f"Descifrado: {descifrado}")