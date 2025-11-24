'''Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene.'''
cadena = input("Introduce una cadena de caracteres: ")
contador_numeros = 0 # Inicializamos el contador a 0
for caracter in cadena: # Recorremos cada caracter de la cadena
    if caracter.isdigit(): # Comprobamos si el caracter es un dígito
        contador_numeros += 1 # Incrementamos el contador si es un dígito
print("Número de caracteres numéricos:", contador_numeros) # Mostramos el resultado