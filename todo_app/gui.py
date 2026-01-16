import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text(key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do", key="todo")
add_button = sg.Button(key="Add", size=2, image_source="add.png",
                       mouseover_colors="lightBlue2", tooltip="Add a To-Do")
list_box = sg.Listbox(values=functions.get_todos(),
                      enable_events=True,
                      key="todos",
                      size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button(key="Complete", size=2, image_source="complete.png",
                            mouseover_colors="lightBlue2", tooltip="Complete To-Do")
exit_button = sg.Button("Exit")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window("My To-Do App",
                   layout=layout,
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"]
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                selected_todo = values["todos"][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(selected_todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))
        case "todos":
            window['todo'].update(value=values["todos"][0])

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()