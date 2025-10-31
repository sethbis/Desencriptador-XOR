import random
def aplicar_xor(texto, clave):
    resultado = ''
    for i in range(len(texto)):
        char_ascii = ord(texto[i])  
        bit_clave = int(clave[i])   
        char_xor = char_ascii ^ bit_clave  
        resultado += chr(char_xor)  
    return resultado


texto = input("Texto: ")

clave = ''
for i in range(len(texto)):
    clave += random.choice('01')

cifrado = aplicar_xor(texto, clave)
descifrado = aplicar_xor(cifrado, clave)

print(f"\nTexto plano: {texto}")
print(f"Clave: {clave}")
print(f"Cifrado: {cifrado}")
print(f"Descifrado: {descifrado}")
