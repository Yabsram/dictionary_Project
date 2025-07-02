"""
from wordapi.py import _

from db.py import _

"""
from gen_api import get_response

def get_user_words():
    SENTINEL = "toyota"
    print(f"Enter words one by one. Type '{SENTINEL} when you are finished.")
    
    words = []
    while True:
        word = input("Enter a word: ").strip()

        if word.lower() == SENTINEL:
            break
        elif word.isalpha():
            words.append(word.lower())
        else:
            print("Please try to only use letters")
    
    return words

def get_valid_sentence():
    
    while True:
        sentence = input("Enter a valid sentence: ").strip()
        if len(sentence) > 1 and sentence[-1] in ".?!":
            return sentence
        else: 
            print("Invalid sentence sentence.")
    

def main():
    print(get_response("Briefly introduce yourself to the user."))
    words = get_user_words()
    sentence = get_valid_sentence()
    synonym_dict = {}
    for word in words:
        synonym_dict[word] = get_synonyms(word)
    

main()