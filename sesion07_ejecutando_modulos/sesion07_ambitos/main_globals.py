import pprint


def test():
    print('Hola')


pprint.pprint(globals())
test()


variable = 5
print(variable)

def prueba():
    globals()['variable'] = 6

    '''
    Sería lo mismo que hacer:
    global variable
    variable = 6
    '''

prueba()
print(variable)

class Hola:
    def patata(self):
        print('clase Hola')

h = Hola()
globals()['h'].patata()         # Llamamos a la función patata() con globals()

class Adios:
    def sandia():
        print('clase Adios')

globals()['Adios'].sandia()     # Llamamos  a la función sandia() con globals()