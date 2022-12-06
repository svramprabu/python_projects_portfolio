import time

def add():
    print("Addition")
    a,b = get_input()
    ans=a + b
    print(str(a) + " + " + str(b) + " = " + str(ans))

def sub():
    print("Subtraction")
    a,b = get_input()
    ans=a - b
    print(str(a) + " - " + str(b) + " = " + str(ans))

def mul():
    print("Multiplication")
    a,b = get_input()
    ans=a * b
    print(str(a) + " * " + str(b) + " = " + str(ans))

def div():
    print("Division")
    a,b = get_input()
    ans=a / b
    print(str(a) + " / " + str(b) + " = " + str(ans))

def get_input():
    a = int(input("First number : "))
    b = int(input("Second number: "))
    return a,b
#if __init__=='__main__':
print("Welcome to the calculator")
while True:
    time.sleep(1)
    
    
    print("Choose from the options:")
    print(" press a to add \n press s to substract \n press m to multiply \n press d to divide \n press q to quit ")
    user_input = (input()).lower()
    if user_input == 'a':
        add()
    elif user_input == 's':
        sub()
    elif user_input == 'm':
        mul()
    elif user_input == 'd':
        div()
    elif user_input == 'q':
        print("Program Ended")
        quit()
    else:
        print("Invalid input try again")
        continue


