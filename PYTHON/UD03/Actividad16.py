'''Programa que lee una secuencia de notas (con valores que van de 0 a 10) que termina con
el valor -1 y nos dice si hubo o no alguna nota con valor 10'''
notas = [] # creamos una lista vacía [] para almacenar las notas introducidas
nota = float(input("Introduce una nota (de 0 a 10) o -1 para terminar: ")) # leemos las notas hasta que se introduzca -1
while nota != -1: # aqui indicamos la condición que mientras se cumpla el bucle seguirá pidiendo notas, en este caso que sea diferente de -1
    if 0 <= nota <= 10: # comprobamos que la nota está en el rango válido entre 0 y 10
        notas.append(nota) # si la nota es válida, la añadimos a la lista de notas
    else: # si la nota no es válida, mostramos un mensaje de error
        print("Nota inválida. Por favor, introduce una nota entre 0 y 10.")
    nota = float(input("Introduce una nota (de 0 a 10) o -1 para terminar: "))
if 10 in notas: # comprobamos si hay alguna nota con un 10 en la lista de notas
    print("Hubo al menos una nota con valor 10.") # si es así, saldrá que hubo un 10
else:
    print("No hubo ninguna nota con valor 10.") # si no es el caso, saldrá que no hubo ningún 10