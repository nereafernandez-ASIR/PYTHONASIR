'''Leer una cadena y construir una nueva cadena dejando sólo los caracteres que son consonantes (sin listas, usando condiciones y concatenación).'''
cadena = input("Introduce una cadena texto: ")
nueva_cadena = ""
for caracter in cadena:
    if caracter.isalpha() and caracter.lower() not in "aeiou": 
        nueva_cadena += caracter
print(f"Caracter añadido: {caracter}")
print("Cadena resultante de consonantes:", nueva_cadena)
