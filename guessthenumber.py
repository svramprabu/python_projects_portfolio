

import random
def guess(x):
    
    random_no=random.randint(1,x)
    guess=0

    while guess!=random_no:
        guess = int(input(f"give a number between 1 and {x} "))
        if guess > random_no:
            print("sorry, give a smaller no")
        elif guess<random_no:
            print("sorry,give a bigger no")
    print(f"Yay! you found the number correctly and it is {random_no}")

def comp_guess(x):
    low=1
    high=x
    feedback=''
    print(f"think of a nmber between {low} and {high}")
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"is {guess} too high (H), too low (L) or correct (C)").lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f" {guess} is the number your had in mind")

max=int(input("What is the maximum range from 1 to :"))
guess(max)
max=int(input("What is the maximum range from 1 to :"))
comp_guess(max)