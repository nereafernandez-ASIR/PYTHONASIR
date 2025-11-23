'''Programa que dada una cantidad de euros que el usuario introduce por teclado (múltiplo de
5 €) mostrará los billetes de cada tipo que serán necesarios para alcanzar dicha cantidad
(utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar el mínimo de billetes posible.
Por ejemplo, si el usuario introduce 145 el programa indicará que será necesario 1 billete de 100
€, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo 29 billetes de 5, que aunque
sume 145 € no es el mínimo número de billetes posible).'''
cantidad = int(input("Introduce una cantidad de euros (múltiplo de 5 €): "))
if cantidad % 5 != 0: # comprobar si es múltiplo de 5 unicamente
    print("La cantidad debe ser un múltiplo de 5 €.") 
else: 
    billetes = [500, 200, 100, 50, 20, 10, 5] # mostraremos los billetes de mayor a menor
    resultado = {} # creamos una lista vacía para almacenar el resultado
    for billete in billetes: # tomamos cada billete 
        if cantidad >= billete: # comprobamos si la cantidad es mayor o igual que el billete
            num_billetes = cantidad // billete # calculamos el número de billetes necesarios
            cantidad -= num_billetes * billete # restamos la cantidad correspondiente
            resultado[billete] = num_billetes # almacenamos el resultado en el diccionario
    print("Desglose de billetes necesarios:") # mostramos el resultado
    for billete, num in resultado.items(): # recorremos el diccionario para mostrar el resultado
        print(f"{num} billete(s) de {billete} €") # mostramos el número de billetes de cada tipo
        # el f despues de print es para formatear la cadena y poder incluir variables dentro de ella
        