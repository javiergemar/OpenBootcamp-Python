import sys
from tkinter import *

window = Tk()
window.title('Encender sistema de misiles')

window.columnconfigure((0, 1), weight=1)
window.columnconfigure(2, weight=1)

frame = Frame(window)               # Creamos un frame
print(type(frame))
print(dir(frame))                       # Vemos una lista de atributos y métodos del objeto
frame['relief']='sunken'

label_frame = Label(frame, text='Esto es un frame')
label_frame.grid(column=0, row=0, sticky=W, padx=50, pady=50)

frame.grid(column=0, row=0, sticky=W)

lista = ['Windows', 'macOS', 'Linux', 'MS DOS', 'AmigaOS', 'BeOS', 'OS/2']
listbox = Listbox(window, listvariable=lista)
listbox.grid(column=0, row=0, sticky=W)

window.mainloop()
sys.exit(0)                             # Finalizamos el script

username_label = Label(window, text="Username:")
username_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)

username_entry = Entry(window)              # Con esto creamos un inputbox, una especie de entrada de texto.
username_entry.grid(column=1, row=0, columnspan=2, sticky=E, padx=5, pady=5)

password_label = Label(window, text="Password:")
password_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)

# El parámetro show='*' hace que al introducir una contraseña se muestren asteriscos
password_entry = Entry(window, show='*')
password_entry.grid(column=1, row=1, columnspan=2, sticky=E, padx=5, pady=5)

aceptar_button = Button(window, text="Aceptar")
aceptar_button.grid(column=0, row=2, sticky=W, padx=5, pady=5)

cancelar_button = Button(window, text="Cancelar")
cancelar_button.grid(column=1, row=2, padx=5, pady=5)

borrar_button = Button(window, text="Borrar")
borrar_button.grid(column=2, row=2, sticky=E, padx=5, pady=5)
