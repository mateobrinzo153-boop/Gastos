import almacenamiento
from datetime import datetime

gastos = almacenamiento.cargar_gastos(almacenamiento.conn)

def agregar_gasto():
    nombre = input("Inserte el nombre del gasto: ")
    monto = input("Monto: ").strip()
    categoria = input("Inserte categoria: ")
    fecha = input("Inserte fecha (DD-MM-YYYY): ").strip()

    resultado = crear_gasto(nombre, monto, categoria, fecha)

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

def ver_gastos():
    if not gastos:
        print("No hay gastos registrados.")
        return
    total_gastos = 0
    for gasto in gastos:
        print(f"{gasto['nombre']} - ${gasto['monto']} - Categoria: {gasto['categoria']} - Fecha: {gasto['fecha']}")
        total_gastos += gasto["monto"]
    print(f"Total de gastos: ${total_gastos}")

def eliminar_gasto():
    nombre = input("Inserte nombre del gasto a eliminar: ").lower().strip()
    encontrado = False
    for gasto in gastos:
        if gasto["nombre"].lower().strip() == nombre:
            respuesta = input("Desea eliminar este gasto? (s/n)").lower().strip()
            encontrado = True
            while respuesta not in ["s","n"]:
                print("Respuesta no valida. Ingrese 's' para sí o 'n' para no.")
                respuesta = input().lower().strip()
            if respuesta == "s":
                gastos.remove(gasto)
                almacenamiento.eliminar(gasto, almacenamiento.conn)
            elif respuesta == "n":
                print("Eliminacion cancelada.")
                break
    if encontrado == False:
        print("Gasto no encontrado.")
        return

def buscar_gasto():
    nombre = input("Inserte nombre del gasto a buscar: ").lower().strip()
    encontrado = False
    for gasto in gastos:
        if gasto["nombre"].lower().strip() == nombre:
            print(f"{gasto['nombre']} - ${gasto['monto']} - Categoria: {gasto['categoria']} - Fecha: {gasto['fecha']}")
            encontrado = True
    if not encontrado:
        print("Gasto no encontrado")

def gastos_por_categoria():
    total_categoria = 0
    categoria = input("Inserte categoria a buscar: ").lower().strip()
    encontrado = False
    if not categoria.strip():
        print("Inserte una categoria")
        return
    for gasto in gastos:
        if gasto["categoria"].lower().strip() == categoria:
            print(f"{gasto['nombre']} - ${gasto['monto']} - Categoria: {gasto['categoria']} - Fecha: {gasto['fecha']}")
            total_categoria += gasto["monto"]
            encontrado = True
    if not encontrado:
        print("No hay gastos en esta categoria")
    else:
        print(f"Total de gastos en la categoria '{categoria}': ${total_categoria}")

def filtrar_por_fecha(): 
    if not gastos:
        print("No hay gastos registrados.")
        return

    try:
        fecha_inicial = str(input("Ingrese la fecha inicial (DD-MM-YYYY): ")).strip()
        fecha_final = str(input("Ingrese la fecha final (DD-MM-YYYY): ")).strip()
        fecha_inicial = datetime.strptime(fecha_inicial, "%d-%m-%Y")
        fecha_final = datetime.strptime(fecha_final, "%d-%m-%Y")
    except ValueError:
        print("Formato de fecha invalido. Por favor, use el formato DD-MM-YYYY.")
        return
    if fecha_inicial > fecha_final:
        print("La fecha inicial no puede ser mayor que la fecha final.")
        return

    encontrado = False
    for gasto in gastos:
        fecha_gasto = datetime.strptime(gasto["fecha"], "%d-%m-%Y")
        if fecha_inicial <= fecha_gasto <= fecha_final:
            print(f"{gasto['nombre']} - ${gasto['monto']} - Categoria: {gasto['categoria']} - Fecha: {gasto['fecha']}")
            encontrado = True
    if not encontrado:
        print("No hay gastos en este rango de fechas.")

def editar_gasto():
    nombre = input("Inserte el nombre del gasto: ")
    encontrado = False
    for gasto in gastos:
        if gasto["nombre"].lower().strip() == nombre:
                respuesta = input("Desea editar este gasto? (s/n)").lower().strip()
                encontrado = True
                while respuesta not in ["s","n"]:
                    print("Respuesta no valida. Ingrese 's' para sí o 'n' para no.")
                    respuesta = input().lower().strip()
                if respuesta == "s":
                    nuevo_nombre = input("Inserte el nuevo nombre del gasto: ").strip()
                    if not nuevo_nombre.strip():
                        print("Campo obligatorio.")
                        return
                    try:
                        nuevo_monto = float(input("Inserte nuevo monto: "))
                        if nuevo_monto <= 0:
                            print("Inserte un numero mayor a 0.")
                            return
                        nueva_categoria = input("Inserte nueva categoria: ").lower().strip()
                        if not nueva_categoria.strip():
                            print("campo obligatorio.")
                            return
                        nueva_fecha = input("Inserte nueva fecha: ").strip()
                        if not nueva_fecha.strip():
                            print("campo obligatorio.")
                            return
                    except ValueError:
                        print("Insertar un numero.")
                        return
                    gasto["nombre"] = nuevo_nombre
                    gasto["monto"] = nuevo_monto
                    gasto["categoria"] = nueva_categoria
                    gasto["fecha"] = nueva_fecha
                    print("Gasto editado exitosamente.")
                    almacenamiento.editar_gasto(gasto, almacenamiento.conn)
                elif respuesta == "n":
                    print("Edición cancelada.")
                    break
    if encontrado == False:
            print("Gasto no encontrado.")
            return

def estadisticas_gastos():
    if gastos == []:
        print("No hay gastos registrados.")
        return
    
    suma_de_gastos = sum(gasto["monto"] for gasto in gastos)
    print(f"Total de gastos: ${suma_de_gastos}")

    promedio_de_gastos = suma_de_gastos / len(gastos)
    print(f"Promedio de gastos: ${promedio_de_gastos:.2f}")
    
    gasto_mas_alto = max(gastos, key=lambda x: x["monto"])
    print(f"Gasto más alto: {gasto_mas_alto['nombre']} - ${gasto_mas_alto['monto']}")
    
    gasto_mas_bajo = min(gastos, key=lambda x: x["monto"])
    print(f"Gasto más bajo: {gasto_mas_bajo['nombre']} - ${gasto_mas_bajo['monto']}")
    
    cantidad_de_gastos = len(gastos)
    print(f"Cantidad de gastos: {cantidad_de_gastos}")
    
    total_categoria = {}
    for gasto in gastos:
        categoria = gasto["categoria"].lower().strip()
        if categoria in total_categoria:
            total_categoria[categoria] += gasto["monto"]
        else:
            total_categoria[categoria] = gasto["monto"]
    print("Total por categoría:")
    for categoria, total in total_categoria.items():
        print(f"  {categoria.capitalize()}: ${total}")