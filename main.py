import sys
from gen_api import complete_sentence
from words_api import get_all_synonyms
from user_input import get_user_input
from db_utils import store_synonyms, fetch_all_synonyms 
from db_utils import print_entire_table, clear_table_allwords
from setup_db import init_db


def main():
    while True:
        nav = input("\nWhat would you like to do? Select a number below.\n"
                    "1 - Find a word\n"
                    "2 - View synonym history\n"
                    "3 - Clear synonym history\n"
                    "0 - Terminate program\n"
                    "Enter choice: ").strip()
        if nav == "1":
            # Finding synonyms
            init_db()
            sentence, user_words = get_user_input()
            synonym_dict = get_all_synonyms(user_words)

            store_synonyms(synonym_dict, sentence)
            db_synonyms = fetch_all_synonyms(sentence)

            completed = complete_sentence(sentence, db_synonyms)
            print("\nSuggested sentence completion: ")
            print(completed)
        elif nav == "2":
            # View synonym history
            print_entire_table()
        elif nav == "3":
            # Clear synonym history
            while True:
                msg = ("Are you sure you want to clear synonym "
                "history? (y/n): ")
                ready = input(msg)  
                if ready == "y":
                    clear_table_allwords()
                    break
                elif ready == "n":
                    break
                else:
                    print("Invalid input. Please select y (yes) "
                    "or n (no).")
        elif nav == "0":
            # Exiting the program
            print("Exiting program.")
            sys.exit(0)
        else:
            print("Invalid input. Please enter 1, 2, 3, or 0.")


if __name__ == "__main__":
    print("Welcome to What's on the Tip of Your Tongue!")
    main()
