todo_list = []
continue_program = True

while continue_program:

    print("\n--- To-Do List Manager ---")
    print("1. Add a task")
    print("2. Display tasks")
    print("3. Remove a task")
    print("4. Mark a task as completed")
    print("5. Mark a task as pending")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == '1':  # Add a task
        task_name = input("Enter the task name: ")
        task = {"task": task_name, "status": "pending"}
        todo_list.append(task)
        print(f'Added task: "{task_name}"')

    elif choice == '2':  # Display tasks
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(todo_list, 1):
                status = "✔" if task["status"] == "completed" else "✗"
                print(f"{index}. {task['task']} [{status}]")

    elif choice == '3':  # Remove a task
        identifier = input("Enter the task number or name to remove: ")
        if identifier.isdigit():  # Treat as index if input is a number
            index = int(identifier) - 1
            if 0 <= index < len(todo_list):
                removed_task = todo_list.pop(index)
                print(f'Removed task: "{removed_task["task"]}"')
            else:
                print("Invalid task number.")
        else:  
            for task in todo_list:
                if task["task"].lower() == identifier.lower():
                    todo_list.remove(task)
                    print(f'Removed task: "{task["task"]}"')
                    break
            else:
                print("Task not found.")

    elif choice == '4': 
        identifier = input("Enter the task number or name to mark as completed: ")
        if identifier.isdigit():  
            index = int(identifier) - 1
            if 0 <= index < len(todo_list):
                todo_list[index]["status"] = "completed"
                print(f'Marked task "{todo_list[index]["task"]}" as completed.')
            else:
                print("Invalid task number.")
        else:  # Treat as task name
            for task in todo_list:
                if task["task"].lower() == identifier.lower():
                    task["status"] = "completed"
                    print(f'Marked task "{task["task"]}" as completed.')
                    break
            else:
                print("Task not found.")

    elif choice == '5':  
        identifier = input("Enter the task number or name to mark as pending: ")
        if identifier.isdigit():  
            index = int(identifier) - 1
            if 0 <= index < len(todo_list):
                todo_list[index]["status"] = "pending"
                print(f'Marked task "{todo_list[index]["task"]}" as pending.')
            else:
                print("Invalid task number.")
        else:  
            for task in todo_list:
                if task["task"].lower() == identifier.lower():
                    task["status"] = "pending"
                    print(f'Marked task "{task["task"]}" as pending.')
                    break
            else:
                print("Task not found.")

    elif choice == '6':  
        print("Exiting the To-Do List Manager. Goodbye!")
        break

    else:
        print("Invalid option, please choose again.")