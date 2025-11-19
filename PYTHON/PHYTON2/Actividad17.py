'''Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
incorrecto'''

usuario = input("Introduce el nombre de usuario: ")
contraseña = input("Introduce la contraseña: ")

if usuario == "admin" and contraseña == "1234":
    print("Inicio de sesión correcto")
else:
    print("Nombre de usuario o contraseña incorrectos")

