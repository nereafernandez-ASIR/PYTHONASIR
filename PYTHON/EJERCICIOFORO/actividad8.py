'''Convertir todas las letras a mayúsculas o minúsculas usando ciclos y sumas de caracteres (sin usar los métodos upper() o lower())'''

def convertir_mayusculas(texto): # convierte todas las letras minúsculas a mayúsculas
    resultado = "" # cadena vacía para almacenar el resultado
    for char in texto: # recorrer cada carácter en el texto
        if 'a' <= char <= 'z': # verificar si el carácter es una letra minúscula
            resultado += chr(ord(char) - 32) # resultado es el carácter convertido a mayúscula, este se hace usando la función chr() y ord() que convierten entre caracteres y sus valores ASCII
        else:
            resultado += char # si no es una letra minúscula, se añade tal cual al resultado
    return resultado

def convertir_minusculas(texto): # convierte todas las letras mayúsculas a minúsculas
    resultado = "" # cadena vacía para almacenar el resultado
    for char in texto: # recorrer cada carácter en el texto
        if 'A' <= char <= 'Z': # verificar si el carácter es una letra mayúscula
            resultado += chr(ord(char) + 32) # resultado es el carácter convertido a minúscula, este se hace usando la función chr() y ord() que convierten entre caracteres y sus valores ASCII
        else:
            resultado += char # si no es una letra mayúscula, se añade tal cual al resultado
    return resultado

frase = input("Ingrese una frase: ")


print("Frase en mayúsculas:", convertir_mayusculas(frase))

print("Frase en minúsculas:", convertir_minusculas(frase))