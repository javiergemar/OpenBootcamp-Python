print('* * * * * SESIÓN 5 * * * * *')
print('* * * * * CÓMO DECLARAR FUNCIONES * * * * *')

texto = 'El resultado de la '                           # variable de ámbito global
textoAlternativo = 'La operación da como resultado: '


def matematicas(a = 8, b = 4, c = 2, d = 1):            # le indicamos que los parámetros sean opcionales
    def suma(a, b, c, d):
        return a + b + c +d

    def resta(a, b, c, d):
        return a - b -c -d
    texto = 'Resultado de'              # la variable LOCAL prevalece sobre la variable GLOBAL
    global textoAlternativo             # la variable de ÁMBITO GLOBAL sobrescribe la de ÁMBITO LOCAL
    resultadoSuma = suma (a, b, c, d)
    print(texto, 'suma es: ', resultadoSuma)
    print(textoAlternativo, resultadoSuma)

    resultadoResta = resta(a, b, c, d)
    print(texto, 'resta es: ', resultadoResta)
    print(textoAlternativo, resultadoResta)

    def masoperaciones(a, b):

        def multi(a, b):
            return a * b

        def divi(a, b):
            return a / b

        resultadoMultiplicacion = multi(a, b)
        print(texto, 'multiplicación es: ', resultadoMultiplicacion)

        resultadoDivision = divi(a, b)
        print(texto, 'división es: ', resultadoDivision)

    masoperaciones(a, b)


matematicas()

print('* * * * * USO DE ARGS * * * * *')


def habitantes(*args):
    totalHabitantes = 0

    for arg in args:
        totalHabitantes += arg

    return totalHabitantes


print(habitantes(1, 3, 5, 7, 9))

print('* * * * * USO DE KWARGS * * * * *')


def diccionario(**kwargs):
        for key, value in kwargs.items():
            print(key, '=', value)


diccionario(coche = 'car', gato = 'cat', perro = 'dog', casa = 'home', rana = 'fog', avion = 'plane')

print('Diferentes formas de las que podemos acceder al resultado de la función')


def operaciones(a, b):
    return a + b, a - b, a * b, a / b


resultados = operaciones(2, 4)
print(resultados)
print(resultados[0])
print(resultados[1])
print(resultados[2])
print(resultados[3])

suma, resta, multi, divi = operaciones(4, 8)
print(suma)
print(resta)
print(multi)
print(divi)

opera, _, _, _ = operaciones(8, 16)
print(opera)

print('* * * * * OPERADORES TERNARIOS * * * * *')


def sumador(**kwargs):
    primerNumero = kwargs['claveInicial'] if 'claveInicial' in kwargs else 0
    ultimoNumero = kwargs['claveFinal'] if 'claveFinal' in kwargs else primerNumero

    resultado = 0
    for x in range(primerNumero, ultimoNumero +1):
        resultado += x

    return resultado


print('El resultado de sumar los valores es :', sumador(claveFinal=50))


print('* * * * * FUNCIONES LAMBDA (o anónimas) * * * * *')

anonima = lambda: print('hola')
anonima()

anonima = lambda parametro: print('hola', parametro)
anonima('Javier')

anonima = lambda parametro1, parametro2: print('hola', parametro1, 'adios', parametro2)
anonima('Javier', 'Javi')

funcionSuma = lambda parametro: parametro + parametro
print(funcionSuma(5))


def funcionSuma(parametro):
    return parametro + parametro


print(funcionSuma(5))
