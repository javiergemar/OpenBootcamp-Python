from abc import ABC, abstractmethod


class recabarDatos(ABC):
    @abstractmethod
    def diccionario(self, **kwargs):
        pass


class consultaDatos(ABC):
    pass




'''
diccionario = {
    'Francisco': 8,
    'Miguel': 7,
    'Antonio': 6,
    'Alvaro': 5,
    'Jesús': 8
}

numeroUsuario = len(diccionario)
print(numeroUsuario)

class Alumno:
    nombre = ''
    nota = 0

    print('Elige un alumno de la lista para saber su nota:')

    for x in diccionario:
        print(x)

    # input('Introduce un nombre de la lista :')

    def funcion(self):
        pass

a = Alumno()
'''