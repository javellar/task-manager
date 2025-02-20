from tasks import load_tasks, add_task, complete_task, delete_task, edit_task

def main():
    print("Welcome to Task Manager! 📝")
    while True:
        command = input("\nEnter command (add/list/complete/delete/edit/exit): ").strip().lower()

        if command == "add":
            description = input("Enter task description: ").strip()
            priority = input("Enter priority (high/medium/low/none): ").strip().lower()
            
            due_date = input("Enter due date (YYYY-MM-DD, leave blank if none): ").strip()
            due_date = due_date if due_date else None  # Ensure None is passed if blank

            add_task(description, priority, due_date)

        elif command == "list":
            tasks = load_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                show_completed = input("Show completed tasks? (yes/no): ").strip().lower()
                filtered_tasks = tasks if show_completed == "yes" else [task for task in tasks if not task["completed"]]

                print("\n📋 Task List")
                print("-" * 75)  # Table width remains 75
                print(f"{'ID':<5} {'Description':<30} {'Priority':<20} {'Due Date':<15}")  # Priority gets fixed width
                print("-" * 75)  # Divider line
                for task in filtered_tasks:
                    status = "✅" if task["completed"] else "❌"
                    priority_color = {
                        "high": "🔴",
                        "medium": "🟠",
                        "low": "🟢",
                        "none": "⚪"
                    }
                    due_date = task.get("due_date", "None")  # Default to "None" if missing
                    
                    priority_text = f"{priority_color[task['priority']]} ({task['priority']})"  # Ensuring uniform priority format
                    
                    print(f"{task['id']:<5} {status} {task['description']:<30} {priority_text:<20} {due_date:<15}")
                print("-" * 75)  # Footer divider



        elif command == "complete":
            try:
                task_id = int(input("Enter task ID to complete: "))
                complete_task(task_id)
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.")

        elif command == "delete":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.")

        elif command == "edit":
            try:
                task_id = int(input("Enter task ID to edit: "))
                new_description = input("Enter new description (leave blank to keep current): ").strip()
                new_priority = input("Enter new priority (high/medium/low/none, leave blank to keep current): ").strip().lower()

                new_description = new_description if new_description else None
                new_priority = new_priority if new_priority else None

                edit_task(task_id, new_description, new_priority)
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.")

        elif command == "exit":
            print("Goodbye! 👋")
            break

        else:
            print("⚠️ Invalid command. Try again.")

if __name__ == "__main__":
    main()
