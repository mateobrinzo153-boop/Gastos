import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import gastos

ventana = tk.Tk()
ventana.title("Gastos")
ventana.geometry("500x400")
mensaje = tk.Label(ventana, text="")
mensaje.grid(row=10, column=1)

nombre_var = tk.StringVar()
monto_var = tk.StringVar()
categoria_var = tk.StringVar()
fecha_var = tk.StringVar()
filtro_categoria_var = tk.StringVar(value="Todas")
gastos_visibles = []

def obtener_datos():
    nombre = nombre_var.get()
    monto = monto_var.get()
    categoria = categoria_var.get()
    fecha = fecha_var.get()
    resultado, texto = gastos.crear_gasto(nombre, monto, categoria, fecha)

    if resultado:
        mensaje.config(text=texto)
        nombre_var.set("")
        monto_var.set("")
        categoria_var.set("")
        fecha_var.set("")
        mostrar_gastos()
    else:
        mensaje.config(text=texto)

def mostrar_gastos():
    lista_gastos.delete(0, tk.END)
    gastos_visibles.clear()
    resultado = filtro_categoria_var.get()

    for gasto in gastos.gastos:
        if resultado == "Todas" or gasto["categoria"] == resultado:
            gastos_visibles.append(gasto)
            lista_gastos.insert(tk.END, f"{gasto['nombre']} - ${gasto['monto']} - {gasto['categoria']} - {gasto['fecha']}")

def seleccionar_gasto():
    resultado = lista_gastos.curselection()
    if not resultado:
        mensaje.config(text="Seleccioná un gasto primero.")
    else:
        gasto_seleccionado = gastos_visibles[resultado[0]]
        nombre_var.set(gasto_seleccionado["nombre"])
        monto_var.set(gasto_seleccionado["monto"])
        categoria_var.set(gasto_seleccionado["categoria"])
        fecha_var.set(gasto_seleccionado["fecha"])

def eliminar_gasto():
    resultado = lista_gastos.curselection()

    if not resultado:
        mensaje.config(text="Selecciona un gasto primero.")
        return
    else:
        gasto_seleccionado = gastos_visibles[resultado[0]]
        resultado = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que querés eliminar este gasto?")
        if resultado:
            gastos.eliminar_gasto(gasto_seleccionado)
            mensaje.config(text="Gasto eliminado correctamente.")
            mostrar_gastos()
        else:
            mensaje.config(text="Eliminacion cancelada.")
            return

def guardar_cambios():
    resultado = lista_gastos.curselection()

    if not resultado:
        mensaje.config(text="Selecciona un gasto primero.")
        return

    gasto_seleccionado = gastos_visibles[resultado[0]]

    nombre = nombre_var.get()
    monto = monto_var.get()
    categoria = categoria_var.get()
    fecha = fecha_var.get()

    exito, texto = gastos.editar_gasto_gui(
        gasto_seleccionado, nombre, monto, categoria, fecha
    )

    mensaje.config(text=texto)

    if exito:
        mostrar_gastos()

tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
tk.Label(ventana, text="Monto:").grid(row=1, column=0)
tk.Label(ventana, text="Categoria:").grid(row=2, column=0)
tk.Label(ventana, text="Fecha:").grid(row=3, column=0)
tk.Label(ventana, text="Filtrar por categoría:").grid(row=5, column=0)

entrada_nombre = tk.Entry(
    ventana,
    textvariable=nombre_var
).grid(row=0, column=1, sticky="w")
entrada_monto = tk.Entry(
    ventana,
    textvariable=monto_var
).grid(row=1, column=1, sticky="w")
entrada_categoria = ttk.Combobox(
    ventana,
    textvariable=categoria_var,
    values=("comida", "transporte", "servicios", "entretenimiento", "otros"),
    state="readonly"
).grid(row=2, column=1, sticky="w")
entrada_fecha = tk.Entry(
    ventana,
    textvariable=fecha_var
).grid(row=3, column=1, sticky="w")

filtro_categoria = ttk.Combobox(
    ventana,
    textvariable=filtro_categoria_var,
    values=("Todas", "comida", "transporte", "servicios", "entretenimiento", "otros"),
    state="readonly"
)
filtro_categoria.grid(row=5, column=1, sticky="w")
filtro_categoria.bind("<<ComboboxSelected>>", lambda evento: mostrar_gastos())

lista_gastos = tk.Listbox(ventana, width=60)
lista_gastos.grid(row=6, column=1)
mostrar_gastos()

tk.Button(
    ventana,
    text="Agregar gasto",
    command=obtener_datos
).grid(row=4, column=1, sticky="w")
tk.Button(
    ventana,
    text="Seleccionar Gasto",
    command=seleccionar_gasto
).grid(row=8, column=1)
tk.Button(
    ventana,
    text="Eliminar Gasto",
    command=eliminar_gasto
).grid(row=9, column=1)
tk.Button(
    ventana,
    text="Guardar gasto",
    command=guardar_cambios
).grid(row=1, column=1)
ventana.mainloop()
