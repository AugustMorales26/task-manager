![Imagen de ejemplo](Captura%20desde%202024-07-01%2006-58-29.png)

# Task-Manager
Task-Manager es una aplicación de terminal desarrollada en Python para gestionar tareas de manera eficiente y organizada. Con esta herramienta, puedes agregar, eliminar, actualizar y ver tus tareas pendientes, todo desde la línea de comandos.

## Características

* Agregar Tareas: Crea nuevas tareas ingresando el título, categoría, prioridad y fecha de vencimiento.
* Leer Tareas: Visualiza todas las tareas creadas junto con su estado, prioridad y fecha de vencimiento.
* Actualizar Tareas: Marca una tarea como completada o pendiente.
* Eliminar Tareas: Elimina tareas por título.
* Filtrar Tareas: Filtra tareas por su estado (completadas o pendientes).
* Organizar Tareas: Organiza las tareas por categorías.
* Resumen: Muestra un resumen de las tareas pendientes y completadas.
* Estadísticas: Proporciona estadísticas sobre las tareas completadas y pendientes, incluyendo el porcentaje de tareas completadas y la categoría más común.

## Dependencias

* `json`: Utilizado para almacenar y cargar tareas desde un archivo JSON.
* `colorama`: Usado para colorear la salida de texto en la terminal.
* `os`: Utilizado para limpiar la pantalla del terminal.

Instala las dependencias con el siguiente comando:
```bash
pip install colorama
