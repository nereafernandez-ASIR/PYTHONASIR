'''Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego
muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos.'''
contador_positivos = 0 
contador_negativos = 0
ha_negativo = False # iniciamos la variable en falso
while True: # mientras sea verdadero 
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0: # si el numéro es 0, salimos del bucle
        break
    if numero > 0: # si el número es positivo, incrementamos el contador de positivos
        contador_positivos += 1
    else: # si el número es negativo, incrementamos el contador de negativos
        contador_negativos += 1
        ha_negativo = True # indicamos que se ha leído un número negativo
if ha_negativo:
    print("Se ha leído al menos un número negativo.")
print("números positivos leídos:", contador_positivos)
print("números negativos leídos:", contador_negativos)
# mostraremos el resultado de positivos y negativos por pantalla