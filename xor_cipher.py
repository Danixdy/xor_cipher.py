import random

def xor_cipher(texto):
    clave = ''.join(random.choice("01") for _ in range(len(texto)))
    cifrado = ''.join(chr(ord(texto[i]) ^ int(clave[i])) for i in range(len(texto)))
    descifrado = ''.join(chr(ord(cifrado[i]) ^ int(clave[i])) for i in range(len(cifrado)))
    return cifrado, descifrado, clave

texto = input("Texto: ")
cifrado, descifrado, clave = xor_cipher(texto)
print(f"Clave: {clave}")
print(f"Cifrado: {cifrado}")
print(f"Descifrado: {descifrado}")