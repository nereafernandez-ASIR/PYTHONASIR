'''Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación (concatenar carácter a carácter con un ciclo).'''
cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")
cadena_concatenada = ""  # cadena resultante
for caracter in cadena1:  # recorremos cada caracter de la primera cadena
    cadena_concatenada += caracter  # añadimos el caracter a la cadena 
for caracter in cadena2:  # recorremos cada caracter de la segunda cadena
    cadena_concatenada += caracter  # añadimos el caracter a la cadena 
print("Cadenas concatenadas:", cadena_concatenada)  # mostramos el resultado