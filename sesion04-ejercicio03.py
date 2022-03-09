'''
Escribe un programa que sea capaz de mostrar
los números del 1 al 100 en orden inverso.
'''

numeros = list(range(100, 0, -1))
print(numeros)

# Con buble for
delUnoAlCien = list(range(1, 101))
for i in reversed(delUnoAlCien):
    print('Número', i)

# Otro bucle for
delUnoAlCien = list(range(1, 101))
for i in range(len(delUnoAlCien) -1, -1, -1):
    print('Número', delUnoAlCien[i])