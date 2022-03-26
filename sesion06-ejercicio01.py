'''
Crear una clase Vehículo con los siguientes atributos:
- Color
- Ruedas
- Puertas

Crear una clase Coche la cual heredaŕa de Vehículo con
los siguientes atributos:
- Velocidad
- Cilindrada

Crear un objeto de la clase Coche y mostrarlo por consola.
'''


class Vehiculo:
    color = ''
    ruedas = 0
    puertas = 0


class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0


c = Coche()
print(c.velocidad)
print(c.puertas)
type(c)