texto = 'El resultado de la '           # variable de ámbito global

def matematicas(a, b):
    def suma(a, b):
        return a + b
    def resta(a, b):
        return a -b
    texto = 'Resultado de'              # la variable local prevalece sobre la variable global
    resultadoSuma = suma (a, b)
    print(texto, 'suma es: ', resultadoSuma)

    resultadoResta = resta(a, b)
    print(texto, 'resta es: ', resultadoResta)

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


matematicas(4, 2)


'''
def matematicas(a, b):
    def suma(a, b):
        print(a + b)

    def resta(a, b):
        print(a - b)

    def masoperaciones(a, b):
        def multiplica(a, b):
            print(a * b)

        multiplica(a, b)

    suma(a, b)
    resta(a, b)
    masoperaciones(a, b)

matematicas(5, 3)
'''