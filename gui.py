# Importing the functions module and PySimpleGUI library
from modules import functions
import PySimpleGUI as sg

# Creating widgets for the GUI
# A text label displaying "Type in a to-do"
label = sg.Text("Type in a to-do")
# A listbox to display the current to-dos, gets its initial values from the `get_todos()` function
# The key 'todos' is used to reference the listbox in the GUI
# The listbox does not respond to events and has a size of (45, 10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
# An input text box with the tooltip "Enter todo" and the key "todo"
input_box = sg.InputText(tooltip="Enter todo", key="todo")
# A button labeled "Add"
add_button = sg.Button("Add")
# A button labeled "Edit"
edit_button = sg.Button("Edit")

# Setting up the GUI layout
# Creating a window with the title "My To-DO App"
# The layout of the window includes the label, input_box, and add_button in the first row
# The layout includes the list_box and the edit_button in the second row
# The font used in the window is Helvetica with a size of 20
window = sg.Window('My To-DO App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button]
                           ],
                   font=('Helvetica', 20))

# Event Loop for handling user input
# Continuously checks for events and values until the window is closed
while True:
    # Returns the event (e.g. button press) and values (e.g. input in the input_box)
    event, values = window.read()
    # debugging
    print(1, event)
    print(2, values)
    print(3, values['todos'])

    if event == "Add":
        # When the "Add" button is pressed, this block of code is executed
        # Gets the current to-do list by calling the `get_todos()` function
        todos = functions.get_todos()
        # Appends the current input in the input_box to the to-do list
        todos.append(values['todo'] + "\n")
        # Writes the updated to-do list to the file by calling the `write_todos(todos)` function
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    elif event == "Edit":
        # When the "Edit" button is pressed, this block of code is executed
        # Edits the selected to-do in the list_box
        # Gets the selected to-do from the list_box by using `values['todos'][0]`
        todo_to_edit = values['todos'][0]
        # Gets the current input in the input_box
        new_todo = values['todo']
        # Gets the current to-do list by calling the `get_todos()` function
        todos = functions.get_todos()
        # Finds the index of the selected to-do in the to-do list
        index = todos.index(todo_to_edit)
        # Replaces the selected to-do with the new to-do inputted in the input_box
        todos[index] = new_todo + "\n"
        # Writes the updated to-do list to the file by calling the `write_todos(todos)` function
        functions.write_todos(todos)
        # Update the list_box with the new to-do list
        window['todos'].update(values=todos)
    elif event == "todos":
        window['todo'].update(value=values['todos'][0])
    elif event == sg.WIN_CLOSED:
        # Closes the GUI window when the x button is clicked
        break
