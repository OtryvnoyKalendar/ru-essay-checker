import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from warning import show_warning
from tkinter import scrolledtext
import webbrowser
import tkhtmlview

from dir_path import *
from menu_text import *
import settings
import ai_request


class Window(object):
    name = "ru-essay-checker"
    width = 1200
    height = 900
    root = Tk()

    ai_model = tkinter.StringVar()
    promt_file = tkinter.StringVar()
    interface_language = tkinter.StringVar()
    view_format = tkinter.StringVar()
    params = {
        "ai_model": ai_model,
        "promt_file": promt_file,
        "interface_language": interface_language,
        "view_format": view_format
    }

    def get_window(self):
        return self.root

    @staticmethod
    def open_repo_docks():
        url = "https://github.com/OtryvnoyKalendar/ru-essay-checker/blob/main/docks/README.md"
        webbrowser.open(url)

    def save_to_clipboard(self, text_to_copy):
        self.root.clipboard_clear()
        self.root.clipboard_append(text_to_copy)
        self.root.update()

    def select_promt_file(self):
        self.promt_file.set(filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")],
            initialdir=get_lower_directory_path("promts")
        ))

        self.promt_file.set(os.path.basename(self.promt_file.get()))
        file_path = self.promt_file.get()
        if file_path:
            if file_path.endswith(".txt"):
                show_warning(get_tr()["selected_file"] + file_path)
            else:
                show_warning(get_tr()["err_path_notxt"])
        else:
            show_warning(get_tr()["err_path_notselect"])
    
    def change_by_downloaded_settings(self, cbx_ai_model, cbx_language, cbx_view_format, prg_settings_selected):
        current_params=settings.get_settings()
        cbx_language.set(current_params["interface_language"])
        cbx_ai_model.set(current_params["ai_model"])
        cbx_view_format.set(current_params["view_format"])
        
        configured_res = settings.is_ai_configured(False)
        prg_settings_selected["value"] = 100 - int(configured_res[1]/configured_res[2]*100)

    def set_widgets(self, ofr_requests, ofr_settings):
        """Расстановка всех виджетов в окне"""

        inner_frame_init_params = {"width": 300, "height": 200, "borderwidth": 2, "relief": "ridge"}
        inner_frame_pack_params = {"anchor": NW, "padx": 20, "pady": 15, "fill": X}
        label_pack_params = {"anchor": NW, "padx": 10, "pady": 5}
        widget_pack_params = {"anchor": NW, "padx": 10, "pady": 8}
        text_init_params = {"height": 9, "wrap": "word"}

        # settings

        ifr_select_progress = Frame(ofr_settings, **inner_frame_init_params)
        ifr_select_progress.pack(**inner_frame_pack_params)

        prg_settings_selected = ttk.Progressbar(
            ifr_select_progress,
            orient="horizontal",
            length=self.width // 3,
            maximum=100,
        )
        prg_settings_selected.pack(**widget_pack_params)

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

        leb_selected_promt_file = Label(ifr_ai_model, text=settings.get_settings()["promt_file"])
        leb_selected_promt_file.pack(**label_pack_params)

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

        leb_select_view_format = Label(
            ifr_other,
            text=get_tr()["ask_select_format"]
        )
        leb_select_view_format.pack(**label_pack_params)

        cbx_view_format = ttk.Combobox(
            ifr_other,
            textvariable=self.view_format,
            values=settings.view_formats,
            state="readonly"
        )
        cbx_view_format.pack(**widget_pack_params)

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
            command=lambda: settings.change_settings(self.params, ent_api_key.get(), prg_settings_selected, leb_selected_promt_file)
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


        ifr_ai_answer = Frame(ofr_requests, **inner_frame_init_params)
        ifr_ai_answer.pack(**inner_frame_pack_params)

        leb_ai_answer = Label(ifr_ai_answer, text=get_tr()["ai_answer"])
        leb_ai_answer.pack(**label_pack_params)

        edt_ai_answer = tkhtmlview.HTMLScrolledText(ifr_ai_answer, html="", **text_init_params)
        edt_ai_answer.pack(**widget_pack_params)
        
        btn_save_answer_to_clipboard = Button(
            ifr_ai_answer,
            text=get_tr()["save_to_clipboard"],
            command=lambda: self.save_to_clipboard(ai_request.read_ais_response_from_file())
        )
        btn_save_answer_to_clipboard.pack(**widget_pack_params)

        self.change_by_downloaded_settings(cbx_ai_model, cbx_language, cbx_view_format, prg_settings_selected)

        btn_ask_ai = Button(
            ifr_ask_ai,
            text=get_tr()["btn_ai_question"],
            command=lambda: ai_request.get_ai_response(edt_source_text.get("1.0", END),
                                                       edt_essay_text.get("1.0", END), edt_ai_answer)
        )
        btn_ask_ai.pack(**widget_pack_params)

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
