import tkinter as tk
from tkinter import messagebox
from menu_text import get_tr

def check_new_message(new_message):
    if not isinstance(new_message, str):
        return get_tr()["err_translation_notfound"]
    return new_message

def show_warning(new_message):
    new_message = check_new_message(new_message)
    messagebox.showwarning(message=new_message)

def show_temporary_warning(new_message, millisecs):
    new_message = check_new_message(new_message)
    if millisecs < 10: millisecs = 10

    popup = tk.Toplevel(title=None)
    popup.geometry("400x150")
    popup.title("")

    label = tk.Label(popup, text=new_message)
    label.pack(pady=20)

    popup.after(millisecs, popup.destroy)
    for i in range(5):
        popup.update_idletasks()
        popup.update()

