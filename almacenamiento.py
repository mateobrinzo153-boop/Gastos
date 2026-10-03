import json

def guardar_gastos(lista_gastos):
    with open("gastos.json", "w") as archivo:
        json.dump(lista_gastos, archivo)

def cargar_gastos():
    try:
        with open("gastos.json", "r") as archivo:
            lista_gastos = json.load(archivo)
        print("Datos de la sesión anterior:")
        return lista_gastos
    except FileNotFoundError:
        lista_gastos = []
        return lista_gastos
    except json.JSONDecodeError:
        print("Error al cargar los gastos. El archivo está dañado.")
        lista_gastos = []
        return lista_gastos


        