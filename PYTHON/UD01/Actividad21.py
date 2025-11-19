'''Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
mensaje de si ha leído número negativo o no'''

negativo = False

for i in range(100):
    num = float(input(f"Introduce el número {i+1}: "))
    if num < 0:
        negativo = True

if negativo:
    print("Se ha leído al menos un número negativo")
else:
    print("No se ha leído ningún número negativo")
