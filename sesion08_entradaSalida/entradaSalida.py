print('* * * * * Forma mala o antigua (versiones anteriores a Python 2.6) * * * * *')

numero = 5
texto = 'quijote'
otromas = 1.2

print('El número es %d y el texto es %s y tiene %f' % (numero, texto, otromas))

'''
El % seguido de la letra es un placeholder, que es una referencia a lo que va a ir en ese punto.
%d (digit) indica que ahí va un número, %s (string) indica cadena y %f un float.
'''

print('Valor flotante: %f' % otromas)
# En el caso de tener solo un elemento no es necesario paréntesis.

print('Valor flotante: %.2f' % otromas)
# Mostraría el flotante con dos decimales.

print('* * * * * Forma fea (versiones de Python hasta la 3.6) * * * * *')

numero = 5
texto = 'quijote'
otromas = 1.2

print('El número es {} y el texto es {} y tiene {}'.format(numero, texto, otromas))

print('El número es {} y el texto es {} y tiene {}'.format(texto, otromas, numero))

print('El número es {0} y el texto es {1} y tiene {2}'.format(texto, otromas, numero))

print('El número es {2} y el texto es {0} y tiene {1}'.format(texto, otromas, numero))

print('El número es {n1} y el texto es {n2} y tiene {n3}'.format(n1=texto, n2=otromas, n3=numero))

print('* * * * * Forma moderna (versiones de Python 3.6 en adelante, se introducen las f-strings) * * * * *')

print(f'El número es {numero} y el texto es {texto} y tiene {otromas}')

'''
Al ser código Python lo que va entre llaves, podemos usar métodos con variables o incluso insertar nuestras
funciones.
'''
print(f'El número es {numero} y el texto es {texto.upper()} y tiene {otromas}')

def suma(a, b):
    return a + b

print(f'El número es {suma(numero, numero)} y el texto es {texto.upper()} y tiene {otromas}')


