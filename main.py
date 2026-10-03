import almacenamiento
import gastos

almacenamiento.cargar_gastos()   
gastos.ver_gastos()

opcion = ""

while opcion != "8":
    print("""
    ------Lista de Gastos------
    |   1. Agregar gasto      |
    |   2. Ver gastos         |
    |   3. Buscar gasto       |
    |   4. Eliminar gasto     |
    |   5. Gastos p categoria |
    |   6. Editar gasto       |
    |   7. Estadísticas       |
    |   8. Salir              |
    ---------------------------
    """)
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        gastos.agregar_gasto()
    elif opcion == "2":
        gastos.ver_gastos()
    elif opcion == "3":
        gastos.buscar_gasto()
    elif opcion == "4":
        gastos.eliminar_gasto()
    elif opcion == "5":
        gastos.gastos_por_categoria()
    elif opcion == "6":
        gastos.editar_gasto()
    elif opcion == "7":
        gastos.estadisticas_gastos()
    elif opcion == "8":
        print("¡Hasta luego!")
        break 
    else:
        print("Opción no válida.")
        

    
    