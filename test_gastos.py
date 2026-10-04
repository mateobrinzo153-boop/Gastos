import sqlite3
import pytest
import gastos
import almacenamiento

@pytest.fixture
def base_de_prueba():
    conn = sqlite3.connect(":memory:")
    almacenamiento.crear_tabla(conn)

    yield conn

    conn.close()

def test_agregar_gasto(base_de_prueba):
    conn = base_de_prueba

    gasto = {
        "nombre": "Prueba",
        "monto": 100.0,
        "categoria": "Test",
        "fecha": "2024-01-01"
    }

    almacenamiento.agregar_gasto(gasto, conn)

    gastos = almacenamiento.cargar_gastos(conn)
    assert len(gastos) == 1
    assert gastos[0]["nombre"] == gasto["nombre"]

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gastos WHERE nombre = ?", (gasto["nombre"],))
    resultado = cursor.fetchone()
    assert resultado is not None
    assert resultado[1] == gasto["nombre"]
    assert resultado[2] == gasto["monto"]
    assert resultado[3] == gasto["categoria"]
    assert resultado[4] == gasto["fecha"]

def test_eliminar_gasto(base_de_prueba):
    conn = base_de_prueba

    gasto = {
        "nombre": "Prueba",
        "monto": 100.0,
        "categoria": "Test",
        "fecha": "2024-01-01"
    }

    almacenamiento.agregar_gasto(gasto, conn)

    almacenamiento.eliminar(gasto, conn)

    gastos = almacenamiento.cargar_gastos(conn)

    assert len(gastos) == 0

def test_editar_gasto(base_de_prueba):
    conn = base_de_prueba

    gasto = {
        "nombre": "Prueba",
        "monto": 100.0,
        "categoria": "Test",
        "fecha": "2024-01-01"
    }

    almacenamiento.agregar_gasto(gasto, conn)

    gasto["nombre"] = "Prueba Editada"
    gasto["monto"] = 200.0
    gasto["categoria"] = "Comida"
    gasto["fecha"] = "05-10-2026"

    almacenamiento.editar_gasto(gasto, conn)

    gastos = almacenamiento.cargar_gastos(conn)

    assert gastos[0]["nombre"] == "Prueba Editada"
    assert gastos[0]["monto"] == 200.0
    assert gastos[0]["categoria"] == "Comida"
    assert gastos[0]["fecha"] == "05-10-2026"

def test_gastos_tienen_datos_necesarios(base_de_prueba):
    conn = base_de_prueba
    almacenamiento.agregar_gasto({
        "nombre": "Gasto Test",
        "monto": 50.0,
        "categoria": "Test",
        "fecha": "2024-01-01"
    }, conn)
    gastos = almacenamiento.cargar_gastos(conn)
    for gasto in gastos:
        assert "id" in gasto
        assert "nombre" in gasto
        assert "monto" in gasto
        assert "categoria" in gasto
        assert "fecha" in gasto

