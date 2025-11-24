'''Imprime una cruz en una matriz de tamaño n x n con puntos en el borde, asteriscos en las líneas vertical y horizontal centrales, y espacios en el resto.
Figura para n=7:'''

n = 7
for i in range(n):
    for j in range(n):
        if i == 3 or j == 3 or i == j or i + j == 6:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print() 

