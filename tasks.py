import json
import os
from datetime import datetime

TASKS_FILE = "data/tasks.json"

def load_tasks():
    """Load tasks from JSON, ensure priorities exist, and sort by priority."""
    if not os.path.exists(TASKS_FILE):
        save_tasks([])
        return []

    with open(TASKS_FILE, "r") as file:
        try:
            tasks = json.load(file)

            # Ensure all tasks have a priority (default: "none")
            for task in tasks:
                if "priority" not in task:
                    task["priority"] = "none"  # Assign default priority

            # Sorting order: High -> Medium -> Low -> None
            priority_order = {"high": 1, "medium": 2, "low": 3, "none": 4}
            tasks.sort(key=lambda task: priority_order.get(task["priority"], 4))

            save_tasks(tasks)  # Save sorted & fixed data
            return tasks

        except json.JSONDecodeError:
            print("⚠️ Corrupt JSON detected. Resetting file.")
            save_tasks([])
            return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description, priority="none"):
    """Add a new task with a priority."""
    valid_priorities = ["high", "medium", "low", "none"]
    
    if priority not in valid_priorities:
        print("⚠️ Invalid priority. Choose from: high, medium, low, none.")
        return

    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,  # Auto-increment ID
        "description": description,
        "priority": priority,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"✅ Task added: {description} (Priority: {priority})")

def complete_task(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()
    
    # Find the task by ID
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"✅ Task {task_id} marked as complete!")
            return
    
    print(f"⚠️ Task {task_id} not found.")

def delete_task(task_id):
    """Delete a task and reassign task IDs."""
    tasks = load_tasks()
    
    # Filter out the task that matches the given ID
    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(updated_tasks) == len(tasks):
        print(f"⚠️ Task {task_id} not found.")
        return

    # Reassign IDs sequentially
    for index, task in enumerate(updated_tasks, start=1):
        task["id"] = index

    save_tasks(updated_tasks)
    print(f"🗑️ Task {task_id} deleted, and task IDs updated.")

def edit_task(task_id, new_description=None, new_priority=None):
    """Edit a task's description and/or priority."""
    tasks = load_tasks()

    # Validate task ID
    for task in tasks:
        if task["id"] == task_id:
            if new_description:
                task["description"] = new_description
            if new_priority:
                valid_priorities = ["high", "medium", "low", "none"]
                if new_priority in valid_priorities:
                    task["priority"] = new_priority
                else:
                    print("⚠️ Invalid priority. Choose from: high, medium, low, none.")
                    return
            
            save_tasks(tasks)
            print(f"✅ Task {task_id} updated.")
            return

    print(f"⚠️ Task {task_id} not found.")

def add_task(description, priority="none", due_date=None):
    """Add a new task with a priority and optional due date."""
    valid_priorities = ["high", "medium", "low", "none"]
    
    if priority not in valid_priorities:
        print("⚠️ Invalid priority. Choose from: high, medium, low, none.")
        return

    # Validate due date format (YYYY-MM-DD)
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("⚠️ Invalid date format. Use YYYY-MM-DD.")
            return

    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "priority": priority,
        "due_date": due_date if due_date else "None",
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"✅ Task added: {description} (Priority: {priority}, Due: {due_date if due_date else 'None'})")
