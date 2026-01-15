import FreeSimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

label1 = sg.Text("Select Zip file:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select Destination Directory:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="directory")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Extract":
            archivepath = values["archive"]
            dest_dir = values["directory"]
            extract_archive(archivepath, dest_dir)
            window["output"].update(value="Extraction Completed!")

        case sg.WIN_CLOSED:
            break
