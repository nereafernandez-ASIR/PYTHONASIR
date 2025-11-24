'''Imprime una estrella de ocho puntas combinando líneas verticales, horizontales y diagonales con asteriscos en una matriz de tamaño impar n x n (ej. 9x9).
Figura para n=9:'''
n = 9 
matriz = [[' ' for _ in range(n)] for _ in range(n)]
centro = n // 2
for i in range(n):
    matriz[centro][i] = '*'  
    matriz[i][centro] = '*'  
    matriz[i][i] = '*'        
    matriz[i][n - 1 - i] = '*'  
for fila in matriz:
    print(''.join(fila))

