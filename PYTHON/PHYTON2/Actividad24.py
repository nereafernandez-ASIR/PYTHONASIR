'''Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
Visualizar el descuento y el total a pagar por la compra'''

monto = float(input("Monto de compra: "))
dia = input("Día de la semana: ").lower()

if dia == "martes" or dia == "jueves":
    descuento = monto * 0.15
else:
    descuento = 0

total = monto - descuento

print("Descuento aplicado:", descuento)
print("Total a pagar:", total)
