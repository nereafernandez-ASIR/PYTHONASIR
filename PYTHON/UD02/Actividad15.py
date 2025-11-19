'''Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales
son iguales.'''

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))

mayor = max(a, b, c)
menor = min(a, b, c)

print("El mayor es:", mayor)
print("El menor es:", menor)

if a == b == c:
    print("Los tres son iguales")
