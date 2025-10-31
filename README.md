XOR Cipher
Programa simple de cifrado y descifrado usando operación XOR con clave binaria aleatoria.
Descripción
Este programa implementa un cifrado XOR básico donde:

Genera una clave binaria aleatoria (0s y 1s)
Cifra texto aplicando XOR entre cada carácter y su bit correspondiente
Descifra usando la misma operación XOR

Funcionamiento

Entrada: Usuario ingresa texto plano
Clave: Se genera una clave binaria aleatoria (un bit por cada carácter)
Cifrado: Cada carácter se convierte a ASCII, se aplica XOR con su bit de clave
Descifrado: Se aplica XOR nuevamente para recuperar el texto original

bashpython xor_cipher.py
Requisitos

Python 3.x

Nota
XOR es una operación simétrica: aplicar XOR dos veces con la misma clave devuelve el valor original.
