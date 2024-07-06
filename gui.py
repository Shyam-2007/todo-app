import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todos")
add_button = sg.Button("Add")
edit_button = sg.Button("Remove")
window = sg.Window("My To-do Application",
                   layout=[[label, input_box, add_button, edit_button]],
                   font=('Arial', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todos"] + "\n")
            functions.write_todos(todos_arg=todos)

        case "Remove":
            todos = functions.get_todos()
            todos.remove(values["todos"] + "\n")
            functions.write_todos(todos_arg=todos)

        case sg.WIN_CLOSED:
            break
