'''Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de
10.'''

num = int(input("Introduce un número: "))

if num % 10 == 0:
    print("Es múltiplo de 10")
else:
    print("No es múltiplo de 10")
