print('* * * * * CLASES Y MÉTODOS ABSTRACTOS * * * * *')

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sonido(self):   # Como el sonido de cada animal es diferente,
        pass            # dejamos el método como abstracto para
                        # cuando lo hereden implementen el código
    def diHola(self):
        print('Hola')

        
class Perro(Animal):
    def sonido(self):   # Definimos el código para el método sonido()
        print('Guau')   # de la clase Perro() derivada de Animal()


class Gato(Animal):
    def sonido(self):   # Definimos el código para el método sonido()
        print('Miau')   # de la clase Gato() derivada de Animal()


p = Perro()
p.sonido()
p.diHola()


g = Gato()
g.sonido()
g.diHola()


print('* * * * * COMPOSICIÓN * * * * *')


class Motor:
    tipo = 'Diesel'


class Ventanas:
    cantidad = 5

    def cambiarCantidad(self, valor):
        self.cantidad = valor


class Ruedas:
    cantidad = 4


class Carroceria:           # Clase compuesta por Ventanas() y Ruedas()
    ventanas = Ventanas()
    ruedas = Ruedas()


class Coche:                # Clase compuesta por Motor() y Carroceria()
    motor = Motor()
    carroceria = Carroceria()


c = Coche()                 # Instanciamos la clase Coche()

print('Motor es', c.motor.tipo)
print('Ventanas', c.carroceria.ventanas.cantidad)
c.carroceria.ventanas.cambiarCantidad(3)    # El parámetro de la función cambiarCantidad() cambia
print(c.carroceria.ventanas.cantidad)       # el valor de la variable cantidad de la clase Ventanas


print('* * * * * EJERCICIO DE COMPOSICIÓN * * * * *')


class Categorias:
    idcategoria = 0
    nombre = ''


class Proveedores:
    idproveedor = 0
    nombre = 0


class Productos:
    idproducto = 0
    CategoriaProducto = Categorias()
    Precio = 0
    Tamano = 0
    TipoDeProducto = 0
    CIFProveedor = Proveedores()

    
p = Productos()
p.CIFProveedor.nombre                       # Accedemos a nombre de Proveedores()
p.CategoriaProducto.idcategoria             # Accedemos a idcategoría de Categorias()
