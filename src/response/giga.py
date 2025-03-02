from gigachat import GigaChat

from warning import show_warning


def write_response_to_file(api_key, user_input, output_filepath):
    model = GigaChat(
        credentials=api_key,
        scope="GIGACHAT_API_PERS",
        model="GigaChat",
        verify_ssl_certs = False,
    )

    try:
        with open(output_filepath, 'w', encoding="utf-8") as ouput_file:
            for chunk in model.stream(user_input):
                print(chunk.choices[0].delta.content, end="", flush=True, file=ouput_file)
    except Exception as e:
        show_warning(f"{e}")

