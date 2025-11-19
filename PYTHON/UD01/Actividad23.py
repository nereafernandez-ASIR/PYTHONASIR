'''Dibuja un ordinograma de un programa que lea una secuencia de números no nulos hasta
que se introduzca un 0, y luego muestre si ha leído algún número negativo, cuantos positivos y
cuantos negativos.'''

positivos = 0
negativos = 0
tiene_negativo = False

num = float(input("Introduce un número (0 para terminar): "))
while num != 0:
    if num > 0:
        positivos += 1
    else:
        negativos += 1
        tiene_negativo = True
    num = float(input("Introduce otro número (0 para terminar): "))

print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)

if tiene_negativo:
    print("Se ha leído algún número negativo")
else:
    print("No se ha leído ningún número negativo")
