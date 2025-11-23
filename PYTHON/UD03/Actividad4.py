'''Programa que muestre los números desde el 1 hasta un número N que se introducirá por
teclado.'''
N = int(input("Introduce un número N:")) #aquí se pide el número N por teclado, que será valor numerico entero por el int.
for numero in range(1, N + 1): #aquí indicamos que el rango empieza en 1 y termina en N+1 porque el último número no se incluye.
    print(numero) #aquí se muestra los numeros del rango que indicamos arriba, en el valor creado "numero".