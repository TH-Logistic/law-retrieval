import requests


def get_stop_words() -> list[str]:
    response = requests.get(
        "https://raw.githubusercontent.com/stopwords/vietnamese-stopwords/master/vietnamese-stopwords.txt"
    )
    return response.text.splitlines()
