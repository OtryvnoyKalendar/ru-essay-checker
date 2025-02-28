from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sys

from menutext import *

class Window(object):
    name = "ru-essay-checker"
    width = 1000
    height = 800
    root = Tk()

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            if file_path.endswith(".txt"):
                print(t_selected_file, file_path)
            else:
                print(t_err_path_notxt)
        else:
            print(t_err_path_noselect)

    def set_widgets(self, ofr_requests, ofr_settings):
        inner_frame_init_params={"width":300, "height":200, "borderwidth":2, "relief":"ridge"}
        inner_frame_pack_params={"anchor":NW, "padx":20, "pady":15, "fill":X}
        label_pack_params={"anchor":NW, "padx":10, "pady":5}
        widget_pack_params={"anchor":NW, "padx":10, "pady":8}
        text_init_params={"height":7, "wrap":"word"}

        # settings

        ifr_select_progress = Frame(ofr_settings, **inner_frame_init_params)
        ifr_select_progress.pack(**inner_frame_pack_params)

        settings_progress_val = IntVar()
        pbr_settings_selected = ttk.Progressbar(ifr_select_progress, orient="horizontal", length=self.width//3, maximum=300,variable=settings_progress_val)
        pbr_settings_selected.pack(**widget_pack_params)
         
        lab_progress = ttk.Label(textvariable=settings_progress_val)
        lab_progress.pack(**label_pack_params)


        ifr_ai_model = Frame(ofr_settings, **inner_frame_init_params)
        ifr_ai_model.pack(**inner_frame_pack_params)

        lab_ai_models = Label(ifr_ai_model, text=t_ask_select_ai_model)
        lab_ai_models.pack(**label_pack_params)

        ai_models = ["Mistral", "GigaChat", "Perplexity"]
        cbx_ai_model = ttk.Combobox(ifr_ai_model, values=ai_models)
        cbx_ai_model.pack(**widget_pack_params)

        btn_choose_promt_file = Button(ifr_ai_model, text=t_choose_promt_file, command=self.select_file)
        btn_choose_promt_file.pack(**widget_pack_params)


        ifr_api = Frame(ofr_settings, **inner_frame_init_params)
        ifr_api.pack(**inner_frame_pack_params)

        leb_entry_api_key = Label(ifr_api, text=t_ask_entry_api_key)
        leb_entry_api_key.pack(**label_pack_params)

        ent_api_key = ttk.Entry(ifr_api)
        ent_api_key.pack(**widget_pack_params)
        
        btn_save = Button(ifr_api, text=t_save_api_key)
        btn_save.pack(**widget_pack_params)


        ifr_other = Frame(ofr_settings, **inner_frame_init_params)
        ifr_other.pack(**inner_frame_pack_params)

        leb_select_language = Label(ifr_other , text=t_ask_select_language)
        leb_select_language.pack(**label_pack_params)

        languages = ["English", "Russian", "Spanish", "German", "Japanese", "French", "Portuguese", "Italian"]
        cbx_language = ttk.Combobox(ifr_other, values=languages)
        cbx_language.pack(**widget_pack_params)

        btn_docs = Button(ifr_other, text=t_read_docs)
        btn_docs.pack(**widget_pack_params)

        # requests

        ifr_source_text = Frame(ofr_requests, **inner_frame_init_params)
        ifr_source_text.pack(**inner_frame_pack_params)

        leb_entry_source_text = Label(ifr_source_text, text=t_ask_entry_source_text)
        leb_entry_source_text.pack(**label_pack_params)

        edt_source_text = Text(ifr_source_text, **text_init_params)
        edt_source_text.pack(**widget_pack_params)


        ifr_ask_ai = Frame(ofr_requests, **inner_frame_init_params)
        ifr_ask_ai.pack(**inner_frame_pack_params)

        leb_entry_essay_text = Label(ifr_ask_ai, text=t_ask_entry_essay_text)
        leb_entry_essay_text.pack(**label_pack_params)
        
        edt_essay_text = Text(ifr_ask_ai, **text_init_params)
        edt_essay_text.pack(**widget_pack_params)

        btn_ask_ai = Button(ifr_ask_ai, text=t_btn_ai_question)
        btn_ask_ai.pack(**widget_pack_params)


        ifr_ai_answer = Frame(ofr_requests, **inner_frame_init_params)
        ifr_ai_answer.pack(**inner_frame_pack_params)

        leb_ai_answer = Label(ifr_ai_answer, text=t_ai_answer)
        leb_ai_answer.pack(**label_pack_params)
        
        edt_ai_answer = Text(ifr_ai_answer, **text_init_params)
        edt_ai_answer.pack(**widget_pack_params)

    def set_frames(self):
        outer_frame_init_params={"width":400, "height":400}
        outer_frame_pack_params={"anchor":NW, "padx":10, "pady":10}

        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill=BOTH)

        ofr_settings = Frame(self.root, **outer_frame_init_params)
        ofr_settings.pack(**outer_frame_pack_params)

        ofr_requests = Frame(self.root, **outer_frame_init_params)
        ofr_requests.pack(**outer_frame_pack_params)

        self.set_widgets(ofr_requests, ofr_settings)

        notebook.add(ofr_settings, text=t_ofr_settings)
        notebook.add(ofr_requests, text=t_ofr_requests)

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
        self.set_frames()
        # self.set_buttons()

    def close(self, event=None):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

