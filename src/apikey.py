import settings
from dir_path import get_lower_directory_path


def _get_current_apikey_filepath() -> str:
    return get_lower_directory_path("apikeys")+settings.get_ai_model()+".apikey"


def save_apikey_to_file(key) -> bool:
    if settings.get_ai_model() in settings.ai_models[1:] and len(key) > 3:
        with open(_get_current_apikey_filepath(), "w") as apikey_file:
            print(key, end="", file=apikey_file)
        return True
    return False


def read_apikey_from_file() -> str:
    with open(_get_current_apikey_filepath(), "r") as apikey_file:
        return apikey_file.readline()

