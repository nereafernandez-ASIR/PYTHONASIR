'''Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'.'''
def reemplazar_vocales(cadena): # función para reemplazar vocales por '*'
    vocales = "aeiouAEIOU" # definición de vocales
    nueva_cadena = "" # cadena resultante
    for char in cadena:  # recore cada carácter de la cadena 
        if char in vocales: # si el carácter es vocal
            nueva_cadena += '*' # la reemplazara por un *
        else: # si no es vocal
            nueva_cadena += char # se añade el carácter original
    return nueva_cadena # nos mostrará la nueva cadena

cadena = input("Introduce una cadena de texto: ")
resultado = reemplazar_vocales(cadena)
print("Cadena con vocales reemplazadas por '*':", resultado)