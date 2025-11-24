'''Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena.'''
cadena = "Los ejercicios de Python me traen de cabeza"
nueva_cadena = "" # Cadena vacía donde se irá almacenando la nueva cadena
for caracter in cadena: # recorremos cada carácter de la cadena original
    if caracter == "e": # si el carácter es una 'e'
        nueva_cadena += "i" # concatenamos una 'i' a la nueva cadena
    else:
        nueva_cadena += caracter # si no, concatenamos el carácter original
print(nueva_cadena) # Imprimimos la nueva cadena
