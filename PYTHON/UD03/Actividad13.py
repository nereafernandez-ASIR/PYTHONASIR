'''Crea una aplicación que dibuje una escalera de números, siendo cada línea números
empezando en uno y acabando en el numero de la línea. Este es un ejemplo, si introducimos un
5 como altura:'''
altura = int(input("Introduce la altura de la escalera: "))
for i in range(1, altura + 1): # recorremos desde 1 hasta la altura indicada incrementando de 1 en 1
    for j in range(1, i + 1): # recorremos desde 1 hasta el valor de i (la línea actual) incrementando de 1 en 1
        print(j, end="") # mostramos el valor de j sin salto de línea
    print()  # hacemos un salto de línea después de cada línea de números 