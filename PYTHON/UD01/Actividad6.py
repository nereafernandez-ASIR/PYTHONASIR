'''Dibuja un ordinograma que dado el precio de un artículo y el precio de venta real nos
muestre el porcentaje de descuento realizado.'''

precio_original = float(input("Introduce el precio original: "))
precio_venta = float(input("Introduce el precio de venta: "))

descuento = ((precio_original - precio_venta) / precio_original) * 100
print("El descuento es del:", descuento, "%")
