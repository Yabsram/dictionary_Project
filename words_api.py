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

# For isolated testing purposes 
#For a single word
# def main():
#     word = input("Enter your word: ").strip()
#    # words = [w.strip() for w in user_input.split(",")]
#     result = get_synonyms(word)
#     print(result)

# if __name__ == "__main__":
#     main() 

#For multiple words
def main():
    user_input = input("Enter your word(s) seperated by commas: ").strip()
    words = [w.strip() for w in user_input.split(",")] 

    all_synonyms = []
    for word in words:
        synonyms = get_synonyms(word)
        print(f"{word} -> {synonyms}")
        all_synonyms.extend(synonyms)
    
    print("All synonyms:")
    print(list(all_synonyms))

if __name__ == "__main__":
    main() 