import pprint

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

print('Muestra la tabla de símbolos a nivel global')
pprint.pprint(globals())

def prueba(a, b):
    valor = 5
    estado = False
    print('Muestra la tabla de símbolos de mi función actual')
    pprint.pprint(locals())

    def dentroDePrueba(x):
        variable = True
        print('Dentro dentroDePrueba')
        pprint.pprint(locals())

    dentroDePrueba(1)
    print('Dentro de prueba')
    pprint.pprint(locals())

prueba(5, 6)