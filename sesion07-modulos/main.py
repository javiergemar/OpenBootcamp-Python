'''
Podemos importar módulos que no hemos creado nosotros y que son parte de Python.
Importamos math que es un módulo de Python.
'''

# import operaciones                        Así importamos el módulo operaciones sin alias
import operaciones as o                     # Importamos el módulo operaciones
import math                                 # Importamos el módulo de matemáticas math
import sys                                  # Importamos el módulo sys para modificar la variable path
import pprint                               # Importamos el módulo pprint para imprimir de forma bonita


def main():
    #   sum = operaciones.sum(2, 2)         Llamada a las funciones sin asignar alias al módulo
    #   res = operaciones.res(6, 1)

    sum = o.suma(2, 2)                      # Invocamos al módulo y luego a la función
    res = o.resta(6, 1)

    pprint.pprint(sys.path)
    '''
    Añadimos a sys.path la ruta de nuestros módulos antes de cargr el módulo que se encuentra
    en otra ruta
    '''
    sys.path.append('/home/javier/OpenBootcamp/OpenBootcamp-MisModulos')
    pprint.pprint(sys.path)

    print('Hola en main(),', 'Variable sum:', sum, 'Variable res:', res)

    print('El módulo se llama:', o.como_me_llamo())     # Llamamos a la variable __name__

    op = o.Operador()
    print('Resultado del método multiplicacion():', op.multiplicacion(3, 5))

    print('La variable PI vale:', o.PI)


if __name__ == '__main__':
    main()
