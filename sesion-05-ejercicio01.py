'''
Escribe una función que calcule el área de un triángulo, recibiendo
la altura y la base como parámetros y otra función que calcule el
área de un círculo recibiendo el radio del mismo.
'''

import math

def calculaAreaTriangulo(baseTriangulo, alturaTriangulo):
    areaTriangulo = (baseTriangulo * alturaTriangulo) / 2
    return areaTriangulo

def calculaAreaCirculo(radio):
    areaCirculo = (radio * math.pi)**2
    return areaCirculo

print('* * * * * VAMOS A CALCULAR EL ÁREA DE UN TRIÁNGULO * * * * *')

baseTriangulo = float(input('Introduce la base del triángulo: '))
alturaTriangulo = float(input('Introduce la altura del triángulo: '))
print('El área de tu triángulo es:', calculaAreaTriangulo(baseTriangulo, alturaTriangulo))

print('* * * * * VAMOS A CALCULAR EL ÁREA DE UN CÍRCULO * * * * *')

radio = float(input('Introduce área del círculo: '))
print('El área del círculo es:', calculaAreaCirculo(radio))