import requests
import os

API_KEY = os.getenv("WORDSAPI_KEY")


def get_synonyms(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/synonyms"
    headers = {
         "x-rapidapi-key": API_KEY,
         "x-rapidapi-host": "wordsapiv1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    return response.json().get("synonyms", [])


def get_all_synonyms(words):
    synonym_dict = {}
    for word in words:
        synonym_dict[word] = get_synonyms(word)
    return synonym_dict
