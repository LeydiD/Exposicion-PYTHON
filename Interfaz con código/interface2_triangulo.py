from Triangulo import Triangulo
from tkinter import *
from tkinter import messagebox

def calcular():
    tipo= Triangulo(lado1.get(), lado2.get(), lado3.get()).get_Tipo()
    rta= "El triángulo es : "+ tipo
    messagebox.showinfo(message=rta)

def ayudar():
    rta= "Ingrese los datos para determinar el tipo de triángulo"
    messagebox.showinfo(message=rta)

ventana= Tk()
ventana.title("Determina el Tipo de triángulo")
ventana.geometry("300x200")
ventana.resizable(False, False)
ventana.configure(background="#B3B3EE")

lblLado1= Label(ventana,text ="Ingrese el lado 1 : ")
lblLado1.grid(row=0, column=0)
lblLado1.config(padx=20, pady=15)
lblLado1.config(background="#B3B3EE")
lado1= IntVar()
txtLado1= Entry(textvariable=lado1).grid(row=0, column=1)

lblLado2 = Label(ventana, text ="Ingrese el lado 2 : ")
lblLado2.grid(row=1, column=0)
lblLado2.config(padx=20, pady=15)
lblLado2.config(background="#B3B3EE")
lado2= IntVar()
txtLado2= Entry(textvariable=lado2).grid(row=1, column=1)

lblLado3 = Label(text ="Ingrese el lado 3 : ")
lblLado3.grid(row=2, column=0)
lblLado3.config(padx=20, pady=15)
lblLado3.config(background="#B3B3EE")
lado3= IntVar()
txtLado3= Entry(ventana, textvariable=lado3).grid(row=2, column=1)

btnCalcular = Button(text = "Determinar Tipo De Triángulo", command= calcular).place(x= 20, y= 160)

btnAyuda= Button(text="Ayuda", command= ayudar).place(x=210, y=160)

ventana.mainloop()