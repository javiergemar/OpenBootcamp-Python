print('* * * * * Ficheros de registro * * * * *')

import logging

'''
La librería logging lo que hace es mostrar información y está sometido a niveles. Los niveles
por defecto son: info, warning, error, critical y debug. 

Cuando llamamos a logging.info() por defecto no se muestra nada, tenemos que llamar a alguno de
los niveles para que se muestre algo.

Si queremos que se muestren todos los mensajes logging desde info (a más críticos) tenemos que configurar
lo que se llama "severitis" y configuramos el logger para mostrar mensajes según nos interesa.

'''

logging.basicConfig(level=logging.INFO)         # Esto mostraría todos los mensajes logging de info o
                                                # más severos

'''
logging.basicConfig(level=logging.ERROR)        # Esto mostraría todos los mensajes logging de error o
                                                # más severos
                                                
logging.basicConfig(level=logging.DEBUG)        # Mostraría todos los mensajes, es el más chivato                                                
'''

logging.debug('El más chivato')
logging.info('Mensaje info')
logging.warning('Mensaje warning')
logging.error('Mensaje error')
logging.critical('Mensaje critical')
