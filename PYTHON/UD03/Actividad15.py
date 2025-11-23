'''Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos
la altura de la pirámide por teclado. Este es un ejemplo:'''
altura = int(input("Introduce la altura de la pirámide invertida: "))
for i in range(altura, 0, -1): # creamos un bucle for que recorra desde la altura hasta 1 decrementando de 1 en 1
    print(' ' * (altura - i) + '*' * (2 * i - 1)) # mostramos los espacios en blanco con la altura - i que aumenta en cada decremento del bucle y los asteriscos con 2 * i - 1 que disminuye en cada decremento del bucle