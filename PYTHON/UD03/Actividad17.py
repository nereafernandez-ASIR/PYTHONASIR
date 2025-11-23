'''Programa que suma independientemente los pares y los impares de los números
comprendidos entre 100 y 200, y luego muestra por pantalla ambas sumas'''
suma_pares = 0 # creamos la variable suma_pares y iniciamos en 0
suma_impares = 0 # creamos la variable suma_impares y iniciamos en 0

for numero in range(100, 201): # creamos la variable numero que recorre los números del 100 al 200
    if numero % 2 == 0: # si el numero es par 
        suma_pares += numero # sumamos el numero a la variable suma_pares
    else:
        suma_impares += numero # si no es par, sumamos el numero a la variable suma_impares

print("Suma de números pares:", suma_pares)
print("Suma de números impares:", suma_impares)
# mostramos por pantalla la suma de los números pares e impares