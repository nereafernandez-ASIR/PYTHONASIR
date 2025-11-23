'''Programa que lea 100 números no nulos y luego muestre un mensaje indicando cuántos
son positivos y cuantos negativos'''
contador_positivos = 0 # iniciamos el contador de positivos en 0
contador_negativos = 0 # iniciamos el contador de negativos en 0
for _ in range(100): # repetimos 100 veces
    numero = int(input("introduce un número no nulo: "))
    if numero > 0: # si el número es positivo, incrementamos el contador de positivos
        contador_positivos += 1
    else: # si el número es negativo, incrementamos el contador de negativos
        contador_negativos += 1
print(f"Se han leído {contador_positivos} números positivos.") # mostraremos el contador por aqui de positivos y negativos
print(f"Se han leído {contador_negativos} números negativos.") 