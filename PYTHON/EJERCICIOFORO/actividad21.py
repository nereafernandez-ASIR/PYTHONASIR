'''Imprime una pirámide de altura n donde se alternan asteriscos y espacios, formando un patrón de huecos internos.
Figura para n=6:'''    

def piramide(n):
    for i in range(1, n + 1):
        left_spaces = n - i

        if i == 1:
            print(" " * left_spaces + "*")
        elif i == 4:
            print(" " * left_spaces + "* " * i)
        else:
            inner_spaces = 2 * i - 3
            print(" " * left_spaces + "*" + " " * inner_spaces + "*")
    print("*" * (2*n - 1))
piramide(6)
