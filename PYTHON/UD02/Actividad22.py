'''Escriba un programa que recibe como datos de entrada una hora expresada en horas,
minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán,
transcurrido un segundo.'''

h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))

s += 1
if s == 60:
    s = 0
    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 24:
            h = 0

print("Hora después de un segundo:", h, ":", m, ":", s)
