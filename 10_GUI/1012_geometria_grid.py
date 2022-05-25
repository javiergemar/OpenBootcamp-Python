print('* * * * * GEOMETRÍA GRID DE TKINTER * * * * *')

import tkinter as tk
from tkinter import ttk         # Importamos la librería ttk (template toolkit) para que las
                                # aplicaciones de tkinter tengan un estilo parecido al sistema operativo.
window = tk.Tk()                                # Creamos la ventana
# window.geometry('350x100')    # Establecemos un tamaño fijo (ancho x alto), aunque no es necesario.
window.title('Encender sistema de misiles')     # Título de la ventana

'''
Tenemos 2 métodos para definir el diseño de una cuadrícula: columnconfigure (para definirla por columnas)
o rowconfigure (para definirla por filas).
'''

window.columnconfigure((0, 1), weight=1)        # Podemos definir varias columnas en una tupla de números de columna.
window.columnconfigure(2, weight=1)

'''
Definimos cada columna y el peso de cada una, una columna con valor 2 en weight tendrá el 
doble de ancho que otra con valor 1.

En este caso hemos definido una cuadrícula de tres columnas y estos serían los índices: 
(0,0) (1,0) 
(1,0) (1,1) 
(2,0) (1,2) (2,2)

Podemos definir columnas que no sean consecutivas, por lo que dejamos espacio por si 
queremos añadir otras columnas más adelante. En este caso las columnas 0 y 1 al tener
menos elementos que la columna 2, los objetos pueden tomar el espacio contiguo.
'''

username_label = ttk.Label(window, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

'''
Creamos un widget del tipo Label y le asignamos el nombre username_label. Dentro de los paréntesis
indicamos la ventana que lo ubicará y los parámetros adicionales.
Establecemos para el widget creado el posicionamiento grid y entre paréntesis añadimos
los parámetros, como la posición en la cuadrícula, alineación, espaciado,... 
El parámetro sticky indica que se pegue a una posición y le indicamos una coordenada al estilo 
de la rosa de los vientos (este = E, oeste = W, norte = N, sur = S,...).
Los parámetros padx y pady indican el espacio que dejamos de margen en el eje x e y entre los widgets.
Los parámetros ipadx e ipady indican el espacio dentro del widget.
'''

username_entry = ttk.Entry(window)              # Con esto creamos un inputbox, una especie de entrada de texto.
username_entry.grid(column=1, row=0, columnspan=2, sticky=tk.E, padx=5, pady=5)

password_label = ttk.Label(window, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

# El parámetro show='*' hace que al introducir una contraseña se muestren asteriscos
password_entry = ttk.Entry(window, show='*')
password_entry.grid(column=1, row=1, columnspan=2, sticky=tk.E, padx=5, pady=5)

aceptar_button = ttk.Button(window, text="Aceptar")
aceptar_button.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

cancelar_button = ttk.Button(window, text="Cancelar")
cancelar_button.grid(column=1, row=2, padx=5, pady=5)

borrar_button = ttk.Button(window, text="Borrar")
borrar_button.grid(column=2, row=2, sticky=tk.E, padx=5, pady=5)


window.mainloop()
'''
La función mainloop() se utiliza para ejecutar la aplicación, esperar a que ocurra un evento y
procesar el evento hasta que la ventana no se cierre.
'''
