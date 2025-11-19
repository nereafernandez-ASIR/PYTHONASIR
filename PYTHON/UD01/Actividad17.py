'''Dibuja un ordinograma de un programa que lea dos números y lo visualiza en orden
ascendente'''

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

if a < b:
    print(a, b)
else:
    print(b, a)
