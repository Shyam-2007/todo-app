def get_todos(filename="todos.txt"):
    """gets todos from the text file"""
    with open(filename , 'r') as todos:
        todos_local = todos.readlines()
    return todos_local


def write_todos(todos_arg, filename="todos.txt"):
    """Writes the todos in the text file"""
    with open(filename, 'w') as file:
        file.writelines(todos_arg)


FILEPATH = "Hello"
