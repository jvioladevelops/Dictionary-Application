import json
from difflib import get_close_matches
#message = f"Hello {firstName} {lastName}. Whats up {when}"

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    matches = get_close_matches(w, data.keys())[0]
    if w in data:
        return data[w]
    elif w.title() in data: #if user enters texas this will return def
        return data[w.title()]
    elif w.title() in data: #if the user enters US
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        reply = input(f"Did you mean {matches} instead? Enter Y if Yes, and N if No:").upper()
        if reply == "Y":
            return data[matches]
        elif reply == "N":
            return "Your word cannot be found. Please double check it."
        else:
            return "We did not understand your entry. Please try again."
    else: 
        return "The word cannot be found. Please double check it."

word = input("Enter word: ") #defining a variable "word" based on user input

definition = translate(word) #passing that dynamic variable "word" through translate function, by redfining it as "w"

if type(definition) == list:
    for item in definition:
        print(item)
else:
    print(definition)

