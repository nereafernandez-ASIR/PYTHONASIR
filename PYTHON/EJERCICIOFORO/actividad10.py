'''Leer una cadena y contar cuántos caracteres son letras mayúsculas.'''
cadena = input("Introduce una cadena de texto: ") 
contador_mayusculas = 0 # ponemos el contandor a 0
for char in cadena: # recorremos cada caracter de la cadena
    if 'A' <= char <= 'Z': # comprobamos si el caracter es mayuscula
        contador_mayusculas += 1 # incrementamos el contador si es mayuscula
print("Número de letras mayúsculas en la cadena:", contador_mayusculas) 
