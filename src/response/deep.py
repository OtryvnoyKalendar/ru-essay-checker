from openai import OpenAI

from warning import show_warning


def write_response_to_file(api_key, user_input, output_filepath):
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": user_input},
            ],
            stream=False
        )

        with open(output_filepath, 'w', encoding="utf-8") as ouput_file:
            print(response.choices[0].message.content, end="", file=ouput_file)
    except Exception as e:
        show_warning(f"{e}")

