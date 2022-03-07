# Escribe un programa en la consola de python que pida al usuario
# su peso (en kg) y estatura (en metros), calcule el índice de masa
# corporal y lo almacene en una variable, e imprima por pantalla la
# frase Tu índice de masa corporal es <imc> donde <imc> es el índice
# de masa corporal calculado redondeado con dos decimales.

print('Bienvenido a la calculadora de IMC')
peso = int(input('¿Cuál es tu peso en Kg? '))
estatura = float(input('¿Cuál es tu estatura en metros?, introduzca los decimales separados por punto '))
imc = peso / (estatura * estatura)
print('Tu indice de masa corporal es ', round(imc, 2))