import tkinter as tk
import gastos

ventana = tk.Tk()
ventana.title("Gastos")
ventana.geometry("500x400")
mensaje = tk.Label(ventana, text="")
mensaje.grid(row=5, column=1)


nombre_var = tk.StringVar()
monto_var = tk.StringVar()
categoria_var = tk.StringVar()
fecha_var = tk.StringVar()

def obtener_datos():
    nombre = nombre_var.get()
    monto = monto_var.get()
    categoria = categoria_var.get()
    fecha = fecha_var.get()
    print(nombre)
    print(monto)
    print(categoria)
    print(fecha)

    resultado, texto = gastos.crear_gasto(nombre, monto, categoria, fecha)

    if resultado:
        mensaje.config(text=texto)
        nombre_var.set("")
        monto_var.set("")
        categoria_var.set("")
        fecha_var.set("")
    else:
        mensaje.config(text=texto)

def mostrar_gastos():
    lista_gastos.delete(0, tk.END)
    for gasto in gastos.gastos:
        lista_gastos.insert(tk.END, f"{gasto['nombre']} - ${gasto['monto']} - {gasto['categoria']} - {gasto['fecha']}")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
tk.Label(ventana, text="Monto:").grid(row=1, column=0)
tk.Label(ventana, text="Categoria:").grid(row=2, column=0)
tk.Label(ventana, text="Fecha:").grid(row=3, column=0)

entrada_nombre = tk.Entry(
    ventana,
    textvariable=nombre_var
)
entrada_nombre.grid(row=0, column=1)
entrada_monto = tk.Entry(
    ventana,
    textvariable=monto_var
)
entrada_monto.grid(row=1, column=1)
entrada_categoria = tk.Entry(
    ventana,
    textvariable=categoria_var
)
entrada_categoria.grid(row=2, column=1)
entrada_fecha = tk.Entry(
    ventana,
    textvariable=fecha_var
)
entrada_fecha.grid(row=3, column=1)

lista_gastos = tk.Listbox(ventana)
lista_gastos.grid(row=6, column=1)
mostrar_gastos()

tk.Button(
    ventana,
    text="Agregar gasto",
    command=obtener_datos
).grid(row=4, column=1)
ventana.mainloop()