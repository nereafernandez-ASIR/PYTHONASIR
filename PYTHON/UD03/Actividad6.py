'''Programa que lea un número positivo N y calcule y visualice su factorial N! Siendo el
factorial:
0! = 1
1! = 1
2! = 2 * 1
3! = 3 * 2* 1
N! = N * (N-1) * (N-2) * … * .'''

numero = int(input("Introduce un número positivo para calcular su factorial: "))
factorial = 1 # iniciamos el factorial en 1
if numero <= 0: # aqui indicamos que si el número puesto es 0 o menor de 0, el factorial es 1
    factorial = 1 # el factorial de 0 es 1
else:  # si el número por el contrario es mayor que 0, calculamos su factorial
    for i in range(1, numero + 1): # recorremos desde 1 hasta el número que se indique, incremnentando de 1 en 1 
        factorial *= i # multiplicamos el factorial por el número actual i
print(f"El factorial de {numero} es {factorial}")   # mostramos el resultado por pantalla 