'''Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre
el porcentaje de descuento realizado.'''

precio_original = float(input("Precio original: "))
precio_venta = float(input("Precio de venta: "))

descuento = ((precio_original - precio_venta) / precio_original) * 100
print("Descuento realizado:", descuento, "%")
