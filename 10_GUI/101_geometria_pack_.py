print('* * * * * Ejemplo de posicionamiento (o geometría) pack * * * * *\n')
# La librería Tkinter lo que hace es generar Tcl y ejecutarlo.
import tkinter

# Vamos a crear una ventana y para ello creamos una instancia de la clase Tk.
window = tkinter.Tk()

import pprint
print(type(window))
pprint.pprint(dir(window))

'''
Introducimos la geometría antes del mainloop() y creamos una serie de widget llamados "labelx" que crea una etiqueta. 
Indicamos entre paréntesis la ventana dónde queremos situar la etiqueta y a continuación un texto descriptivo.
También podemos indicar otra serie de parámetros. 
'''

label1 = tkinter.Label(window, text='label1', bg='yellow', fg='black')

'''
Posicionamos con la geometría pack (que agolpa unas cosas con otras) el widget en la ventana. Y entre paréntesis
introducimos las propiedades. 
Los parámetros ipadx e ipady establecen el padding que se cuenta desde donde empieza el widget hasta los extremos.
El parámetro fill rellena la ventana cuando la estiramos hasta los bordes, admite tres parámetros (x, y, both).
expand añade más espacio a un objeto.
'''

label1.pack(ipadx=45, ipady=15, fill='x')

label2 = tkinter.Label(window, text='label2', bg='red', fg='white')
label2.pack(ipadx=45, ipady=15, fill='x')

label3 = tkinter.Label(window, text='label3', bg='green', fg='white')
label3.pack(ipadx=45, ipady=15, fill='x')

label4 = tkinter.Label(window, text='label4', bg='blue', fg='white')
label4.pack(ipadx=15, ipady=15, side='left', expand=True)

label5 = tkinter.Label(window, text='label5', bg='purple', fg='white')
label5.pack(ipadx=15, ipady=15, side='bottom')

label6 = tkinter.Label(window, text='label6', bg='pink', fg='white')
label6.pack(ipadx=15, ipady=15, side='right', fill='both')

# El método mainloop() muestra en pantalla y responde a la entrada del usuario hasta que el programa termina.
window.mainloop()