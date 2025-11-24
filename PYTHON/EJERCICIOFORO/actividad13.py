'''Leer una cadena y eliminar todos los espacios, construyendo una cadena continua.'''
cadena=input("Introduce una cadena de texto: ")
cadena_sin_espacios="" # iniciamos una cadena vacía para almacenar el resultado                   
for caracter in cadena: # recorremos cada caracter de la primera cadena
    if caracter!=" ": # comprobamos si el caracter no es un espacio
        cadena_sin_espacios+=caracter # si no es un espacio, lo añadimos a la nueva cadena
print("Cadena sin espacios:", cadena_sin_espacios) # mostramos el resultado 