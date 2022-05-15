print('* * * * * Programación multihilo * * * * *')

import _thread
import time

def horaActual(nombre_thread, tiempo_de_espera):
    count = 0

    while count < 5:
        time.sleep(tiempo_de_espera)
        count += 1
        print(f'hilo: {nombre_thread} - {time.ctime(time.time())}')

_thread.start_new_thread(horaActual, ('thread_uno', 1))
_thread.start_new_thread(horaActual, ('thread_dos', 2))

'''
Cuando se ejecuta código multihilo tenemos que darle tiempo al programa para que se ejecute,
es decir, tenemos que bloquear al programa para que se ejecute nuestro código paralelo.
'''

print('He disparado ya los hilos')

while True:             # Podríamos hacerlo con un bucle
    pass

'''
while True:
    time.sleep(0.1)     # Otra forma de hacerlo que carga menos el procesador.
'''
