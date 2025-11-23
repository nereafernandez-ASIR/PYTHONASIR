'''Programa donde el usuario "piensa" un número del 1 al 100 y el ordenador intenta
adivinarlo. Es decir, el ordenador irá proponiendo números una y otra vez hasta adivinarlo (el
usuario deberá indicarle al ordenador si es mayor, menor o igual al número que ha pensado).'''
import random # importamos la librería random para generar números aleatorios
print("Piensa un número del 1 al 100 y yo intentaré adivinarlo.")
minimo = 1 # límite inferior será 1
maximo = 100 # límite superior será 100
intentos = 0 # contador de intentos comienza en 0
while True: # bucle infinito hasta que se adivine el número
    intentos += 1 # aquí se incrementará el contador según el número de intentos
    adivinanza = random.randint(minimo, maximo) # creamos la variable adivinanza con un número aleatorio entre los límites
    print(f"¿Es {adivinanza}?")
    respuesta = input("Responde con 'mayor', 'menor' o 'igual': ").lower()
    if respuesta == 'igual': # si la respuesta es igual, finaliza el bucle
        print(f"¡He adivinado tu número {adivinanza} en {intentos} intentos!")
        break
    elif respuesta == 'mayor': # si la respuesta es mayor, aumentamos el minimo en 1
        minimo = adivinanza + 1
    elif respuesta == 'menor': # si la respuesta es menor, disminuimos el maximo en 1
        maximo = adivinanza - 1
    else: # si la respuesta no es válida, se lo indicamos al usuario
        print("Respuesta no válida. Por favor, responde con 'mayor', 'menor' o 'igual'.")
    if minimo > maximo: # si se pasa del límite, indicamos que hubo un error y salimos del bucle
        print("Parece que ha habido un error. ¿Estás seguro de tus respuestas?")
        break