'''Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.'''
cadena = input("Introduce una cadena de texto: ") # Solicitar al usuario que ingrese una cadena
caracter = input("Introduce un carácter a buscar: ") # Solicitar al usuario que ingrese un carácter para buscar
contador = 0 # Inicializar el contador en 0
for char in cadena: # recorre cada carácter en la cadena
    if char == caracter: # Si el carácter actual coincide con el carácter buscado
        contador += 1 # incrementará el contador en 1
print(f"El carácter '{caracter}' aparece {contador} veces en la cadena.")
# Mostrará cuantas veces aparece el carácter en la cadena
