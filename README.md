# Gastos

Aplicación de consola desarrollada en Python para registrar y administrar gastos personales.

El proyecto permite almacenar gastos, buscarlos, eliminarlos y consultar el dinero gastado por categoría. Los datos se guardan en un archivo JSON para conservarlos entre ejecuciones.

## Funcionalidades

- Agregar gastos.
- Ver todos los gastos registrados.
- Calcular el total de gastos.
- Buscar gastos por nombre.
- Eliminar gastos con confirmación.
- Buscar gastos por categoría.
- Calcular el total gastado en una categoría.
- Guardar los datos automáticamente en `gastos.json`.
- Cargar los datos al iniciar el programa.
- Manejar archivos inexistentes o JSON dañados mediante excepciones.

## Datos de cada gasto

Cada gasto contiene:

- Nombre
- Monto
- Categoría
- Fecha

## Tecnologías utilizadas

- Python 3
- JSON
- Git / GitHub

## Estructura

```text
Gastos/
├── main.py
├── gastos.py
├── gastos.json
├── .gitignore
└── README.md
```

## Cómo ejecutar

1. Clonar el repositorio.
2. Abrir la carpeta del proyecto.
3. Ejecutar:

```bash
python main.py
```

## Persistencia de datos

Los gastos se almacenan en `gastos.json`. Esto permite cerrar el programa y conservar los datos para la próxima ejecución.

El programa también maneja situaciones en las que el archivo no existe o contiene información JSON inválida.

## Objetivo del proyecto

Este proyecto fue desarrollado para practicar Python mediante un programa funcional, trabajando con:

- Listas y diccionarios
- Funciones
- Bucles y condicionales
- Validación de datos
- Manejo de excepciones
- Módulos
- Archivos
- JSON
- Persistencia de datos

## Próximas mejoras

Algunas mejoras posibles para futuras versiones:

- Editar gastos existentes.
- Agregar estadísticas de gastos.
- Filtrar por fechas.
- Utilizar SQLite como base de datos.
- Agregar tests automatizados.
- Crear una interfaz gráfica o web.

## Restante

- Editar gastos
- Agregar estadísticas
- Filtrar gastos por fechas
- Migrar de JSON a SQLite
- Agregar tests automatizados
- Crear una interfaz gráfica o web