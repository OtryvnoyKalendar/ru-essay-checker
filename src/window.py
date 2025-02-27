from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sys
# sudo apt-get install python3-tk

class Window(object):
    name = "ru-essay-checker"
    width = 1000
    height = 800
    root = Tk()

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            print("Выбранный файл:", file_path)

    def set_buttons(self):
        ai_models = ["Mistral", "GigaChat", "Perplexity"]
        pack_params = {'anchor': 'nw', 'padx': 50, 'pady': 8}

        self.cbx_ai_model = ttk.Combobox(values=ai_models)
        self.cbx_ai_model.pack(**pack_params)

        self.api_key_entry = ttk.Entry()
        self.api_key_entry.pack(**pack_params)
        
        self.btn_save = Button(text="Save API key")
        self.btn_save.pack(**pack_params)

        self.btn_choose_promt_file = Button(self.root, text="Choose promt txt file", command=self.select_file)
        self.btn_choose_promt_file.pack(**pack_params)

        self.btn_docs = Button(text="Ask an AI question")
        self.btn_docs.pack(**pack_params)

        self.btn_docs = Button(text="Read docs on Github")
        self.btn_docs.pack(**pack_params)

    def set_window(self):
        self.root.title(self.name)

        self.root.geometry(f"{self.width}x{self.height}")
        self.root.minsize(self.width//2, self.height//2)

        if sys.platform == 'win32':
            self.root.iconbitmap(default="icon.ico")
        else:
            icon = PhotoImage(file = "icon.png")
            self.root.iconphoto(False, icon)

    def set_mappings(self):
        self.root.bind('<Escape>', self.close)

    def __init__(self):
        self.set_window()
        self.set_mappings()
        self.set_buttons()

    def close(self, event=None):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

