'''Dibuja un ordinograma que toma como dato de entrada un número que corresponde a la
longitud de un radio (La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud
de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del
círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la
esfera que corresponde con dicho radio'''

import math

radio = float(input("Introduce el radio: "))
diametro = 2 * radio
longitud = math.pi * diametro
area = math.pi * radio**2
volumen = (4/3) * math.pi * radio**3

print("Longitud de la circunferencia:", longitud)
print("Área del círculo:", area)
print("Volumen de la esfera:", volumen)
