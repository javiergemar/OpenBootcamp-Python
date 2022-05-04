'''
Si queremos guardar mensajes en un fichero o leerlos desde un fichero tenemos el conjunto de funciones de manipulación de ficheros.
'''

print('\n* * * * * Abrir ficheros y leer el contenido completo (o un número de bites) * * * * *\n')

f = open('/etc/passwd', 'r')            # Abrimos el fichero
datos = f.read()                        # Declaramos la variable datos y le asignamos el contenido completo del fichero
print(datos)
f.close()                               # Cerramos el fichero

'''
Abrimos un fichero con la función open() y lo asignamos a la variable f. Como la función open() devuelve
una clase, la variable f será una instancia de una clase (un objeto). Dentro de la función open() indicamos
la ruta del fichero y el permiso.

Aplicamos la función read() al objeto f y almacenamos el contenido en la variable datos.
 
Tenemos que dejar el fichero cerrado con la función close().

Significado de los permisos:
r: lectura
a: append (añadimos datos a un fichero existente)
w: escritura (machacamos el fichero y escribimos los datos desde cero)
x: create (creamos el fichero en caso de no existir, aunque esto es automático en Python)
t: texto (para texto plano)
b: binary (para texto binario)
+ (es un potenciador, por ejemplo, si ponemos w+ es escritura con lectura)
'''

print('\n* * * * * Abrir ficheros y leer un número determinado de bites * * * * *\n')

f = open('/etc/passwd', 'r')            # Abrimos el fichero
numeroDeBites = f.read(79)              # Solo leemos los 79 primeros bites
print(numeroDeBites)
f.close()                               # Cerramos el fichero

'''
Podemos indicar el número de bites que queremos leer, en este caso 79 para coger las dos primeras líneas.
En las dos primeras líneas hay 78 caracteres, pero está el carácter oculto \n que es el salto de línea que
cuenta como un carácter más. 
'''

print('\n* * * * * Abrir ficheros y leer la primera línea * * * * *\n')

f = open('/etc/passwd', 'r')
primeraLinea = f.readline()        # Solo leeríamos la primera línea del fichero
print(primeraLinea)
f.close()

print ('\n* * * * * Leyendo línea a línea * * * * *\n')

f = open('/etc/passwd', 'r')

primeraLinea = f.readline()
print(primeraLinea)
primeraLinea = f.readline()
print(primeraLinea)

f.close()

'''
Cada vez que lee una línea se posiciona al principio de la siguiente línea.
'''

print ('\n* * * * * Creamos una función para leer línea a línea un fichero * * * * *\n')

f = open('/etc/passwd', 'r')

datosFichero = None
while datosFichero != '':
    datosFichero = f.readline()
    print(datosFichero)

f.close()

print('\n* * * * * Otra forma de hacer que lea línea a línea * * * * *\n')

f = open('/etc/passwd', 'r')

datosOtraForma = 'vacio'
while len(datosOtraForma) > 0:
    datosOtraForma = f.readline()
    print(datosOtraForma)

f.close()

print('\n* * * * * Leer todo un fichero y meterlo en una lista * * * * *\n')

f = open('/etc/passwd', 'r')

datosLista = f.readlines()
f.close()

print(datosLista)

'''
Ahora si que podemos ver en la lista al final de cada elemento el \n.
'''

print('\n* * * * * Listar ciertos datos de un archivo * * * * *\n')

def main():
    usuariosLinux = listamosUsuarios()
    for usuario in usuariosLinux:
        print(f'Usuario: {usuario}')

def listamosUsuarios():
    fichero = open('/etc/passwd', 'r')
    lineasFichero = fichero.readlines()         # Leemos el fichero en formato lista
    fichero.close()

    resultado = []                              # Creamos una lista vacía para almacenar la salida final
    for linea in lineasFichero:                 # Iteramos sobre el fichero
        if linea[0] == '_':                     # Si la línea empieza con el carácter _
            continue                            # forzamos que salte a la siguiente línea

        if linea[0] == 'j':                     # Igual que el anterior pero si la línea empieza por j
            continue

#       if linea[0] == '_' or linea[0] == 'j':  # También se podría haber hecho así
#           continue

        partes = linea.split(':')               # Rompemos cada línea por el carácter que indicamos
#       print(linea)                            # Muestra línea a línea
#       print(partes)                           # Muestra cada línea como una lista
#       print(partes[0])                        # De cada lista muestra el primer elemento (o el elemento 0)
        resultado.append(partes[0])             # Añade el elemento 0 de cada línea a la lista resultado

    return resultado                            # Devuelve resultado

if __name__ == '__main__':
    main()

'''
Hemos listado las líneas de un archivo quitando las líneas que empiezan con el guión bajo '_' y 'j'.
Además como cada línea es un string, con el método split() cada línea la hemos convertido en lista 
separando los elementos por el carácter ':'

Como habíamos declarado resultado como una lista vacía, con la función append() le hemos ido añadiendo
cada primer elemento (es decir, la posición 0) de la lista partes.

Y return nos devolverá los datos almacenados en la lista resultado. 
'''

print('\n* * * * * Escribir ficheros * * * * *\n')

f = open('mensajesEnFichero.txt', 'w')                  # El permiso 'w' sobrescribe lo que haya escrito
f.write('datos1\n')
f.write('datos2\n')
f.close()

f = open('mensajesEnFichero.txt', 'a')                  # El permiso 'a' añade a lo que haya escrito
f.write('datos1\n')
f.write('datos2\n')
f.close()

f = open('mensajesEnFichero.txt', 'w')
lista = [
    'una liena\n',
    'dos lineas\n',
    'tres lineas\n'
]
f.writelines(lista)                             # Con el método writelines() tenemos que pasar una lista
f.close()

print('\n* * * * * Creamos una función que al pasarle una lista machaque y escriba un fichero * * * * *\n')

lista = [                                       # Definimos la lista
    'una linea',
    'dos lineas',
    'tres lineas'
]

def escribe(fichero, datos):                    # La función requiere dos parámetros, nombre fichero y lista
    f = open(fichero, 'w')

    for linea in datos:                         # Por cada línea de la lista
        if not linea.endswith('\n'):            # Si no termina con \n
            linea += '\n'                       # linea es igual a linea más un salto de línea
        f.write(linea)                          # Escribimos el valor de linea en el fichero

    f.close()

escribe('mensajesEnFichero2.txt', lista)                # Invocamos a la función con sus dos parámetros
