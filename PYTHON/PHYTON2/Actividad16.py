'''Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene.'''

num = int(input("Introduce un número entre 0 y 99999: "))

if num >= 0 and num <= 99999:
    cifras = len(str(num))
    print("El número tiene", cifras, "cifras")
else:
    print("Número fuera de rango")
