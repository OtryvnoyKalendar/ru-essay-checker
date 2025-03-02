import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
import webbrowser

from dir_path import *
from menu_text import *
import settings


class Window(object):
    name = "ru-essay-checker"
    width = 1000
    height = 800
    root = Tk()

    ai_model = tkinter.StringVar()
    promt_file = tkinter.StringVar()
    interface_language = tkinter.StringVar()
    params = {
        "ai_model": ai_model,
        "promt_file": promt_file,
        "interface_language": interface_language
    }

    def get_window(self):
        return self.root

    @staticmethod
    def open_repo_docks():
        url = "https://github.com/OtryvnoyKalendar/ru-essay-checker/blob/main/docks/README.md"
        webbrowser.open(url)

    @staticmethod
    def show_warning(message):
        messagebox.showwarning(message=message)

    def select_promt_file(self):
        self.promt_file.set(filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")],
            initialdir=get_lower_directory_path("promts")
        ))

        self.promt_file.set(os.path.basename(self.promt_file.get()))
        file_path = self.promt_file.get()
        if file_path:
            if file_path.endswith(".txt"):
                Window.show_warning(get_tr()["selected_file"] + file_path)
            else:
                Window.show_warning(get_tr()["err_path_notxt"])
        else:
            Window.show_warning(get_tr()["err_path_noselect"])
    
    def set_compboxes(self, cbx_ai_model, cbx_language):
        current_params=settings.get_settings()
        cbx_language.set(current_params["interface_language"])
        cbx_ai_model.set(current_params["ai_model"])

    def set_widgets(self, ofr_requests, ofr_settings):
        """Расстановка всех виджетов в окне"""

        inner_frame_init_params = {"width": 300, "height": 200, "borderwidth": 2, "relief": "ridge"}
        inner_frame_pack_params = {"anchor": NW, "padx": 20, "pady": 15, "fill": X}
        label_pack_params = {"anchor": NW, "padx": 10, "pady": 5}
        widget_pack_params = {"anchor": NW, "padx": 10, "pady": 8}
        text_init_params = {"height": 7, "wrap": "word"}

        # settings

        ifr_select_progress = Frame(ofr_settings, **inner_frame_init_params)
        ifr_select_progress.pack(**inner_frame_pack_params)

        settings_progress_val = IntVar()
        pbr_settings_selected = ttk.Progressbar(
            ifr_select_progress,
            orient="horizontal",
            length=self.width // 3,
            maximum=300,
            variable=settings_progress_val
        )
        pbr_settings_selected.pack(**widget_pack_params)

        lab_progress = ttk.Label(textvariable=settings_progress_val)
        lab_progress.pack(**label_pack_params)

        ifr_ai_model = Frame(ofr_settings, **inner_frame_init_params)
        ifr_ai_model.pack(**inner_frame_pack_params)

        lab_ai_models = Label(ifr_ai_model, text=get_tr()["ask_select_ai_model"])
        lab_ai_models.pack(**label_pack_params)

        cbx_ai_model = ttk.Combobox(
            ifr_ai_model,
            textvariable=self.ai_model,
            values=settings.ai_models,
            state="readonly"
        )
        cbx_ai_model.pack(**widget_pack_params)

        leb_choose_promt_file = Label(ifr_ai_model, text=get_tr()["choose_promt_file"])
        leb_choose_promt_file.pack(**label_pack_params)

        btn_choose_promt_file = Button(ifr_ai_model, text=get_tr()["search_in_filesystem"],
                                       command=self.select_promt_file)
        btn_choose_promt_file.pack(**widget_pack_params)

        leb_entry_api_key = Label(
            ifr_ai_model,
            text=get_tr()["ask_entry_api_key"]
        )
        leb_entry_api_key.pack(**label_pack_params)

        ent_api_key = ttk.Entry(
            ifr_ai_model
        )
        ent_api_key.pack(**widget_pack_params, fill=X)

        ifr_other = Frame(
            ofr_settings,
            **inner_frame_init_params
        )
        ifr_other.pack(**inner_frame_pack_params)

        leb_select_language = Label(
            ifr_other,
            text=get_tr()["ask_select_language"]
        )
        leb_select_language.pack(**label_pack_params)

        cbx_language = ttk.Combobox(
            ifr_other,
            textvariable=self.interface_language,
            values=settings.languages,
            state="readonly"
        )
        cbx_language.pack(**widget_pack_params)

        btn_docks = Button(
            ifr_other,
            text=get_tr()["read_docks"],
            command=Window.open_repo_docks
        )
        btn_docks.pack(**widget_pack_params)

        # сохраняет заданные настройки
        btn_save = Button(
            ofr_settings,
            text=get_tr()["btn_save_settings"],
            command=lambda: settings.change_settings(self.params)
        )
        btn_save.pack(**inner_frame_pack_params)

        # requests

        ifr_source_text = Frame(ofr_requests, **inner_frame_init_params)
        ifr_source_text.pack(**inner_frame_pack_params)

        leb_entry_source_text = Label(ifr_source_text, text=get_tr()["ask_entry_source_text"])
        leb_entry_source_text.pack(**label_pack_params)

        edt_source_text = scrolledtext.ScrolledText(ifr_source_text, **text_init_params)
        edt_source_text.pack(**widget_pack_params)

        ifr_ask_ai = Frame(ofr_requests, **inner_frame_init_params)
        ifr_ask_ai.pack(**inner_frame_pack_params)

        leb_entry_essay_text = Label(ifr_ask_ai, text=get_tr()["ask_entry_essay_text"])
        leb_entry_essay_text.pack(**label_pack_params)

        edt_essay_text = scrolledtext.ScrolledText(ifr_ask_ai, **text_init_params)
        edt_essay_text.pack(**widget_pack_params)

        btn_ask_ai = Button(ifr_ask_ai, text=get_tr()["btn_ai_question"])
        btn_ask_ai.pack(**widget_pack_params)

        ifr_ai_answer = Frame(ofr_requests, **inner_frame_init_params)
        ifr_ai_answer.pack(**inner_frame_pack_params)

        leb_ai_answer = Label(ifr_ai_answer, text=get_tr()["ai_answer"])
        leb_ai_answer.pack(**label_pack_params)

        edt_ai_answer = scrolledtext.ScrolledText(ifr_ai_answer, **text_init_params)
        edt_ai_answer.pack(**widget_pack_params)

        self.set_compboxes(cbx_ai_model, cbx_language)

    def set_frames(self):
        outer_frame_init_params = {"width": 400, "height": 400}
        outer_frame_pack_params = {"anchor": NW, "padx": 10, "pady": 10}

        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill=BOTH)

        ofr_settings = Frame(self.root, **outer_frame_init_params)
        ofr_settings.pack(**outer_frame_pack_params)

        ofr_requests = Frame(self.root, **outer_frame_init_params)
        ofr_requests.pack(**outer_frame_pack_params)

        self.set_widgets(ofr_requests, ofr_settings)

        notebook.add(ofr_settings, text=get_tr()["ofr_settings"])
        notebook.add(ofr_requests, text=get_tr()["ofr_requests"])

    def set_window(self):
        self.root.title(self.name)

        self.root.geometry(f"{self.width}x{self.height}")
        self.root.minsize(self.width // 2, self.height // 2)

        if sys.platform == 'win32':
            self.root.iconbitmap(default=f"{get_lower_directory_path("icons")}icon.ico")
        else:
            icon = PhotoImage(file=f"{get_lower_directory_path("icons")}icon.png")
            self.root.iconphoto(False, icon)

    def cbx_selected(self, event):
        """Изменяет значение params[key] когда выбран один из combobox`ов"""
        self.params

    def set_mappings(self):
        self.root.bind('<Escape>', self.close)

    def __init__(self):
        self.set_window()
        self.set_mappings()
        self.set_frames()

    def close(self, event=None):
        self.root.destroy()

    def run(self):
        self.root.mainloop()
