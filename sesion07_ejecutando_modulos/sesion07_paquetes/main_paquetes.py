def main():
    print(sesion07_ejecutando_modulos.sesion07_paquetes.operaciones.suma.suma(2, 3))
    mp = sesion07_ejecutando_modulos.sesion07_paquetes.operaciones.suma.Multiplicador()       # Creamos un objeto de la clase Multiplicador()
    print(mp.multiplica(5, 5))

if __name__ == '__main__':
    main()