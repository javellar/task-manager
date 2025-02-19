from tasks import load_tasks, add_task, complete_task, delete_task

def main():
    print("Welcome to Task Manager! 📝")
    while True:
        command = input("\nEnter command (add/list/complete/delete/exit): ").strip().lower()

        if command == "add":
            description = input("Enter task description: ").strip()
            priority = input("Enter priority (high/medium/low/none): ").strip().lower()
            add_task(description, priority)

        elif command == "list":
            tasks = load_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nTasks:")
                for task in tasks:
                    status = "✅" if task["completed"] else "❌"
                    priority_color = {
                        "high": "🔴",
                        "medium": "🟠",
                        "low": "🟢",
                        "none": "⚪"
                    }
                    print(f"{task['id']}. {status} {task['description']} {priority_color[task['priority']]} ({task['priority']})")

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

        elif command == "exit":
            print("Goodbye! 👋")
            break

        else:
            print("⚠️ Invalid command. Try again.")

if __name__ == "__main__":
    main()

