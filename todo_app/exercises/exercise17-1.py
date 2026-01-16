import FreeSimpleGUI as sg
from converters import convert

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")
label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output")

window = sg.Window("Converter",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button, output_label]],)

while True:
    event, values = window.read()
    match event:
        case "Convert":
            feet = window["feet"].Get()
            inches = window["inches"].Get()
            meters = convert(feet, inches)
            window["output"].update(f"{meters:1.3f} m")
        case sg.WIN_CLOSED:
            break


window.read()
window.close()
