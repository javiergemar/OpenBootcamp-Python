'''
Escribe un programa capaz de mostrar todos los números
impares desde un número de inicio y otro final.

Primero lo vamos a realizar con un if
'''

numInicial = int(input('Introduce el número inicial: '))
numFinal = int(input('Introduce el número final: '))

for i in range(numInicial,numFinal):
    if i % 2 == 0:
        print(i, 'es un número par')
    else:
        print(i, 'no es un número par')

# Ahora realizado con un while

contador = numInicial

while contador <= numFinal:
    if contador % 2 == 0:
        print(contador, 'es un número par')
    else:
        print(contador, 'no es un número par')
    contador += 1