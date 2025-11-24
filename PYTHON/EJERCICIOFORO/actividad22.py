'''Imprime un cuadrado de lado n con bordes de asteriscos y las dos diagonales marcadas, dejando espacios en el resto.
Figura para n=7:'''

n = 6  # Tamaño de la figura

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i + j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  
