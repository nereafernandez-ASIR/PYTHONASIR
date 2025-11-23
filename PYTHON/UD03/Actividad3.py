'''Programa que muestre los números pares comprendidos entre el 1 y el 200. Esta vez utiliza
un contador sumando de 1 en 1.'''
for numero in range(1, 201): #el rango es de 1 a 200
    if numero % 2 == 0: #aquí indicamos que si el número es divisible entre 2, %2 == 0, es par 
        print(numero) # aquí se mostrarían los números pares, que indicamos antes con el %2 == 0.
        