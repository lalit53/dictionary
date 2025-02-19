import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, N if no."  % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please check again."
        else:
            return "The word does not exist"
    else:
        return "The word doesn't exist."

word = input("Enter word:")


print(translate(word))