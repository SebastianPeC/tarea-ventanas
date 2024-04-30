import tkinter as tk
from tkinter import messagebox

#CREACION DE LA VENTANA PRINCIPAL
ventana = tk.Tk()
ventana.title("Formulario Tkinter")
ventana.geometry("600x400")
ventana.resizable(True,True)
ventana.config(bg="light blue")

#creacion de la etiqueta y la entrada de nombre
nombre = tk.Label(ventana, text="Nombre")
nombre.grid(row=0, column=1)
ingresarnombre= tk.Entry(ventana, width=30)
ingresarnombre.grid(row=0,column=2)
nombre.config(bg="light blue",fg="black")

#creacion de la etiqueta y la entrada de apellido
apellido = tk.Label(ventana, text="Apellido")
apellido.grid(row=1, column=1)
ingresarapellido= tk.Entry(ventana, width=30)
ingresarapellido.grid(row=1,column=2)
apellido.config(bg="light blue",fg="black")

#creacion de la etiqueta y la entrada de edad
edad = tk.Label(ventana, text="Edad")
edad.grid(row=2, column=1)
ingresaredad= tk.Entry(ventana, width=30)
ingresaredad.grid(row=2,column=2)
edad.config(bg="light blue",fg="black")

#creacion de la etiqueta y la entrada de direccion
direccion = tk.Label(ventana, text="Direccion")
direccion.grid(row=3, column=1)
ingresardireccion= tk.Entry(ventana, width=30)
ingresardireccion.grid(row=3,column=2)
direccion.config(bg="light blue",fg="black")

#creacion de la etiqueta y la entrada de telefono
telefono = tk.Label(ventana, text="Telefono")
telefono.grid(row=4, column=1)
ingresartelefono= tk.Entry(ventana, width=30)
ingresartelefono.grid(row=4,column=2)
telefono.config(bg="light blue",fg="black")

#hacer frame para radiobutton
marco1 = tk.Frame(ventana, width=200, height=100, bd=2, relief="solid",bg="white")
marco1.grid(row=5, column=1)

#hacer radiobuttones para elegir sexo(label y opciones)
sexo = tk.Label(marco1, text="Sexo")
sexo.grid(row=0, column=2)
sexo.config(bg="white",fg="black",height=3)

genero = tk.StringVar()
BotonMasculino=tk.Radiobutton(marco1, text="Masculino",variable=genero, value="Masculino",bg="white",fg="black")
BotonMasculino.grid(row=1, column=2)
BotonFemenino=tk.Radiobutton(marco1, text="Femenino",variable=genero, value="Femenino",bg="white",fg="black")
BotonFemenino.grid(row=2, column=2)



#hacer frame para lista de ciudades
marco2 = tk.Frame(ventana, width=200, height=100, bd=2, relief="solid",bg="white")
marco2.grid(row=6, column=1)

# Lista de ciudades
ciudades = ["Bogotá", "Medellín", "Barranquilla", "Cartagena"]
listaciudad = tk.Listbox(marco2, height=5)
listaciudad.grid(row=2, column=2)
for ciudad in ciudades:
    listaciudad.insert(tk.END, ciudad)

# Función para registrar datos
def registrar():

    # Verificar si se ha seleccionado una ciudad
    if listaciudad.curselection():
        ciudad_index = listaciudad.curselection()[0]
        ciudad_seleccionada = ciudades[ciudad_index]

       

        # Mostrar los datos en un messagebox
        datos = f"Nombre: {ingresarnombre.get()}\nApellido: {ingresarapellido.get()}\nDirección: {ingresardireccion.get()}\nTeléfono: {ingresartelefono.get()}\nSexo: {genero.get()}\nEdad: {ingresaredad.get()}\nCiudad: {ciudad_seleccionada}"
        messagebox.showinfo("Datos Personales", datos)
    else:
        messagebox.showwarning("Error", "Por favor selecciona una ciudad.")

registrar_btn = tk.Button(ventana, text="Registrar", command=registrar)
registrar_btn.grid(row=8, column=2)


ventana.mainloop()