import operaciones.restador.resta
import operaciones.sumador.suma

def main():
    resta = operaciones.restador.resta.resta(5, 3)
    suma = operaciones.sumador.suma.suma(5, 3)
    print(resta)
    print(suma)

if __name__ == '__main__':
    main()

# TAMBIÉN SE PODRÍA HACER DE LA SIGUIENTE MANERA ASIGNANDO ALIAS

'''
import operaciones.restador.resta as orr
import operaciones.sumador.suma as oss

def main():
    resta = orr.resta(5, 3)
    suma = oss.suma(5, 3)
    print(resta)
    print(suma)

if __name__ == '__main__':
    main()
'''

# OTRA FORMA SERÍA IMPORTANDO LOS MÓDULOS DE LOS PAQUETES DE LA SIGUIENTE FORMA

'''
from operaciones import restador, sumador

def main():
    resta = restador.resta(5, 3)        # ahora para llamar a la función solo tenemos 
    suma = sumador.suma(5, 3)           # que poner el nombre del módulo antes de la función
    print(resta)
    print(suma)

if __name__ == '__main__':
    main()
'''
