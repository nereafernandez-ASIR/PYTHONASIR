'''Este ejemplo es de altura 5:'''
altura = 5
for i in range(altura):
    if i == 0:
        print('4')
    elif i == altura - 1:
        print('4 ' * altura)
    else:
        espacios = ' ' * (2 * i - 1)
        print('4' + espacios + '4')