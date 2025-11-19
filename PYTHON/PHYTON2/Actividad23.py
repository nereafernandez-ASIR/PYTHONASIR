'''Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
según sea el caso y el total a pagar de la compra.'''

valor = float(input("Introduce el valor de compra: "))
pago = input("¿Forma de pago (contado/tarjeta)? ").lower()

if pago == "contado":
    descuento = valor * 0.05
    total = valor - descuento
    print("Descuento del 5%:", descuento)
else:
    recargo = valor * 0.03
    total = valor + recargo
    print("Recargo del 3%:", recargo)

print("Total a pagar:", total)
