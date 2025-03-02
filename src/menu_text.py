import pandas as pd

import settings
from dir_path import get_lower_directory_path

def get_tr():
    return tr

def _get_translate_from_file(language, table_name):
    data_file = pd.read_excel(get_lower_directory_path("")+table_name)
    translate_dictionary = data_file.set_index('Dictionary key')[language].to_dict()
    return translate_dictionary

def set_language():
    tr=_get_translate_from_file(settings.get_settings()["interface_language"], "translation.xlsx")

tr=_get_translate_from_file(settings.get_settings()["interface_language"], "translation.xlsx")

