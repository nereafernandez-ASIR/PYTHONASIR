'''Leer una cadena y contar cuántas vocales contiene.'''
cadena = input("Introduce una cadena de texto: ")
vocales = "aeiouAEIOU" # Definimos las vocales mayúsculas y minúsculas
contador = 0 # Inicializamos el contador de vocales
for char in cadena: # recorremos cada carácter en la cadena
    if char in vocales: # comprobamos si el carácter es una vocal
        contador += 1 # incrementamos el contador si es una vocal
print("Número de vocales en la cadena:", contador)
