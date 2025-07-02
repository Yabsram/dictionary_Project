from gen_api import complete_sentence
from words_api import get_all_synonyms
from user_input import get_user_input
from db_utils import store_synonyms, fetch_all_synonyms as load_from_db
from setup_db import init_db


def main():
    init_db()
    sentence, user_words = get_user_input()
    synonym_dict = get_all_synonyms(user_words)

    store_synonyms(synonym_dict, sentence)
    db_synonyms = load_from_db(sentence)

    completed = complete_sentence(sentence, db_synonyms)
    print("\nSuggested sentence completion: ")
    print(completed)

if __name__ == "__main__":
    main()