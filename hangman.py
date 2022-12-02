
import random
import string
from words import words

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)

    return word.upper()

def hangman():
    word=get_valid_word(words)
    valid_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used=set()
    lifeline=len(word)*2

    while len(valid_letters) > 0 and lifeline>0:
            print("you have", lifeline, "lifelines left and you have used these letters: ",' '.join(used))
            print("unused letter",' '.join(alphabet - used))
            print("type '=' to exit the game")
            word_list=[letter if letter in used else '-' for letter in word]
            print("current word:",' '.join(word_list))
            user=input("enter a letter: ").upper()
            if user=='=':
                return
            if user in alphabet - used:
                used.add(user)
                if user in valid_letters:
                    valid_letters.remove(user)
                else:
                    lifeline-=1
                    print("sorry, letter not in word")
            elif user in used:
                print("Already used this letter. try something else")
            else:
                print("Invalid character")
    #if len(used)==len(valid_letters)                
        
    if lifeline==0:
        return "You failed. better luck next time. BTW the word is " + word
    else:
        return word + " is the word and you made it!!!"

print(hangman())  