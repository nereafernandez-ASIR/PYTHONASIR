'''Dibuja un ordinograma de un programa que lea tres números y nos diga cual es mayor, cual
menor y cuales son iguales.'''

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))

mayor = max(a, b, c)
menor = min(a, b, c)

print("El mayor es:", mayor)
print("El menor es:", menor)

if a == b == c:
    print("Los tres son iguales")
