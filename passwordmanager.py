
#in cmd line type pip install cryptography before proceeding
from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: #her wb means write in bytes
        key_file.write(key) '''

#write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


#master_pwd = input("What is the dummy password? ")
key = load_key() #+ master_pwd.encode()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User: ",user,"\n","Password: ", fer.decrypt(passw.encode()).decode())
def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f: #a means append i.e to add to the exiting one if exits else create one / w means write which wil overwrite r means read mode
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n")

while True:
    print("would u like to add creds or view existing ones? ")
    mode = input("type (view/add) or press q to quit \n").lower()

    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid option")
        continue