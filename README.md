# Gastos

Aplicación de escritorio desarrollada en Python para registrar y administrar gastos personales mediante una interfaz gráfica.

El proyecto permite agregar, consultar, editar y eliminar gastos, además de filtrarlos por categoría. Los datos se almacenan en una base de datos SQLite para conservarlos entre ejecuciones.

## Funcionalidades

- Agregar gastos.
- Ver los gastos registrados.
- Editar gastos existentes.
- Eliminar gastos.
- Filtrar gastos por categoría.
- Validar los datos ingresados.
- Guardar los gastos en una base de datos SQLite.
- Cargar los datos almacenados al iniciar la aplicación.

## Datos de cada gasto

Cada gasto contiene:

- Nombre
- Monto
- Categoría
- Fecha

## Tecnologías utilizadas

- Python 3
- Tkinter
- SQLite
- Pytest
- Git / GitHub

## Estructura

El proyecto se organiza en módulos para separar la interfaz gráfica, la lógica de los gastos y el almacenamiento de los datos.

- `interfaz.py`: interfaz gráfica de la aplicación.
- `gastos.py`: lógica y operaciones relacionadas con los gastos.
- `almacenamiento.py`: gestión de la persistencia mediante SQLite.
- `gastos.db`: base de datos utilizada para almacenar los gastos.

## Cómo ejecutar

1. Abrir la carpeta del proyecto.
2. Abrir una terminal en esa ubicación.
3. Ejecutar:

```bash
python interfaz.py
```

Si el sistema utiliza `python3`, ejecutar:

```bash
python3 interfaz.py
```

## Persistencia de datos

Los gastos se almacenan mediante SQLite. Esto permite cerrar la aplicación y conservar la información para la próxima ejecución.

La gestión de la base de datos está separada de la lógica principal para facilitar el mantenimiento del código.

## Pruebas

El proyecto utiliza Pytest para ejecutar pruebas automatizadas.

Para ejecutar las pruebas, utilizar:

```bash
python -m pytest
```

## Objetivo del proyecto

Este proyecto fue desarrollado para practicar Python mediante una aplicación funcional, trabajando con:

- Listas y diccionarios
- Funciones y módulos
- Programación orientada a eventos
- Interfaces gráficas con Tkinter
- Validación de datos
- Manejo de excepciones
- Bases de datos SQLite
- Persistencia de datos
- Pruebas automatizadas
- Organización y mantenimiento de código

## Posibles mejoras futuras

- Incorporar estadísticas y resúmenes de gastos.
- Agregar filtros por fecha.
- Mejorar la visualización de los gastos.
- Ampliar la cobertura de las pruebas automatizadas.

