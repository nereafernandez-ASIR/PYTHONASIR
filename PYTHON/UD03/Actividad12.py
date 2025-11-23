'''Crea una aplicación que dibuje una escalera de números, siendo cada línea un número.
Nosotros le pasamos la altura por teclado.'''
altura = int(input("Introduce la altura de la escalera: "))
for i in range(1, altura + 1): # es igual que la anterior, pero en vez de asteriscos, mostramos el número i tantas veces como su valor
    print(str(i) * i)   # moestramos el número i convertido a cadena tantas veces como su valor i