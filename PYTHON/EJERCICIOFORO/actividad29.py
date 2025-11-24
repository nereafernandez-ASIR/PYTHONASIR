'''Este ejemplo es de altura 5: '''
altura = 5
for i in range(altura):
    if i == 0:
        print(' ' * (2 * (altura - 1)) + '*')
    else:
        espacios_antes = ' ' * (2 * (altura - i - 1))
        espacios_medio = ' ' * (2 * i - 1)
        print(espacios_antes + '*' + espacios_medio + '*')
for i in range(altura - 2, -1, -1):
    if i == 0:
        print(' ' * (2 * (altura - 1)) + '*')
    else:
        espacios_antes = ' ' * (2 * (altura - i - 1))
        espacios_medio = ' ' * (2 * i - 1)
        print(espacios_antes + '*' + espacios_medio + '*')
        