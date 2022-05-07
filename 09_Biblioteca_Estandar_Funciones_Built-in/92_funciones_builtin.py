print('\n* * * * * Funciones built-in, ejemplo de filter() * * * * *\n')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mifuncion(x):
    if x % 2 == 0:                      # Vamos a sacar los números pares y eliminar los impares
        return True

    return False

'''
A la función mifuncion() se le irá pasando cada elemento de la lista y tiene que devolver
True o False. En caso de que devuelva True la función filter() mantiene el número, pero si
es False, elimina el número de la lista.
'''

resultadoPares = filter(mifuncion, numeros)
print(list(resultadoPares))

'''
La función que le pasamos a filter() tenemos que crearla previamente o creamos una lambda,
y debe devolver True o False.
'''

resultadoImpares = filter(lambda x: x % 2, numeros)
print(list(resultadoImpares))

'''
Podríamos hacerlo con una lambda, en este caso para sacar los impares.
'''

def mifuncion(x):
    if str(x).startswith('pep'):                # También funciona omitiendo str()
        return True

    return False

resultadoNombres = filter(mifuncion, ['pepe', 'pepito', 'juan'])
print(list(resultadoNombres))

resultadoNombre = filter(lambda x: x.startswith('ju'), ['pepe', 'pepito', 'juan'])
print(list(resultadoNombre))

print('\n* * * * * Funciones built-in, ejemplo de map() * * * * *\n')

def cuadrado(x):
    return x * x

resultadoMultiplica = map(cuadrado, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(resultadoMultiplica))

'''
La función map() requiere una función y una lista, y aplica la función sobre cada elemento
de la lista. 
'''

resultadoMultiplicacion = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(resultadoMultiplicacion))

# También podemos hacerlo con una función lambda.

print('\n* * * * * Funciones built-in, ejemplo de reduce() * * * * *\n')

from functools import reduce

'''
La función reduce() ejecuta de forma recursiva una función sobre una lista hasta que la lista se
quede con un único elemento.
'''

def suma(a, b):
    print(f'a={a}, b={b}')
    return a + b

resulSuma = reduce(suma, [1, 2, 3, 4, 5])
print(resulSuma)

resulSumaLambda = reduce(lambda a, b: a + b, [6, 7, 8, 9, 10])
print(resulSumaLambda)

print('\n* * * * * Funciones built-in, ejemplo de zip() * * * * *\n')

'''
La función zip() agrega iterables en una tupla y los devuelve. Es decir, devuelve una lista con tuplas
correspondientes cada una a un elemento de cada lista.
En el caso de tener más elementos en una lista que en otra, solo devuelve los elementos que tengan su 
correspondiente en la otra lista.
'''

cursos = ['Java', 'Python', 'Git', 'Linux']
asistentes = [15, 20, 4]

demo = zip(cursos, asistentes)
print(list(demo))

print('\n* * * * * Funciones built-in, ejemplo de all() y any() * * * * *\n')

'''
Las funciones all() y any() sirven para verificar que todas las condiciones de una lista se cumplan o para
verificar que alguna de las condiciones de la lista se cumplan.
'''

listaA = [1 == 1, 2 == 2, 3 == 4]
resA = any(listaA)
print(resA)

''' 
La función any() atraviesa una lista y si encuentra una condición que se cumple entonces devuelve True.  
'''

listaB = [1 == 1, 2 == 2, 3 == 4]
resB = all(listaB)
print(resB)

''' 
La función all() atraviesa la lista y si todas las condiciones se cumplen devuelve True.  
'''

print('\n* * * * * Funciones built-in, ejemplo de round() * * * * *\n')

'''
La función round() redondea al número más cercano, teniendo en cuenta que a partir de 0.5 redondea a 1.
'''

a = 5.5
b = 5.4
c = 5.6

print(round(a))
print(round(b))
print(round(c))

print('\n* * * * * Funciones built-in, ejemplo de min() * * * * *\n')

'''
La función min() devuelve el número mínimo de un número de parámetros de entrada.
'''

print(min(2, 3, 4, 5, 9, 3, 1))

print('\n* * * * * Funciones built-in, ejemplo de pow() * * * * *\n')

'''
La función pow() sirve para elevar un número.
'''

print(pow(2, 4))                        # Esto sería lo mismo que print(2**4)

print('\n* * * * * Funciones built-in, ejemplo de sorted() * * * * *\n')

'''
La función sorted() ordena una lista de elementos.
'''

listaLetras = ['z', 'c', 'd', 'a']
letrasOrdenada = sorted(listaLetras)
print(letrasOrdenada)

letrasOrdenadaRever = sorted(listaLetras, reverse=True)     # Aquí indicamos que la ordene al revés.
print(letrasOrdenadaRever)

letrasOrdenadaReverKey = sorted(listaLetras, reverse=True, key=lambda x: str(x).startswith('a'))
print(letrasOrdenadaReverKey)

'''
Podemos añadir una key con una función lambda y añadir ciertos parámetros. En este caso los elementos
que empiecen con 'a' se sitúan al principio.
'''

listaNombres = ['Javier', 'Manuel', 'Lucia']
nombresOrdenados = sorted(listaNombres)
print(nombresOrdenados)

listaNumeros = [3, 6, 9, 8, 6, 4, 1]
numerosOrdenador = sorted(listaNumeros)
print(listaNumeros)

print('\n* * * * * Funciones built-in, ejemplo de input() * * * * *\n')

'''
La función input() nos permite preguntar al usuario por datos. Cuando solicitamos un número por consola
nos dará un string y si necesitamos un integer tenemos que convertirlo con la función int().
'''

from getpass import getpass

user = input('username: ')
passwd = getpass('password: ')      # La función getpass() permite solicitar la contraseña y que no se muestre en pantalla

print(user, passwd)

'''
Al ejecutarlo en PyCharm saltará una alarma, pero si se ejecuta por consola se ejecuta bien.
'''

secreto = 50

valor = 0
while valor != secreto:
    valor = int(input('Introduce un número: '))     # También podríamos hacer valor = int(valor)

    if valor > secreto:
        print('Muy alto')
        continue

    if valor < secreto:
        print('Muy bajo')
        continue

print('Acertaste!!!')
