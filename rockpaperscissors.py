import random

def play():
    user=input("What's your choice? 'r' for rock 'p' for paper 's' for scissors\n").lower()
    comp=random.choice['r','p','s']

    if user==comp :
        return "It's a tie"
    if is_win(user,comp):
        return "You won!!!"
    return "You Lost!!!"



def is_win(me,u):
    if (me=='r' and u=='s') or (me=='s' and u=='p') or (me=='p' and u=='r') :
        return True

print(play())