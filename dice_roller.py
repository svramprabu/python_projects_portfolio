import string
import random



def generate_dice_roll():
    

    Dice1 = random.randint(1,6)
    Dice2 = random.randint(1,6)
   

    
    print(f"Dice Rolled: {Dice1} and {Dice2}")

while True:
    option = input("Do you want to roll: (Y/N) ").lower()
    if option == 'y':
        generate_dice_roll()
    elif option == 'n':
        print("Thank you for using the program.")
        quit()
    else:
        print("Invalid option, Try again")