import sys
import json
from colorama import Fore, Style
from datetime import datetime
from pathlib import Path

# Define the file path
TASKS_FILE = Path("tasks.json")

STATUS_COLORS = {
    "todo": Fore.RED,
    "in-progress": Fore.YELLOW,
    "done": Fore.GREEN,
}


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


def format_datetime(dt_str):
    """Convert ISO datetime string to a readable format."""
    try:
        dt = datetime.fromisoformat(dt_str)
        return dt.strftime("%B %d, %Y, %I:%M %p")  # Example: January 28, 2025, 05:20 AM
    except ValueError:
        return dt_str  # Return as-is if it's already formatted incorrectly


def get_current_iso_time():
    """Return the current time in ISO format."""
    return datetime.now().isoformat()


def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    task_id = len(tasks) + 1
    current_time = get_current_iso_time()
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": current_time,
        "updatedAt": current_time,
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
            task["updatedAt"] = get_current_iso_time()
            save_tasks(tasks)
            print(f"Task updated successfully (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found.")


def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if task["id"] != task_id]
    if len(filtered_tasks) == len(tasks):
        print(f"Task with ID {task_id} not found.")
    else:
        save_tasks(filtered_tasks)
        print(f"Task deleted successfully (ID: {task_id})")


def mark_task(task_id, status):
    """Mark a task as in-progress or done."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = get_current_iso_time()
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
        created_at = format_datetime(task["createdAt"])
        updated_at = format_datetime(task["updatedAt"])
        status_color = STATUS_COLORS.get(task["status"], Fore.WHITE)
        print(f"{status_color}[{task['id']}] {task['description']} - {task['status']} "
              f"(Created: {created_at}, Updated: {updated_at}){Style.RESET_ALL}")


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
        description = " ".join(arguments)
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
            print("Error: Task ID must be a number.")
    elif command == "delete":
        if len(arguments) < 1:
            print("Error: Missing task ID.")
            return
        try:
            task_id = int(arguments[0])
            delete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a number.")
    elif command == "mark-in-progress":
        if len(arguments) < 1:
            print("Error: Missing task ID.")
            return
        try:
            task_id = int(arguments[0])
            mark_task(task_id, "in-progress")
        except ValueError:
            print("Error: Task ID must be a number.")
    elif command == "mark-done":
        if len(arguments) < 1:
            print("Error: Missing task ID.")
            return
        try:
            task_id = int(arguments[0])
            mark_task(task_id, "done")
        except ValueError:
            print("Error: Task ID must be a number.")
    elif command == "list":
        if len(arguments) == 0:
            list_tasks()
        else:
            status = arguments[0].lower()
            list_tasks(status)
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
