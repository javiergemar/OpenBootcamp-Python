print('* * * * * Serializar datos * * * * *\n')

import pickle                           # Esta librería nos va a permitir serializar y deserializar

class Juguete:
    nombre =''
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre

j1 = Juguete('Potato', 10.5)
print(type(j1))
print(j1.getNombre())

f = open('datos.bin', 'wb')             # Creamos el fichero 'datos.bin' con los permisos 'wb' para escribir en binario
pickle.dump(j1, f)                      # Serializamos los datos del objeto 'j1' en la variable 'f'
f.close()

f = open('datos.bin', 'rb')             # Abrimos el fichero y leemos un binario (permiso rb)
potato = pickle.load(f)                 # Deserializamos los datos al objeto 'potato'
f.close()

print(type(potato))
print(potato.getNombre(), 'precio: ', potato.precio)

'''
El módulo pickle nos va a permitir serializar y deserializar un objeto (en este caso 'j1') a datos
binarios y luego deserializarlos para recuperar la información. La función dump('nombreArchivo', 'permisos') 
serializa los datos y la función load('nombreArchivo', 'permisos') deserializa.
'''