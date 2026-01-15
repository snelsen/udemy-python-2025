# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete, or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todo = todo.capitalize()

        items = functions.get_todos()
        items.append(todo)
        functions.write_todos(items)

    elif user_action.startswith("show"):
        items = functions.get_todos()
        for i, item in enumerate(items):
            item = item.strip()
            print(f"{i+1}. {item.title()}")

    elif user_action.startswith("edit"):
        try:
            user_selection = int(user_action[5:])
            user_selection -= 1

            items = functions.get_todos()
            print(f"Current value: {items[user_selection]}")
            new_item = input("Enter the new value:")
            items[user_selection] = new_item
            functions.write_todos(items)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        user_selection = int(user_action[9:])
        user_selection -= 1

        items = functions.get_todos()
        try:
            if user_selection >=0 and user_selection < len(items):
                removed = items.pop(user_selection)
                print(f"Removed item: {removed.title()}")
            functions.write_todos(items)
        except IndexError:
            print("Invalid selection.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print(f"Invalid input {user_action}")

