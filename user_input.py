def get_user_input():
    SENTINEL = "q"
    # print(f"Enter words one by one. Type `{SENTINEL}` to finish.")
    words = []

    while True:
        prompt = "Enter a sentence with a _ ending in . ? or !: "
        sentence = input(prompt).strip()        
        if (
            len(sentence) > 1
            and "_" in sentence
            and sentence[-1] in ".?!"
        ):
            break
        else:
            print("Invalid sentence. Try again.")

    print(f"Enter words one by one. Type '{SENTINEL}' to finish.")
    while True:
        word = input("Enter a word: ").strip()

        if word.lower() == SENTINEL:
            break
        elif word.isalpha():
            words.append(word.lower())
        else:
            print("Please try to only use letters.")
    return sentence, words
