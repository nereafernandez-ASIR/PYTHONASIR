'''Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal.'''
cadena = input("Introduce una cadena de texto: ")
nueva_cadena = "" # iniciamos una cadena vacía para almacenar el resultado
vocales = "aeiouAEIOU" # definimos las vocales mayúsculas y minúsculas
for char in cadena: # recorremos cada carácter de la cadena original
    if char in vocales: # comprobamos si el carácter es una vocal
        nueva_cadena += char * 2 # duplicamos la vocal y la añadimos a la nueva cadena
    else:
        nueva_cadena += char # añadimos el carácter tal cual si no es vocal
print("Nueva cadena:", nueva_cadena)