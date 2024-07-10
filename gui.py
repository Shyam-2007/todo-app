import FreeSimpleGUI as sg
import functions
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt") as file:
        pass

clock = sg.Text('', key='clock')
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button(image_source="add.png", size=2,
                       mouseover_colors="LightBlue2",
                       tooltip="Click to add a todo", key='Add')
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source="complete.png", tooltip="Click to remove the finished todo",
                            key="Complete")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values=functions.get_todos(), size=(45, 10), key='todos', enable_events=True)
exit_text = sg.Text(key='exit_text', )

window = sg.Window("My To-do Application",
                   layout=[[label],
                           [clock],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button, exit_text]],
                   font=('Arial', 20))

while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(time.strftime("%b - %d - %Y, %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            try:
                todos = functions.get_todos()
                todos.append(values["todo"] + "\n")
                functions.write_todos(todos_arg=todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except values['todo'] == ' ':
                sg.popup("Please type an item first!", font=("Helvetica", 20))

        case "Edit":
            try:
                todo = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.get_todos()
                todos[todos.index(todo)] = new_todo + "\n"
                functions.write_todos(todos_arg=todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first!", font=("Helvetica", 20))

        case "Remove":
            try:
                todos = functions.get_todos()
                todos.remove(values["todos"] + "\n")
                functions.write_todos(todos_arg=todos)
            except IndexError:
                sg.popup("Please select an item first!", font=("Helvetica", 20))

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'Complete':
            try:
                todos = functions.get_todos()
                remove = values['todos'][0]
                todos.remove(remove)
                functions.write_todos(todos_arg=todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first!", font=("Helvetica", 20))

        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

            # !try adding later
            # window['exit_text'].update(value="Done!")
            # time.sleep(1)
            # window['exit_text'].update(value="")
