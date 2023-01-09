import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-DO App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, value = window.read()
    print(event, value)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(value['todo'] + "\n")
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()

