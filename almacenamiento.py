import sqlite3

conn = sqlite3.connect("gastos.db")
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


def guardar_gastos(lista_gastos):
    for gasto in lista_gastos:
        cursor.execute("""
            INSERT INTO gastos (nombre, monto, categoria, fecha)
            VALUES (?, ?, ?, ?)
        """, (
            gasto["nombre"],
            gasto["monto"],
            gasto["categoria"],
            gasto["fecha"]
        ))

    conn.commit()


def cargar_gastos():
    cursor.execute("""
        SELECT nombre, monto, categoria, fecha
        FROM gastos
    """)

    filas = cursor.fetchall()

    lista_gastos = []

    for fila in filas:
        print(fila)
        gasto = {
            "nombre": fila[0],
            "monto": fila[1],
            "categoria": fila[2],
            "fecha": fila[3]
        }

        lista_gastos.append(gasto)

    return lista_gastos

