'''Leer una cadena desde teclado y mostrarla carácter por carácter usando un ciclo for y el índice.'''
cadena = input("Introduce una cadena: ") # leer cadena desde teclado
for i in range(len(cadena)): # creamos la variable i que recorrera el rango de la longitud ("len") de la cadena
    print(f"Carácter en la posición {i}: {cadena[i]}") # mostramos la posición y el carácter correspondiente