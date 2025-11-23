'''Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura
de la pirámide por teclado. Este es un ejemplo, si introducimos 5 de altura:'''
altura = int(input("introduce la altura de la pirámide: ")) # creamos la variable altura, para que el usuario introduzca la altura
for i in range(1, altura + 1): # creamos un bucle for que recorra desde 1 hasta la altura + 1 
    print(' '* (altura - i) + '*' * (2 * i - 1)) # mostramos los espacios en blanco con la altura - i que disminuye en cada incremento del bucle y los asteriscos con 2 * i - 1 que aumenta en cada incremento del bucle