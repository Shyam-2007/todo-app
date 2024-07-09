import FreeSimpleGUI as sg
import functions
import time

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values=functions.get_todos(), size=(45, 10), key='todos', enable_events=True)
exit_text = sg.Text(key='exit_text', )

window = sg.Window("My To-do Application",
                   layout=[[label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button, exit_text]],
                   font=('Arial', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos_arg=todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Edit":
            todo = values["todos"][0]
            new_todo = values["todo"]
            todos = functions.get_todos()
            todos[todos.index(todo)] = new_todo + "\n"
            functions.write_todos(todos_arg=todos)
            window['todos'].update(values=todos)

        case "Remove":
            todos = functions.get_todos()
            todos.remove(values["todos"] + "\n")
            functions.write_todos(todos_arg=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'Complete':
            todos = functions.get_todos()
            remove = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(remove)
            functions.write_todos(todos_arg=todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

            # !try adding later
            # window['exit_text'].update(value="Done!")
            # time.sleep(1)
            # window['exit_text'].update(value="")
