'''Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas).'''
cadena = input("Introduce una cadena de texto: ") 
nueva_cadena = "" # Inicia una nueva cadena vacía
for char in cadena: # recorre cada carácter en la cadena
    if char.lower() not in 'aeiou': # Si el carácter no es una vocal (ignora mayúsculas/minúsculas)
        nueva_cadena += char # Añadirá el carácter a la nueva cadena
print(f"Cadena original: {cadena}") 
print(f"Cadena sin vocales: {nueva_cadena}")
# Mostrará la cadena original y la nueva cadena sin vocales