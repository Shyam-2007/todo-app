import functions
import time
now = time.strftime("%b - %d - %Y, %H:%M")
print("the time is now:")
print("Time now: " + now)
while True:
    User_input = input("type add, edit, delete, quit:")
    todos = []
    if User_input.strip().startswith('add'):
        todos = functions.get_todos()
        todos.append(User_input[3:].strip() + "\n")
        functions.write_todos(todos)

    if User_input.strip().startswith('delete'):
        todos = functions.get_todos()
        User_input.strip()
        todos.remove(User_input[7:] + "\n")
        functions.write_todos(todos)

    if User_input.strip().startswith('edit'):
        new_todo = input("What would you like to replace it with:")
        try:
            todos = functions.get_todos()
            User_input.strip()
            todos[todos.index(User_input[5:] + "\n")] = new_todo + "\n"
            functions.write_todos(todos)
        except ValueError or IndexError:
            print("No such item exists.")

    if User_input.strip().startswith('show'):
        todos = functions.get_todos()
        i = 1
        for item in todos:
            print(str(i) + ". " + item)
            i += 1

    if User_input.strip().startswith('quit'):
        break

print("See ya later!")
