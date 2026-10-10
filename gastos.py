import almacenamiento
from datetime import datetime

gastos = almacenamiento.cargar_gastos(almacenamiento.conn)

def crear_gasto(nombre, monto, categoria, fecha):
    if not nombre.strip() or not categoria.strip() or not fecha.strip():
        return False, "Todos los campos son obligatorios."

    try:
        monto = float(monto)
    except ValueError:
        return False, "Debes insertar un numero."

    if monto <= 0:
        return False, "El monto debe ser mayor a 0."

    try:
        datetime.strptime(fecha, "%d-%m-%Y")
    except ValueError:
        return False, "Formato de fecha inválido. Use DD-MM-YYYY."

    gasto = {
        "nombre": nombre,
        "monto": monto,
        "categoria": categoria,
        "fecha": fecha
    }
    gastos.append(gasto)
    almacenamiento.agregar_gasto(gasto, almacenamiento.conn)
    return True, "Gasto agregado correctamente."

def eliminar_gasto(gasto):
    gastos.remove(gasto)
    almacenamiento.eliminar(gasto, almacenamiento.conn)

def editar_gasto_gui(gasto, nombre, monto, categoria, fecha): 
    nombre = nombre.strip()
    categoria = categoria.lower().strip()
    fecha = fecha.strip()

    if not nombre or not categoria or not fecha:
        return False, "Todos los campos son obligatorios."

    try:
        monto = float(monto)
    except ValueError:
        return False, "El monto debe ser un número."

    if monto <= 0:
        return False, "El monto debe ser mayor a cero."

    from datetime import datetime
    try:
        datetime.strptime(fecha, "%d-%m-%Y")
    except ValueError:
        return False, "La fecha debe tener formato DD-MM-AAAA."

    gasto["nombre"] = nombre
    gasto["monto"] = monto
    gasto["categoria"] = categoria
    gasto["fecha"] = fecha

    almacenamiento.editar_gasto(gasto, almacenamiento.conn)

    return True, "Gasto editado exitosamente."
