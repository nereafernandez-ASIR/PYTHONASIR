'''Programa que muestre en líneas separadas lo siguiente:
ZYWXVUTSRQPONMLKJIHGFEDCBA, YWXVUTSRQPONMLKJIHGFEDCBA,
WXVUTSRQPONMLKJIHGFEDCBA, ...., DCBA, CBA, BA, A.'''
for letra in range(90, 64, -1): #creamos el valor "letra" que va desde el 90 (Z) hasta el 65 (A) en orden decreciente
    for subletra in range(90, letra - 1, -1): #creamos el valor "subletra" que va desde el 90 (Z) hasta el valor de "letra" en orden decreciente
        print(chr(subletra), end="") #aquí se muestra el valor de "subletra" convertido a carácter
    print()  #aquí se hace un salto de línea para que se muestre los resultados en líneas separadas