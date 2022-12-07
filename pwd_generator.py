import string
import random

characters = list(string.ascii_letters)
numbers = list( string.digits) 
symbols = list ("!@#$%&*" )

def generate_password():
    pass_length = int(input("Enter the length of the password: "))
    

    random.shuffle(characters)
    random.shuffle(numbers)
    random.shuffle(symbols)

    password = []

    for x in range(pass_length-2):
        password.append(random.choice(characters))
    password.append(random.choice(numbers))
    password.append(random.choice(symbols))

    random.shuffle(password)

    password= "".join(password)
    print(password)

while True:
    option = input("Do you want to print a new password: (Y/N) ").lower()
    if option == 'y':
        generate_password()
    elif option == 'n':
        print("Thank you for using the program.")
        quit()
    else:
        print("Invalid option, Try again")