'''Imprime la letra M mayúscula usando asteriscos en una matriz cuadrada de tamaño impar n. Las líneas de la M deben visualizarse usando asteriscos, con espacios en el resto.
Figura para n=7: '''     

n = int(input("Ingrese un número impar para el tamaño de la matriz: ")) 
if n % 2 == 0:
    print("Por favor, ingrese un número impar.")
else:
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n - 1 or (i == j and i <= n // 2) or (i + j == n - 1 and i <= n // 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()