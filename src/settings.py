from dir_path import get_lower_directory_path
from apikey import save_apikey_to_file
import warning
import menu_text

import json
import os
from enum import Enum
from apikey import get_current_apikey_filepath

ai_models = ["None", "Mistral", "GigaChat", "DeepSeek", "Perplexity"]
languages = [
    "English",
    "Russian",
    "Spanish",
    "German",
    "Japanese",
    "French",
    "Portuguese",
    "Italian",
]
view_formats = ["Markdown", "HTML", "Console"]


def write_settings_to_file():
    with open(
        get_lower_directory_path("") + "settings.json", "w", encoding="utf-8"
    ) as file:
        json.dump(params, file, ensure_ascii=False, indent=4)


def change_settings(
    new_params: dict[str, str],
    apikey: str,
    prg_settings_selected,
    leb_selected_promt_file,
):
    # ai settings
    for key, value in new_params.items():
        value = value.get()
        if len(value) > 0:
            params[key] = value
    write_settings_to_file()
    save_apikey_to_file(apikey)

    # language
    import menu_text

    menu_text.set_language()

    # update gui
    configured_res = is_ai_configured(False)
    prg_settings_selected["value"] = 100 - int(
        configured_res[1] / configured_res[2] * 100
    )
    leb_selected_promt_file["text"] = params["promt_file"]


def get_ai_model() -> str:
    return params["ai_model"]


def get_settings():
    return params


def get_promt_filepath() -> str:
    return get_lower_directory_path("promts") + params["promt_file"]


class ConfigStatus(Enum):
    CONFIGURED = 0

    ERR_AI_MODEL_NOT_SELECT = 1
    ERR_PROMT_NOT_FOUND = 2
    ERR_APIKEY_FILE_NOT_FOUND = 3


def is_ai_configured(is_show_warning) -> (ConfigStatus, int, int):
    errors_num_max = len(list(ConfigStatus)) - 1
    errors_num = 0
    result = ConfigStatus.CONFIGURED

    if get_ai_model() not in ai_models[1:]:
        if is_show_warning:
            warning.show_warning(menu_text.get_tr()["err_ai_model_notselect"])
        errors_num += 1
        result = ConfigStatus.ERR_AI_MODEL_NOT_SELECT

    if not os.path.exists(get_promt_filepath()):
        if is_show_warning:
            warning.show_warning(menu_text.get_tr()["err_promt_notfound"])
        errors_num += 1
        result = ConfigStatus.ERR_PROMT_NOT_FOUND

    if not os.path.exists(get_current_apikey_filepath()):
        if is_show_warning:
            warning.show_warning(menu_text.get_tr()["err_apikey_file_notfound"])
        errors_num += 1
        result = ConfigStatus.ERR_APIKEY_FILE_NOT_FOUND

    return (result, errors_num, errors_num_max)


def _init_settings():
    """Инициализирует файл настроек"""
    with open(f"{get_lower_directory_path('')}settings.json", "r") as file:
        return json.load(file)


params = _init_settings()
