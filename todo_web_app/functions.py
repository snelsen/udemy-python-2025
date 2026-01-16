FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as f:
        items_local = f.readlines()
        items_local = [item.strip() for item in items_local]
        return items_local
    return []

def write_todos(items_arg, filepath=FILEPATH, ):
    with open(filepath, "w") as f:
        f.writelines([item + '\n' for item in items_arg])

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
