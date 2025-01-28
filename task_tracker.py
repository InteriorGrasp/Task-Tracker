import sys
import json
from datetime import datetime
from pathlib import Path

# Define the file path
TASKS_FILE = Path("tasks.json")


def load_tasks():
    """Load tasks from the JSON file."""
    if not TASKS_FILE.exists():
        return []
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")


def update_task(task_id, new_description):
    """Update an existing task."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task updated successfully (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found.")


def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task deleted successfully (ID: {task_id})")


def mark_task(task_id, status):
    """Mark a task as in-progress or done."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status} (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found.")


def list_tasks(filter_status=None):
    """List tasks based on their status."""
    tasks = load_tasks()
    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} (Created: {task['createdAt']})")

def show_help():
    """Show help for available commands."""
    help_text = """
Task Tracker - Command List:

1. add <description>             Add a new task.
2. update <id> <description>     Update an existing task's description.
3. delete <id>                   Delete a task by its ID.
4. mark-in-progress <id>         Mark a task as 'in-progress'.
5. mark-done <id>                Mark a task as 'done'.
6. list [status]                 List tasks (optionally filtered by status: 'todo', 'in-progress', 'done').
    """
    print(help_text)


def main():
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py <command> [arguments]")
        return

    command = sys.argv[1].lower()  # Convert the command to lowercase
    arguments = sys.argv[2:]

    if command == "add":
        if len(arguments) < 1:
            print("Error: Missing task description.")
            return
        description = " ".join(arguments)  # Handle multi-word descriptions
        add_task(description)
    elif command == "update":
        if len(arguments) < 2:
            print("Error: Missing task ID or description.")
            return
        try:
            task_id = int(arguments[0])
            description = " ".join(arguments[1:])
            update_task(task_id, description)
        except ValueError:
            print("Error: Task ID must be an integer.")
    elif command == "delete":
        if len(arguments) < 1:
            print("Error: Missing task ID.")
            return
        try:
            task_id = int(arguments[0])
            delete_task(task_id)
        except ValueError:
            print("Error: Task ID must be an integer.")
    elif command == "mark-in-progress":
        if len(arguments) < 1:
            print("Error: Missing task ID.")
            return
        try:
            task_id = int(arguments[0])
            mark_task(task_id, "in-progress")
        except ValueError:
            print("Error: Task ID must be an integer.")
    elif command == "mark-done":
        if len(arguments) < 1:
            print("Error: Missing task ID.")
            return
        try:
            task_id = int(arguments[0])
            mark_task(task_id, "done")
        except ValueError:
            print("Error: Task ID must be an integer.")
    elif command == "list":
        if len(arguments) == 0:
            list_tasks()
        else:
            status = arguments[0].lower()
            list_tasks(status)
    elif command == "help":
        show_help()
    else:
        print(f"Unknown command: {command}.\nAvailable commands: add, update, delete, mark-in-progress, mark-done, list.")


if __name__ == "__main__":
    main()
 