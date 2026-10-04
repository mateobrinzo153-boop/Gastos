import sqlite3

def conectar(base_datos):
    return sqlite3.connect(base_datos)

def crear_tabla(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            monto REAL NOT NULL,
            categoria TEXT NOT NULL,
            fecha TEXT NOT NULL
        )
    """)

    conn.commit()

conn = conectar("gastos.db")
crear_tabla(conn)

def agregar_gasto(gasto, conn):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO gastos (nombre, monto, categoria, fecha)
        VALUES (?, ?, ?, ?)
    """, (
        gasto["nombre"],
        gasto["monto"],
        gasto["categoria"],
        gasto["fecha"]
    ))

    gasto["id"] = cursor.lastrowid

    conn.commit()

def cargar_gastos(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nombre, monto, categoria, fecha
        FROM gastos
    """)

    filas = cursor.fetchall()

    lista_gastos = []

    for fila in filas:
        gasto = {
            "id": fila[0],
            "nombre": fila[1],
            "monto": fila[2],
            "categoria": fila[3],
            "fecha": fila[4]
        }

        lista_gastos.append(gasto)

    return lista_gastos

def eliminar(gasto, conn):
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM gastos
        WHERE id = ?
    """, (gasto["id"],))

    conn.commit()

def editar_gasto(gasto, conn):
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE gastos
        SET nombre = ?, monto = ?, categoria = ?, fecha = ?
        WHERE id = ?
    """, (
        gasto["nombre"],
        gasto["monto"],
        gasto["categoria"],
        gasto["fecha"],
        gasto["id"]
    ))

    conn.commit()

