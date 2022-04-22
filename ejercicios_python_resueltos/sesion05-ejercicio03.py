'''
Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
'''

def leapYear(year):
    resto = year % 4
    return resto

year = int(input('Introduce un año para comprobar si es bisiesto: '))

devolucionFuncion = leapYear(year)

if devolucionFuncion == 0:
    print('Es un año bisiesto')
else:
    print('Este año no es bisiesto')