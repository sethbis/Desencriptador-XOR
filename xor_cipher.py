import random

"""texto = input("Texto: ")
clave = ''.join(random.choice('01') for _ in range(len(texto)))
cifrado = ''.join(chr(ord(texto[i]) ^ int(clave[i])) for i in range(len(texto)))
descifrado = ''.join(chr(ord(cifrado[i]) ^ int(clave[i])) for i in range(len(texto)))
print(f"Texto plano: {texto}\nClave: {clave}\nCifrado: {cifrado}\nDescifrado: {descifrado}")"""



texto = input("Texto: ")

clave = ''
for i in range(len(texto)):
    clave += random.choice('01')


cifrado = ''
for i in range(len(texto)):
    char_ascii = ord(texto[i])  # Convertir carácter a número ASCII
    bit_clave = int(clave[i])   # Convertir '0' o '1' a número
    char_cifrado = char_ascii ^ bit_clave  # Aplicar XOR
    cifrado += chr(char_cifrado)  # Convertir número a carácter


descifrado = ''
for i in range(len(cifrado)):
    char_ascii = ord(cifrado[i])
    bit_clave = int(clave[i])
    char_descifrado = char_ascii ^ bit_clave
    descifrado += chr(char_descifrado)


print(f"\nTexto plano: {texto}")
print(f"Clave: {clave}")
print(f"Cifrado: {cifrado}")
print(f"Descifrado: {descifrado}")
