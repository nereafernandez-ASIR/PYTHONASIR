'''En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
Si los tres dados son seis, mostrar el mensaje “Excelente”
Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
Si un dado se obtiene seis, mostrar el mensaje “Regular”
Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
(Use el control switch).'''

import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)

print(f"Resultados: {dado1}, {dado2}, {dado3}")

seis = [dado1, dado2, dado3].count(6)

if seis == 3:
    print("Excelente")
elif seis == 2:
    print("Muy bien")
elif seis == 1:
    print("Regular")
else:
    print("Pésimo")
