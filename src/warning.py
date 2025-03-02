from tkinter import messagebox
from menu_text import get_tr

def show_warning(new_message):
    if not isinstance(new_message, str):
        new_message = get_tr()["err_translation_notfound"]
    messagebox.showwarning(message=new_message)

