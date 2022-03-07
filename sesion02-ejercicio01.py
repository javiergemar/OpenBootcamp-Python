# En este ejercicio tendrás que crear una variable a la cual asignarás
# una cadena de texto y la imprimirás por consola, a su vez, tendrás que
# imprimir también el tipo de la variable por consola.

texto = input('Inserta una cadena de caracteres: ')
print('La cadena de texto introducida es: ', texto)
tipoVariable = type(texto)
tipoVariable = str(tipoVariable)
print('El tipo de dato es ',  tipoVariable)