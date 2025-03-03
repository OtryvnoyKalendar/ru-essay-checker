import settings
from dir_path import get_lower_directory_path
from menu_text import get_tr
from apikey import read_apikey_from_file
import response.deep
import response.giga
import response.mist
from warning import show_warning

output_filename = "ai's response.md"
_input_filename = "user's full question.md"


def read_promt_from_file():
    with open(settings.get_promt_filepath(), "r", encoding='utf-8') as user_file:
        return user_file.read()


def write_users_full_question_to_file(source_text, essay_text):
    with open(get_lower_directory_path("")+_input_filename, "w", encoding='utf-8') as user_file:
        promt_string = read_promt_from_file()
        if promt_string.strip():
            print(promt_string, file=user_file)
        if source_text.strip():
            print(get_tr()["ask_entry_source_text"], file=user_file)
            print(source_text, file=user_file)
        print(get_tr()["ask_entry_essay_text"], file=user_file)
        print(essay_text, file=user_file)


def read_users_full_question_from_file() -> str:
    with open(get_lower_directory_path("")+_input_filename, "r", encoding='utf-8') as user_file:
        return user_file.read()


def read_ais_response_from_file() -> str:
    with open(get_lower_directory_path("")+output_filename, "r", encoding='utf-8') as ai_file:
        return ai_file.read()


def get_ai_response(source_text, essay_text, edt_ai_answer) -> bool:
    if not essay_text.strip():
        show_warning(get_tr()["err_essay_noentry"])
        return False
    
    configured_result = settings.is_ai_configured(True)
    if configured_result[0] == settings.ConfigStatus.CONFIGURED:
        write_users_full_question_to_file(source_text, essay_text)

        user_input = read_users_full_question_from_file()
        ai_name = settings.get_ai_model()
        output_filepath = get_lower_directory_path("")+output_filename
        api_key=read_apikey_from_file()

        if ai_name == settings.ai_models[1]: # Mistral
            response.mist.write_response_to_file(api_key, user_input, output_filepath)
        elif ai_name == settings.ai_models[2]: # GigaChat
            response.giga.write_response_to_file(api_key, user_input, output_filepath)
        elif ai_name == settings.ai_models[3]: # DeepSeek
            response.deep.write_response_to_file(api_key, user_input, output_filepath)
        else:
            show_warning(get_tr()["err_ai_currently_notsupport"])
            return False

        edt_ai_answer.delete("1.0", "end")
        edt_ai_answer.insert(index="1.0", chars=read_ais_response_from_file())
        return True
    else:
        return False

