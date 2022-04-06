import operaciones.suma             # Importamos el módulo suma dentro del paquete operaciones

def main():
    print(operaciones.suma.suma(2, 3))
    mp = operaciones.suma.Multiplicador()       # Creamos un objeto de la clase Multiplicador()
    print(mp.multiplica(5, 5))

if __name__ == '__main__':
    main()