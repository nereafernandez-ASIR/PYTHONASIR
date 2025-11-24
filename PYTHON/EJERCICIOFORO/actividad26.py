'''Imprime un rombo sólido de altura 2n-1, centrado, usando asteriscos.
Figura para n=4:'''

altura = 4
print() 
for i in range(1, altura + 1):
    print(" " * (altura - i) + "*" * (2 * i - 1)) 
for i in range(altura - 1, 0, -1):
    print(" " * (altura - i) + "*" * (2 * i - 1))      