from dirpaths import *
from menu_text import *

import json

ai_models = ["None", "Mistral", "GigaChat", "Perplexity"]
languages = ["English", "Russian", "Spanish", "German", "Japanese", "French", "Portuguese",
             "Italian"]


def change_settings(table: dict[str]) -> bool:
    for i in table:
        print(i)


def get_settings():
    return params


def _init_settings():
    """Инициализирует файл настроек"""
    with open(f"{get_lower_directory_path("")}settings.json", "r") as file:
        return json.load(file)


params = _init_settings()
