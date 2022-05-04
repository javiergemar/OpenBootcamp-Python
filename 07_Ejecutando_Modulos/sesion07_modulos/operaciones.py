PI = 3.14151921             # Añadimos variables al inicio del módulo


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def como_me_llamo():        # Esta función nos devolverá el nombre del módulo
    return __name__         # con la variable __name__


class Operador:             # También podemos tener clases en los módulos
    def multiplicacion(self, a, b):
        return a * b


'''
IMPORTANTE
Debemos evitar el código que sigue a continuación, es decir,
el código de ámbito global fuera de las funciones. Esto es 
una mala práctica.
'''

print('Hola')
