# Modifica la variable del anterior ejercicio en la consola de python
# y después muestrala por consola para ver la modificación de la variable.

texto = input('Inserta una cadena de texto: ')
print('La cadena de texto introducida es: ', texto)
texto = input('Teclea una nueva cadena de texto: ')
print('La cadena almacenada ha cambiado, ahora es: ', texto)
tipoVariable = type(texto)
tipoVariable = str(tipoVariable)
print('El tipo de dato es ' + tipoVariable)

