from functions import get_todo,write_todo
import time

now = time.strftime("%b %d, %Y %H:%M")
print("It is",now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todo("todos.txt")
        todos.append(todo + '\n')
        write_todo("todos.txt",todos)
    elif user_action.startswith("show"):
        todos = get_todo("todos.txt")

        # new_todos = [item.strip('\n') for item in todos] --- list comprehension method

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")
    elif user_action.startswith("complete"):
        try:
            num = int(user_action[9:])
            todos = get_todo("todos.txt")
            removed_todo = todos.pop(num - 1)
            removed_todo = removed_todo.strip('\n')
            write_todo("todos.txt",todos)
            print(f"Todo '{removed_todo}' has been removed.")
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("edit"):
        try:
            num = int(user_action[5:])
            num = num - 1
            todos = get_todo("todos.txt")
            new_todo = input("Enter new todo: ")
            todos[num] = new_todo + '\n'
            write_todo("todos.txt",todos)
        except ValueError:
            print("Your command is not valid,please enter the number of todo you want to edit!")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Please give a valid command")

print("Bye!")
