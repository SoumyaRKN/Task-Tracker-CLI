import os
import json
import datetime
from constants import TASKS_FILE_NAME, Color


def init_tasks_file():
    """Initialize the tasks file if it doesn't exist."""
    if not os.path.exists(TASKS_FILE_NAME):
        with open(TASKS_FILE_NAME, "w") as file:
            json.dump([], file)


def load_tasks():
    """Load all tasks from the tasks file."""
    with open(TASKS_FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    """Save the list of tasks back to the tasks file."""
    with open(TASKS_FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    """Add a new task with the given description."""
    tasks = load_tasks()
    task_id = len(tasks) + 1
    now = datetime.datetime.now().isoformat()
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"{Color.GREEN}Task added successfully (ID: {task_id})!{Color.RESET}")


def update_task(task_id, description):
    """Update an existing task with the new description."""
    tasks = load_tasks()
    task = next((task for task in tasks if task["id"] == task_id), None)
    if not task:
        print(f"{Color.RED}Task not found!{Color.RESET}")
        return
    task["description"] = description
    task["updatedAt"] = datetime.datetime.now().isoformat()
    save_tasks(tasks)
    print(f"{Color.GREEN}Task updated successfully!{Color.RESET}")


def delete_task(task_id):
    """Delete a task by its ID."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"{Color.GREEN}Task deleted successfully!{Color.RESET}")


def change_status(task_id, new_status):
    """Change the status of a task to 'todo', 'in-progress', or 'done'."""
    if new_status not in ["todo", "in-progress", "done"]:
        print(f"{Color.RED}Invalid status: {new_status}{Color.RESET}")
        return
    tasks = load_tasks()
    task = next((task for task in tasks if task["id"] == task_id), None)
    if not task:
        print(f"{Color.RED}Task not found!{Color.RESET}")
        return
    task["status"] = new_status
    task["updatedAt"] = datetime.datetime.now().isoformat()
    save_tasks(tasks)
    print(f"{Color.GREEN}Task marked as {new_status} successfully!{Color.RESET}")


def list_tasks(status=None):
    """List all tasks or tasks filtered by status ('todo', 'in-progress', 'done')."""
    tasks = load_tasks()
    filtered_tasks = [
        task for task in tasks if status is None or task["status"] == status
    ]

    if not filtered_tasks:
        print(f"{Color.YELLOW}No tasks found.{Color.RESET}")
        return

    print(f"{Color.CYAN}Tasks:{Color.RESET}")
    for task in filtered_tasks:
        print(
            f"{Color.BLUE}ID: {task['id']} - {task['description']} [{task['status']}]{Color.RESET}"
        )
