'''Dibuja un ordinograma que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división (Ten en cuenta la división por cero).'''

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

print("Suma:", a + b)
print("Resta:", a - b)
print("Producto:", a * b)

if b != 0:
    print("División:", a / b)
else:
    print("No se puede dividir entre cero")
