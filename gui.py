from modules import functions
import PySimpleGUI as sg
import time

sg.theme("DarkBlack")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


window = sg.Window('My To-DO App',
                   layout=[[clock],
                           [label, add_button, edit_button,complete_button],
                           [input_box],
                           [list_box],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b, %d, %Y %H:%M:%S"))

    if event == "Add":
        todos = functions.get_todos()
        todos.append(values['todo'] + "\n")
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value="")
    elif event == "Edit":
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
    elif event == "Complete":
        try:
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            index = todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        except IndexError:
            sg.popup("Please select an item first.", font=("Helvetica", 20))
    elif event == "Exit":
        break
    elif event == "todos":
        window['todo'].update(value=values['todos'][0])
    elif event == sg.WIN_CLOSED:
        break
