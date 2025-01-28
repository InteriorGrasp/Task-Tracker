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
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


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
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} (Created: {task['createdAt']})")


def main():
    """Main CLI function."""
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [options]")
        return

    command = sys.argv[1]
    if command == "add":
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "update":
        task_id = int(sys.argv[2])
        description = " ".join(sys.argv[3:])
        update_task(task_id, description)
    elif command == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_id)
    elif command == "mark-in-progress":
        task_id = int(sys.argv[2])
        mark_task(task_id, "in-progress")
    elif command == "mark-done":
        task_id = int(sys.argv[2])
        mark_task(task_id, "done")
    elif command == "list":
        filter_status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(filter_status)
    else:
        print("Unknown command. Available commands: add, update, delete, mark-in-progress, mark-done, list")


if __name__ == "__main__":
    main()
