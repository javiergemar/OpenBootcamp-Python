# Escribe un programa que pregunte al usuario su edad
# y muestre por pantalla si es mayor de edad o no.

edad = int(input('¿Qué edad tienes? '))

if edad >= 18:
    print('Con', edad, 'años eres mayor de edad')
else:
    print('Con', edad, 'años eres menor de edad')