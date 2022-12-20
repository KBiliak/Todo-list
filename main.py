
while True:
    user_action = input("Choose the action: add, show, edit, exit or complete: ")
    user_action = user_action.strip()

    match user_action:
        case "add":

            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "show":

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todos =[todo.strip("\n") for todo in todos]


            for index, todo in enumerate(new_todos):
                index = index + 1
                row = (f"{index}. {todo}")
                print(row)


        case "edit":
            number = int(input("Enter the number of todo: "))
            number = number - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Edit existing todo: ")
            todos[number] = new_todo + "\n"
            print("Here is how it will be", todos)

            with open("todos.txt", "w") as file:
                file.writelines(todos)



        case "exit":
            print("Good bye")
            break

        case "complete":
            nums = int(input("Enter the number of todo to complete task: "))

            with open("todos.txt", "r") as file:
                file.readlines()


            completed_item = todos.pop(nums - 1).strip("\n")
            print(f"Item '{completed_item}' was deleted")

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case _:
            print("Unknown command")
        # case "complete":






