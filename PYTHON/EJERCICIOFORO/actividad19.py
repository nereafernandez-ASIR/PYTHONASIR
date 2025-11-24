'''Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, donde solo se imprimen los bordes y el centro.'''
n = int(input("Introduce altura del diamante: "))
altura = 2 * n - 1
for i in range(altura):
    if i < n:
        espacios_externos = n - i - 1
        if i == 0:
            print(" " * espacios_externos + "*")
        else:
            espacios_internos = 2 * i - 1
            print(" " * espacios_externos + "*" + " " * espacios_internos + "*")
    else:
        j = altura - i - 1
        espacios_externos = n - j - 1
        if j == 0:
            print(" " * espacios_externos + "*")
        else:
            espacios_internos = 2 * j - 1
            print(" " * espacios_externos + "*" + " " * espacios_internos + "*")
        
