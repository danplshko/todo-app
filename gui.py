from modules import functions
import PySimpleGUI as sg
import time

sg.theme("DarkBlack")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
input_box = sg.InputText(tooltip="Enter todo", key="todo")

add_button = sg.Button(key="add", image_source="icons/add.png",
                       tooltip="Add", mouseover_colors="Grey")
edit_button = sg.Button(key="edit", image_source="icons/edit.png",
                        tooltip="Edit", mouseover_colors="Grey")
complete_button = sg.Button(key="complete", image_source="icons/done.png",
                            tooltip="Complete", mouseover_colors="Grey")
exit_button = sg.Button(key="exit", image_source="icons/exit.png",
                        tooltip="Exit", mouseover_colors="Grey")

window = sg.Window('My To-DO App',
                   layout=[[clock],
                           [label, add_button, edit_button, complete_button],
                           [input_box],
                           [list_box],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b, %d, %Y %H:%M:%S"))

    if event == "add":
        todos = functions.get_todos()
        todos.append(values['todo'] + "\n")
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value="")
    elif event == "edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        except IndexError:
            sg.popup("Please select an item first.", font=("Helvetica", 20))
    elif event == "complete":
        try:
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            index = todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        except IndexError:
            sg.popup("Please select an item first.", font=("Helvetica", 20))
    elif event == "exit":
        break
    elif event == "todos":
        window['todo'].update(value=values['todos'][0])
    elif event == sg.WIN_CLOSED:
        break
