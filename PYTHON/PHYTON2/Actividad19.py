'''Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares,
con el siguiente menú de opciones:
Bienvenido a su Cajero Virtual
1. Ingresar dinero en cuenta
2. Retirar dinero de la cuenta
3. Salir'''

saldo = 1000

print("Bienvenido a su Cajero Virtual")
print("1. Ingresar dinero en cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Salir")

opcion = int(input("Elige una opción: "))

if opcion == 1:
    ingreso = float(input("Cantidad a ingresar: "))
    saldo += ingreso
    print("Saldo actual:", saldo)
elif opcion == 2:
    retiro = float(input("Cantidad a retirar: "))
    if retiro <= saldo:
        saldo -= retiro
        print("Saldo actual:", saldo)
    else:
        print("Fondos insuficientes")
elif opcion == 3:
    print("Gracias por usar el cajero.")
else:
    print("Opción no válida")
