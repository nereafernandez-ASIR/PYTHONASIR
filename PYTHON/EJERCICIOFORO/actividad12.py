'''Leer una cadena y construir una nueva cadena con los caracteres en orden inverso.'''
cadena = input("Introduce una cadena: ")
cadena_invertida = "" # iniciamos una cadena vacía para almacenar el resultado
for char in cadena: # recorremos cada carácter de la primera cadena
    cadena_invertida = char + cadena_invertida # añadimos el carácter al inicio de la nueva cadena
print("Cadena invertida:", cadena_invertida) # mostramos la cadena resultante