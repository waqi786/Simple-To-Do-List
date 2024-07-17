def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        tasks.pop(task_num - 1)
        print("Task removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def todo_list():
    tasks = []
    while True:
        print("\nTo-Do List")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    todo_list()