'''La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el
control switch).'''

nombre = input("Nombre del postulante: ")
facultad = input("Facultad (Ingeniería/Medicina/Derecho): ").lower()

if facultad == "ingeniería":
    importe = 800
    mensualidad = 400
elif facultad == "medicina":
    importe = 1200
    mensualidad = 700
elif facultad == "derecho":
    importe = 1000
    mensualidad = 600
else:
    print("Facultad no válida")
    exit()

igv = (importe + mensualidad) * 0.18
total = importe + mensualidad + igv

print(f"\nPostulante: {nombre}")
print(f"Importe: {importe}")
print(f"Mensualidad: {mensualidad}")
print(f"IGV (18%): {igv}")
print(f"Total a pagar: {total}")
