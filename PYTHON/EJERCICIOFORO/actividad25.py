'''Imprime un triángulo invertido de altura n con asteriscos en el borde, y líneas internas de relleno alternadas entre espacios y asteriscos.

Figura para n=6:

******  
* * * *
*     *
* * * *
*     *
******  
'''
n = 7  
m = 6  

for i in range(m):
    for j in range(n):
        if i == 0 or i == m-1:
            print("*", end="")
        elif i % 2 == 1:
            if j % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            if j == 0 or j == n-1:
                print("*", end="")
            else:
                print(" ", end="")
    print()

