'''Verificar si un carácter específico está en la cadena con un ciclo y comparaciones.'''
cadena = input("Introduce una cadena de texto: ")
caracter_a_buscar = input("Introduce el carácter para buscar: ")
encontrado = False # Variable para rastrear si se encuentra el carácter
for char in cadena: # en cada caracter de la cadena
    if char == caracter_a_buscar: # si el caracter es igual al caracter a buscar
        encontrado = True # marcar como encontrado
        break # romperemos el bucle
if encontrado: # si se ha encontrado el caracter
    print(f"El carácter '{caracter_a_buscar}' está en la cadena.")
else:
    print(f"El carácter '{caracter_a_buscar}' no está en la cadena.")
    # mostraremos si esta o no el caracter