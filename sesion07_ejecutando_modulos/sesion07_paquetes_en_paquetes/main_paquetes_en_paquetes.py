import operaciones.sumador.suma as s
import operaciones.restador.resta as r

import pprint
import math

def main():
    resta = r.resta(5, 3)
    suma = s.suma(4, 2)
    add = s.add(5, 4)
    minus = r.minus(8, 4)
    print(resta, suma, add, minus)
    print('Mostramos las funciones que tiene el módulo suma')
    pprint.pprint(dir(s))
    print('Mostramos las funciones que tenemos cargadas desde nuestros módulos')
    pprint.pprint(dir())

    misuma = s.Sumatorio()
    misuma.sumaEnClase(2, 2)
    print('Mostramos los comentarios de ayuda que incluimos en la función sumaEnClase')
    help(misuma.sumaEnClase)

    print('Mostramos los métodos que tiene un objeto')
    print(dir(misuma))

    print('Mostramos los métodos que tiene un string')
    print(dir('cadena'))
    print('Mostramos los métodos que tiene un integer')
    print(dir(1))
    print('Mostramos los métodos que tiene un float')
    print(dir(1.1))
    print('Mostramos los métodos que tiene una lista')
    print(dir([]))
    print('Mostramos los métodos que tiene una tupla')
    print(dir(()))
    print('Mostramos los métodos que tiene un diccionario')
    print(dir({}))
    print('Mostramos las funciones que tiene el módulo math de Python')
    print(dir(math))


if __name__ == '__main__':
    main()
