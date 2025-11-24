'''Imprime un cuadrado de lado n con borde y diagonales en asteriscos, y un cuadro hueco centrado dentro.

Figura para n=9:'''

N = 9 

for i in range(N):
    fila = ""
    for j in range(N):
        
        if i == 0 or i == N - 1:
            fila += "*"
        
        elif j == 0 or j == N - 1:
            fila += "*"
            
        
        elif i == j or i + j == N - 1:
            fila += "*"
            
       
        elif (i == 1 and j == 2) or (i == 1 and j == 6) or \
             (i == 2 and j == 3) or (i == 2 and j == 5) or \
             (i == 6 and j == 2) or (i == 6 and j == 6) or \
             (i == 5 and j == 3) or (i == 5 and j == 5):
            fila += "*" 
            
        else:
         
            fila += " "
    
    print(fila)