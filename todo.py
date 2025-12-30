# To-Do List Application (CLI Based)

tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["completed"] else "❌"
            print(f"{i}. {task['task']} [{status}]")
        print()

def mark_completed():
    view_tasks()
    try:
        choice = int(input("Enter task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            print("Task marked as completed!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task():
    view_tasks()
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            tasks.pop(choice - 1)
            print("Task deleted successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

while True:
    print("---- To-Do List Application ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting application. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
