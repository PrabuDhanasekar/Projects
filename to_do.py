import json

tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def add_task():
    task_name = input("Enter task name: ")
    category = input("Enter category (Work/Personal/Others): ")
    tasks.append({"name": task_name, "category": category, "status": "Pending"})
    save_tasks()
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']} [{task['category']}] - {task['status']}")

def mark_completed():
    view_tasks()
    task_number = int(input("Enter task number to mark as completed: "))
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["status"] = "Completed"
        save_tasks()
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter task number to delete: "))
    if 0 < task_number <= len(tasks):
        del tasks[task_number - 1]
        save_tasks()
        print("Task deleted!")
    else:
        print("Invalid task number.")

def menu():
    load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

