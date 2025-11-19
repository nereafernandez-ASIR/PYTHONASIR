'''Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
mensaje indicando cuántos son positivos y cuantos negativos'''

positivos = 0
negativos = 0

for i in range(100):
    num = float(input(f"Introduce el número {i+1}: "))
    if num > 0:
        positivos += 1
    else:
        negativos += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
