'''Crea una aplicación que dibuje una escalera de asteriscos. Nosotros le pasamos la altura de
la escalera por teclado. Este es un ejemplo si insertaras un 5 de altura:'''
altura = int(input("Introduce la altura de la escalera: "))
for i in range(1, altura + 1): # creamos la variable i que inicia en 1 y va hasta la altura indicando la altura de la escalera, que se incrementa de 1 en 1
    print('*' * i)      # mostramos la escalera entre las comillas saldra el * veces i, que es la altura que se ha indicado
    