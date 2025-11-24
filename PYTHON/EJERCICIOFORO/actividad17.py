'''Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez.'''
cadena = input("Introduce una cadena de texto: ")
nueva_cadena = "" 
for caracter in cadena:
    if cadena.count(caracter) > 1 and caracter not in nueva_cadena:
        nueva_cadena += caracter
print("Nueva cadena con caracteres repetidos:", nueva_cadena)
