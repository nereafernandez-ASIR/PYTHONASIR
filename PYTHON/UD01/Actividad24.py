'''Dibuja un ordinograma de un programa que calcule y escriba la suma y el producto de los
10 primeros números naturales.'''

suma = 0
producto = 1

for i in range(1, 11):
    suma += i
    producto *= i

print("Suma de los 10 primeros números naturales:", suma)
print("Producto de los 10 primeros números naturales:", producto)
