'''
Escribe una función que pueda decirte si un número (número entero) es primo o no.
'''

def numeroPrimo(numero):
    resto = numero % numero
    return resto

numero = int(input('Introduce un número para comprobar si es primo: '))

seraPrimo = numeroPrimo(numero)

if seraPrimo == 0:
    print('¡¡¡PREMIO!!!, es número primo')
else:
    print('No es un número primo')