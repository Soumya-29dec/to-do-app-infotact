import pickle

TASKS_FILE = 'tasks.pkl'

def load_tasks():
    try:
        with open(TASKS_FILE, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'wb') as f:
        pickle.dump(tasks, f)

def add_task(tasks, title, description=""):
    task = {'title': title, 'description': description, 'completed': False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{i+1}. Title: {task['title']}, Status: {status}, Description: {task['description']}")

def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_index]['title']}' marked as completed.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            add_task(tasks, title, description)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks) # Show tasks to choose
            try:
                task_num = int(input("Enter the number of the task to complete: ")) - 1
                complete_task(tasks, task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
