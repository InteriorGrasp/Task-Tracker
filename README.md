# Task-Tracker
A simple command-line tool for managing tasks. You can add, update, delete, mark as "in-progress" or "done," and list tasks with optional filtering by status. 
https://roadmap.sh/projects/task-tracker

## Features
- Add a task: Add a new task with a description.
- Update a task: Modify the description of an existing task.
- Delete a task: Remove a task by its ID.
- Mark tasks: Mark a task as "in-progress" or "done."
- List tasks: List all tasks, or filter them by their status (e.g., todo, in-progress, done).
- Optional due dates: Add due dates to tasks to keep track of deadlines.
- Task priorities: Set priorities (e.g., low, medium, high) for tasks (if implemented).
- Task statuses: Color-coded task statuses for better readability.

## Usage
The task tracker is run from the command line with the following commands:

add <description>
Add a new task with the provided description.
- python task_tracker.py add "Buy groceries"

update <id> <new description>
Update the description of an existing task by providing its ID and new description.
- python task_tracker.py update 1 "Buy vegetables"

delete <id>
Delete a task by providing its ID.
- python task_tracker.py delete 1

mark-in-progress <id>
Mark a task as "in-progress."
- python task_tracker.py mark-in-progress 1

mark-done <id>
Mark a task as "done."
- python task_tracker.py mark-done 1

list [status]
List tasks. Optionally filter by status (todo, in-progress, done).
- python task_tracker.py list
- python task_tracker.py list todo
- python task_tracker.py list in-progress
- python task_tracker.py list done

help
Display a list of available commands and their usage.
- python task_tracker.py help

## Task Statuses
- todo: The task is not yet started.
- in-progress: The task is currently being worked on.
- done: The task is completed.

## Task File (task.json)
The task data is stored in a JSON file named tasks.json in the same directory. If the file does not exist, it will be created automatically.

## Contributing
If you'd like to contribute to this project, feel free to fork it, make changes, and submit a pull request. All contributions are welcome!

## License
This project is open-source and available under the MIT License. See the LICENSE file for more information.