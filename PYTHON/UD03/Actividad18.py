'''Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia
(^), siendo A y B valores introducidos por teclado, y luego muestre el resultado por pantalla.'''
A = int(input("Introduce el valor de A: ")) # creamos la variable A para que el usuario introduzca un valor
B = int(input("Introduce el valor de B: ")) # creamos la variable B para que el usuario introduzca un valor
resultado = 1 # iniciamos la variable resultado en 1
for _ in range(B): # creamos un bucle que se repita B veces
    resultado *= A # multiplicamos el resultado por A hasta completar las B multiplicaciones
print(f"El resultado de {A} elevado a {B} es: {resultado}")
# mostramos el resultado por pantalla