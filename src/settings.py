from dirpaths import *
from menu_text import *

import json

ai_models = ["None", "Mistral", "GigaChat", "Perplexity"]
languages = ["English", "Russian", "Spanish", "German", "Japanese", "French", "Portuguese",
             "Italian"]


def write_settings_to_file():
    with open('settings.json', 'w', encoding='utf-8') as file:
        json.dump(params, file, ensure_ascii=False, indent=4)


def change_settings(new_params: dict[str, str]):
    for key, value in new_params.items():
        value = value.get()
        if len(value) > 0:
            params[key] = value
    write_settings_to_file()


def get_settings():
    return params


def _init_settings():
    """Инициализирует файл настроек"""
    with open(f"{get_lower_directory_path("")}settings.json", "r") as file:
        return json.load(file)


params = _init_settings()
