from dirpaths import *
from menutext import *

import json

settings = {}

class Settings:
    ai_models = ["None", "Mistral", "GigaChat", "Perplexity"]
    languages = ["English", "Russian", "Spanish", "German", "Japanese", "French", "Portuguese", "Italian"]

    @staticmethod
    def get():
        global settings
        return settings

    @staticmethod
    def read_from_file():
        global settings

        with open(f"{get_lower_directory_path("")}settings.json", "r") as file:
            settings = json.load(file)

    @staticmethod
    def print():
        global settings
        print(settings)

    @staticmethod
    def save():
        from window import Window
        from main import get_app

        app = get_app()

        app.show_warning(t_settings_are_saved)

