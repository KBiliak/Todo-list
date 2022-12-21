while True:
    user_action = input("Choose the action: add, show, edit, exit or complete: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todos =[todo.strip("\n") for todo in todos]


        for index, todo in enumerate(new_todos):
            index = index + 1
            row = (f"{index}. {todo}")
            print(row)


    elif user_action.startswith("edit") :
        number = int(user_action[5:])
        print(number)
        number = number - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Edit existing todo: ")
        todos[number] = new_todo + "\n"
        print("Here is how it will be", todos)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("complete"):
        number = int(user_action[9:])

        with open("todos.txt", "r") as file:
            file.readlines()

        index = number - 1
        completed_item = todos[index].strip("\n")
        todos.pop(index)
        print(f"Item '{completed_item}' was deleted")

        with open("todos.txt", "w") as file:
            file.writelines(todos)


    elif user_action.startswith("exit"):
        print("Good bye")
        break

    else:
        print("Command is not valid.")
print("Bye")







