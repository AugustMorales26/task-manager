import json
from colorama import init, Fore, Style
import os

init()  # Inicializar colorama

# Clase Task para representar una tarea
class Task:
    def __init__(self, title, category, priority, due_date, completed=False):
        self.title = title
        self.category = category
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "Completada" if self.completed else "Pendiente"
        return f"{self.title} ({self.category}): {status} - Prioridad: {self.priority} - Fecha de vencimiento: {self.due_date}"

# Clase TaskManager para gestionar las tareas
class TaskManager:
    def __init__(self, file_name):
        self.tasks = []
        self.file_name = file_name
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, "r") as f:
                self.tasks = [Task(**task) for task in json.load(f)]
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open(self.file_name, "w") as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def create_task(self, title, category, priority, due_date):
        task = Task(title, category, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def read_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self, title, completed):
        for task in self.tasks:
            if task.title == title:
                task.completed = completed
                self.save_tasks()
                return
        print(f"Tarea '{title}' no encontrada")

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                self.save_tasks()
                return
        print(f"Tarea '{title}' no encontrada")

    def filter_tasks(self, status):
        for task in self.tasks:
            if task.completed == status:
                print(task)

    def organize_tasks(self, category):
        for task in self.tasks:
            if task.category == category:
                print(task)

    def show_help(self):
        print("Ayuda:")
        print("1. Crear tarea: Ingrese el título, categoría, prioridad y fecha de vencimiento de la tarea.")
        print("2. Leer tareas: Muestra todas las tareas.")
        print("3. Actualizar tarea: Ingrese el título de la tarea y el nuevo estado (True/False).")
        print("4. Eliminar tarea: Ingrese el título de la tarea a eliminar.")
        print("5. Filtrar tareas por estado: Ingrese el estado de la tarea (completadas/pending).")
        print("6. Organizar tareas por categoría: Ingrese la categoría de la tarea.")
        print("7. Salir: Sale del programa.")
        print("8. Mostrar ayuda: Muestra este mensaje de ayuda.")
        print("9. Mostrar resumen: Muestra un resumen de las tareas pendientes y completadas.")
        print("10. Mostrar estadísticas: Muestra estadísticas sobre las tareas completadas y pendientes.")

    def show_summary(self):
        pending_tasks = [task for task in self.tasks if not task.completed]
        completed_tasks = [task for task in self.tasks if task.completed]
        print(f"Tareas pendientes: {len(pending_tasks)}")
        print(f"Tareas completadas: {len(completed_tasks)}")

    def show_statistics(self):
        pending_tasks = [task for task in self.tasks if not task.completed]
        completed_tasks = [task for task in self.tasks if task.completed]

        print("Estadísticas:")
        print(f"Tareas pendientes: {len(pending_tasks)}")
        print(f"Tareas completadas: {len(completed_tasks)}")
        print(f"Porcentaje de tareas completadas: {(len(completed_tasks) / len(self.tasks)) * 100:.2f}%")
        print(f"Prioridad promedio de tareas pendientes: {sum(task.priority == 'Alta' for task in pending_tasks) / len(pending_tasks):.2f}")
        print(f"Categoría más común de tareas pendientes: {max(set(task.category for task in pending_tasks), key=list(task.category for task in pending_tasks).count)}")

def main():
    task_manager = TaskManager("tasks.json")

    while True:
        os.system("clear")  # Limpiar pantalla
        print(Fore.GREEN + "Menú de Gestor de Tareas" + Style.RESET_ALL)
        print("1. Crear tarea")
        print("2. Leer tareas")
        print("3. Actualizar tarea")
        print("4. Eliminar tarea")
        print("5. Filtrar tareas por estado")
        print("6. Organizar tareas por categoría")
        print("7. Salir")
        print("8. Mostrar ayuda")
        print("9. Mostrar resumen")
        print("10. Mostrar estadísticas")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            os.system("clear")  # Limpiar pantalla
            print("Crear tarea")
            title = input("Ingrese el título de la tarea: ")
            category = input("Ingrese la categoría de la tarea: ")
            priority = input("Ingrese la prioridad de la tarea (Alta/Media/Baja): ")
            due_date = input("Ingrese la fecha de vencimiento de la tarea (dd/mm/yyyy): ")
            task_manager.create_task(title, category, priority, due_date)
            print(f"Tarea '{title}' creada")
            input("Presione Enter para continuar...")

        elif choice == "2":
            os.system("clear")  # Limpiar pantalla
            print("Leer tareas")
            task_manager.read_tasks()
            input("Presione Enter para continuar...")

        elif choice == "3":
            os.system("clear")  # Limpiar pantalla
            print("Actualizar tarea")
            title = input("Ingrese el título de la tarea a actualizar: ")
            completed = input("Ingrese el estado de la tarea (True/False): ")
            task_manager.update_task(title, completed == "True")
            input("Presione Enter para continuar...")

        elif choice == "4":
            os.system("clear")  # Limpiar pantalla
            print("Eliminar tarea")
            title = input("Ingrese el título de la tarea a eliminar: ")
            task_manager.delete_task(title)
            input("Presione Enter para continuar...")

        elif choice == "5":
            os.system("clear")  # Limpiar pantalla
            print("Filtrar tareas por estado")
            status = input("Ingrese el estado de la tarea (completadas/pending): ")
            status = status == "completadas"
            task_manager.filter_tasks(status)
            input("Presione Enter para continuar...")

        elif choice == "6":
            os.system("clear")  # Limpiar pantalla
            print("Organizar tareas por categoría")
            category = input("Ingrese la categoría de la tarea: ")
            task_manager.organize_tasks(category)
            input("Presione Enter para continuar...")

        elif choice == "7":
            break

        elif choice == "8":
            os.system("clear")  # Limpiar pantalla
            print("Mostrar ayuda")
            task_manager.show_help()
            input("Presione Enter para continuar...")

        elif choice == "9":
            os.system("clear")  # Limpiar pantalla
            print("Mostrar resumen")
            task_manager.show_summary()
            input("Presione Enter para continuar...")

        elif choice == "10":
            os.system("clear")  # Limpiar pantalla
            print("Mostrar estadísticas")
            task_manager.show_statistics()
            input("Presione Enter para continuar...")

        else:
            print("Opción inválida. Intente de nuevo.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()