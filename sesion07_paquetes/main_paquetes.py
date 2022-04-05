import operaciones.suma             # Importamos el módulo suma dentro del paquete operaciones

def main():
    mp = operaciones.suma.Multiplicador()       # Creamos un objeto de la clase Multiplicador()
    print(mp.multiplica(5, 5))
