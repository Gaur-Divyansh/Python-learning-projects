while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        with open("todos.txt", 'r') as file:
            todos = file.readlines()
        todos.append(todo + '\n')
        with open("todos.txt", 'w') as file:
            file.writelines(todos)
    elif user_action.startswith("show"):
        with open("todos.txt", 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos] --- list comprehension method

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")
    elif user_action.startswith("complete"):
        try:
            num = int(user_action[9:])
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            removed_todo = todos.pop(num - 1)
            removed_todo = removed_todo.strip('\n')
            with open("todos.txt", 'w') as file:
                file.writelines(todos)
            print(f"Todo '{removed_todo}' has been removed.")
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("edit"):
        try:
            num = int(user_action[5:])
            num = num - 1
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            new_todo = input("Enter new todo: ")
            todos[num] = new_todo + '\n'
            with open("todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid,please enter the number of todo you want to edit!")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Please give a valid command")

print("Bye!")
