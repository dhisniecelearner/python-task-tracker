import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()


def add_task():
    description = input("Enter task description: ")

    if not description.strip():
        print("Task description cannot be empty!")
        return

    if tasks:
        task_id = max(task["id"] for task in tasks) + 1
    else:
        task_id = 1

    task = {
        "id": task_id,
        "description": description,
        "status": "todo"
    }

    tasks.append(task)
    save_tasks()
    print("Task added successfully!")


def update_task():
    task_id = int(input("Enter task ID to update: "))

    for task in tasks:
        if task["id"] == task_id:
            new_description = input("Enter new description: ")

            if new_description.strip():
                task["description"] = new_description
                save_tasks()
                print("Task updated successfully!")
            else:
                print("Description cannot be empty!")
            return

    print("Task not found!")


def delete_task():
    task_id = int(input("Enter task ID to delete: "))

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks()
            print("Task deleted successfully!")
            return

    print("Task not found!")


def mark_task():
    task_id = int(input("Enter task ID: "))

    for task in tasks:
        if task["id"] == task_id:
            print("1. Mark as in-progress")
            print("2. Mark as done")

            choice = input("Choose status: ")

            if choice == "1":
                task["status"] = "in-progress"
            elif choice == "2":
                task["status"] = "done"
            else:
                print("Invalid choice!")
                return

            save_tasks()
            print("Task status updated!")
            return

    print("Task not found!")


def list_tasks():
    if not tasks:
        print("No tasks found!")
        return

    print("\n--- Your Tasks ---")

    for task in tasks:
        print(
            "ID:", task["id"],
            "| Description:", task["description"],
            "| Status:", task["status"]
        )


while True:
    print("\n===== TASK TRACKER =====")
    print("1. Add task")
    print("2. Update task")
    print("3. Delete task")
    print("4. Mark task status")
    print("5. List all tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            add_task()

        elif choice == "2":
            update_task()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            mark_task()

        elif choice == "5":
            list_tasks()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please choose 1 to 6.")

    except ValueError:
        print("Please enter a valid number!")
