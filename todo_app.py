# todo_app.py
# Simple Command-Line To-Do List App

tasks = []

def show_menu():
    print("\n=== 📝 Python To-Do List App ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print("✅ Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✔️ Done" if t["done"] else "❌ Pending"
        print(f"{i}. {t['task']} - {status}")

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        tasks[num - 1]["done"] = True
        print("🎉 Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid input. Try again.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"🗑️ Deleted: {removed['task']}")
    except (ValueError, IndexError):
        print("Invalid input. Try again.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Goodbye! Stay productive.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
