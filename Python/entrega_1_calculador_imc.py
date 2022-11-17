from cProfile import label
from distutils.cmd import Command
from distutils.log import error
from imaplib import Commands
from struct import pack
from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("calculador de imc")
ventana.geometry("400x300")

persona = {
    'mail': '',
    'nombre': '',
    'peso': 0,
    'altura':0,
    'indice': 0
}

def Imc ():
    p = entrada3.get()
    a = entrada4.get()
    peso = int(p)
    altura = float(a)
    persona["indice"] = peso/(altura**2)
    persona["indice"] = str(round (persona["indice"]))
    print (persona["indice"])

def deteccion_arroba ():
    if ("@" not in persona["mail"]): 
        label_error = ttk.Label(text="ingrese un mail valido", foreground="#FF0000")
        label_error.pack()
    else:
        label_imc = ttk.Label (text= "su imc es: "+persona["indice"])    
        label_imc.pack()



def junta():
    persona['mail'] = entrada1.get()
    persona['nombre'] = entrada2.get() 
    persona['peso'] = entrada3.get()
    persona['altura'] = entrada4.get()

    print(persona)
    Imc()
    deteccion_arroba()         

#input de datos
label1 = ttk.Label(ventana, text="Ingrese su Mail")
label1.pack()
entrada1 = ttk.Entry(ventana)
entrada1.pack()

label2 = ttk.Label(ventana, text="Ingrese su Nombre")
label2.pack()
entrada2 = ttk.Entry(ventana)
entrada2.pack()

label3 = ttk.Label(ventana, text="Ingrese su Peso")
label3.pack()
entrada3 = ttk.Entry(ventana)
entrada3.pack()

label4 = ttk.Label(ventana, text="Ingrese su Altura")
label4.pack()
entrada4 = ttk.Entry(ventana)
entrada4.pack()

#buttons
submit = ttk.Button(text="Siguiente", command=lambda: junta())
submit.pack()
quit = ttk.Button(ventana, command=ventana.destroy, text="Quit")
quit.pack()

ventana.mainloop()
