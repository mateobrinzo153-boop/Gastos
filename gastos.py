import almacenamiento

gastos = almacenamiento.cargar_gastos()

def agregar_gasto():
    nombre = input("Inserte el nombre del gasto: ")

    if not nombre.strip():
        print("Campo obligatorio.")
        return

    try:
        monto = float(input("Monto: ").strip())
    except ValueError:
        print("Insertar un numero.")
        return

    categoria = input("Inserte categoria: ")

    if not categoria.strip():
        print("Campo obligatorio.")
        return

    fecha = input("Inserte fecha: ")

    if not fecha.strip():
        print("Campo obligatorio.")
        return

    if monto <= 0:
        print("El monto debe ser mayor a 0.")
        return

    gasto = {
        "nombre": nombre,
        "monto": monto,
        "categoria": categoria,
        "fecha": fecha
    }

    gastos.append(gasto)
    almacenamiento.guardar_gastos(gastos)

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
                almacenamiento.guardar_gastos(gastos)
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
                    almacenamiento.guardar_gastos(gastos)
                elif respuesta == "n":
                    print("Edición cancelada.")
                    break
    if encontrado == False:
            print("Gasto no encontrado.")
            return

def estadisticas_gastos():
    total_gastos = 0
    for gasto in gastos:
        total_gastos += gasto["monto"]
    print(f"Total de gastos: ${total_gastos}")