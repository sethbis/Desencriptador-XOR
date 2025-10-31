import random

texto = input("Texto: ")

clave = ''
for i in range(len(texto)):
    clave += random.choice('01')


cifrado = ''
for i in range(len(texto)):
    char_ascii = ord(texto[i])  
    bit_clave = int(clave[i])  
    char_cifrado = char_ascii ^ bit_clave  
    cifrado += chr(char_cifrado)  


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
