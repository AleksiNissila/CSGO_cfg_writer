import tkinter as tk
import tkinter.filedialog
from tkinter import *
from tkinter import ttk
import cfg_writer
import json

class Gui:
    def __init__(self, root):
        self.root = root
        self.init_gui()

    def init_gui(self):
        """
        Function to initiate the GUI, including all elements and properties of it
        :return: nothing
        """
        # Initialize the folder
        self.selected_folder = cfg_writer.init_path()

        self.file_button = tk.Button(self.root, text="Select file location", command=self.get_file_name, width=20)

        self.cmd_box = ttk.Combobox(self.root, width=25)
        self.update_cmd_combobox()
        self.cmd_box.bind("<Return>", self.process_input)
        self.cmd_box.bind("<KeyRelease>", self.check_cmd_input)

        self.ok_button = tk.Button(self.root, text="Ok", width=20)
        self.ok_button.bind("<Button>", self.process_input)

        self.info_box = tk.Text(self.root, height=15, width=65, state=DISABLED)
        self.add_text_to_info_box(cfg_writer.init_path(), 'black')
        self.info_box.tag_config('gray', foreground='gray')
        self.info_box.tag_config('black', foreground='black')

        self.file_button.grid(row=2, column=0, ipadx= 5, ipady=5)
        self.ok_button.grid(row=1, column=0, ipadx = 5, ipady = 5)
        self.cmd_box.grid(row=0, column=0, columnspan=1, padx = 5)
        self.info_box.grid(row=0, rowspan=3, column=1, pady = 5, padx = 5)

        self.root.resizable(False, False)

    def add_text_to_info_box(self, text, tag):
        """
        Function for adding text to GUI text box
        :param text: text to be added to GUI text box
        :param tag: Color of the text
        :return: nothing
        """
        self.info_box.config(state=NORMAL)
        # Change the color of older text to gray
        self.info_box.replace("0.0", tkinter.END, self.info_box.get("0.0", tkinter.END), 'gray')
        # Insert new text
        self.info_box.insert(tkinter.END, text + '\n', tag)
        self.info_box.config(state=DISABLED)


    def get_file_name(self):
        """
        Function for selecting cfg file location. Folder (which contains the cfg-file)
        is selected, hence the function name.
        :return: nothing
        """
        self.selected_file = tkinter.filedialog.askopenfilename()
        self.add_text_to_info_box(self.selected_file, 'black')
        cfg_writer.update_path(self.selected_file)

    def process_input(self, event):
        """
        Function for getting user input, and sending it to be processed
        :param event: Event that triggers this function. Pressing enter or the 'ok'-button
        :return: nothing
        """
        input_text = self.cmd_box.get()
        if input_text:
            self.add_text_to_info_box(input_text, 'black')
            cfg_writer.process_input_commands(self.selected_folder, input_text, self.info_box, self)
            self.cmd_box.set('')
        else:
            pass

    def update_cmd_combobox(self):
        """
        Function for adding new command to a list of commands
        :return: nothing
        """
        self.cmd_box.configure(values=list(cfg_writer.cmd_list))

    def check_cmd_input(self, event):
        value = event.widget.get()

        if value == '':
            self.cmd_box.configure(values=list(cfg_writer.cmd_list))
        else:
            data = []
            for item in list(cfg_writer.cmd_list):
                if value.lower() in item.lower():
                    data.append(item)

            self.cmd_box.configure(values=data)