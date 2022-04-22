import pprint

print('\n* * * * * Jugando con cadenas de texto para mejorar las salidas * * * * *\n')

pprint.pprint(dir(''))                                      # Listamos los métodos que puedo usar dentro de una cadena de texto

cadenaUno = 'en un lugar de la manchA'
print(cadenaUno.capitalize())                               # Capitaliza la primera letra y pone el resto en minúscula
print(cadenaUno.title())                                    # Capitaliza la primera letra de cada palabra y pone en minúscula las demás
print(cadenaUno.count('e'))                                 # Nos dice cuantas veces aparece una letra o palabra en una cadena
print(cadenaUno.lower())                                    # Convierte a minúsculas
print(cadenaUno.upper())                                    # Convierte a mayúsculas

print(cadenaUno.lower().count('a'))                         # Convertimos a minúsculas y luego contamos las 'a'
'''
Esta línea sería igual que:
otracadena = cadena.lower()
print(otracadena.count('a'))
'''

cadenaDos = 'De cuyo {nOmBrE} no quiero acordarme'
print(cadenaDos.format(nOmBrE = 'nombre'))                  # Para dar formato al texto

numero = '5'
print(numero.isdigit())                                     # Comprobamos si la cadena es un dígito

cadenaTres = 'a2'
print(cadenaTres.isalnum())                                 # Comprobamos si la cadena es alfanumérica

cadenaCuatro = '1'
print(cadenaCuatro.isalpha())                               # Comprobamos si es alfabético

cadenaCinco = '        El perro de San Roque no tiene ...        '
print(cadenaCinco.strip())                                  # Elimina los espacios en blanco antes y después
print(cadenaCinco.lstrip())                                 # Elimina los espacios a la izquierda
print(cadenaCinco.rstrip())                                 # Elimina los espacios a la derecha

print(cadenaUno.split(' '))                                 # Convierte una cadena a una lista por el punto de ruptura que le indiquemos, en este caso por el espacio
print(cadenaUno.split('de'))

print(cadenaUno.startswith('en'))                           # Comprueba si la cadena comienza por las letras que le indiquemos
print(cadenaDos.endswith('acordarme'))                      # Comprueba si la cadena termina por las letras que le indiquemos
print(cadenaUno.lower().endswith('mancha'))                 # Concatenamos métodos de cadenas
