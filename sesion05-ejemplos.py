texto = 'El resultado de la '                           # variable de ámbito global
textoAlternativo = 'La operación da como resultado: '

def matematicas(a = 8, b = 4, c = 2, d = 1):            # le indicamos que los parámetros sean opcionales
    def suma(a, b, c, d):
        return a + b + c +d
    def resta(a, b, c, d):
        return a - b -c -d
    texto = 'Resultado de'              # la variable local prevalece sobre la variable global
    global textoAlternativo             # la variable de ámbito global sobrescribe la de ámbito local
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

def habitantes(*args):
    totalHabitantes = 0

    for arg in args:
        totalHabitantes += arg

    return totalHabitantes

print(habitantes(1, 3, 5, 7, 9))

def diccionario(**kwargs):
        for key, value in kwargs.items():
            print(key, '=', value)

diccionario(coche = 'car', gato = 'cat', perro = 'dog', casa = 'home', rana = 'fog', avion = 'plane')
