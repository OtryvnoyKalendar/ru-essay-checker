from mistralai import Mistral

from warning import show_warning


def write_response_to_file(api_key, user_input, output_filepath):
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)

    try:
        chat_response = client.chat.complete(
            model = model,
            messages = [
                {
                    "role": "user",
                    "content": user_input,
                },
            ]
        )

        with open(output_filepath, 'w', encoding="utf-8") as ouput_file:
            print(chat_response.choices[0].message.content, end="", file=ouput_file)
    except Exception as e:
        show_warning(f"{e}")

