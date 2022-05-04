print('* * * * * Representaciones textuales de cadenas * * * * *\n')
num = 511
print(type(num))

numtxt = str(num)                               # Convertimos num a cadena con str()
print(type(numtxt))

print(repr(num))
print(numtxt)

print('\n* * * * * Sobrecarga de __str__() * * * * *\n')

class Juguete:
    nombre = ''
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'Mi nombre es {self.nombre} y mi precio es {self.precio}'

j1 = Juguete('Potato', 10.5)
print('print(j1):', j1)                         # Por debajo Python hace un print(str(j1))
print('print(repr(j1)):', repr(j1))             # repr() lo usaremos para salidas técnicas o de depuración
print('\n')
demo = j1                                       # Asignamos a la variable demo el objeto j1
print('print(demo):', demo)
print('print(type(demo)):', type(demo))
print('\n')
demoStr = str(j1)                               # De esta forma solo asignamos a la variable demoStr la representación de j1
print('print(demoStr):', demoStr)
print('print(type(demoStr)):', type(demoStr))

print('\n* * * * * Sobrecarga de __repr__() * * * * *\n')

class Juguete2:
    nombre = ''
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'Mi nombre es {self.nombre} y mi precio es {self.precio}'

    def __repr__(self):
        return f'Potato({self.nombre}, {self.precio})'

j2 = Juguete2('Potato', 10.5)
print('print(j2):', j2)
print('print(str(j2)):', str(j2))
print('print(repr(j2)):', repr(j2))

print('\n* * * * * No tiene __str__() pero tiene __repr__() * * * * *\n')

class Juguete3:
    nombre = ''
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f'Potato({self.nombre}, {self.precio})'

j3 = Juguete3('Potato', 10.5)
print('print(j3):', (j3))
print('print(str(j3)):', str(j3))
print('print(repr(j3)):', repr(j3))

print('\n* * * * * No tiene __repr__() pero tiene __str__() * * * * *\n')

class Juguete4:
    nombre = ''
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'Mi nombre es {self.nombre} y mi precio es {self.precio}'

j4 = Juguete4('Potato', 10.5)
print('print(j4):', (j4))
print('print(str(j4)):', str(j4))
print('print(repr(j4)):', repr(j4))

representacionTextual = j4                                  # Asignamos a representacionTextual el objeto j4
print('representacionTextual:', representacionTextual)
print('type(representacionTextual):', type(representacionTextual))
representacionTextual = str(j4)                             # Asignamos a representacionTextual la representación textual del objeto
print('representacionTextual:', representacionTextual)
print('type(representacionTextual):', type(representacionTextual))
