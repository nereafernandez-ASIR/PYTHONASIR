'''Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún
número negativo o no'''
hay_negativo = False # iniciamos la variable en falso
for _ in range(100): # repetimos 100 veces
    numero = int(input("Introduce un número no nulo: "))
    if numero < 0: # si el número es negativo, cambiamos la variable a verdadero
        hay_negativo = True # indicamos que se ha leído un número negativo
if hay_negativo: # si la variable es verdadera, mostramos el mensaje
    print("Se ha leído al menos un número negativo.")   
else:
    print("No se ha leído ningún número negativo.") 
    