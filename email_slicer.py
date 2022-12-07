def main():
    print("Welcome to Email slicer")
    print("")
    email_id = input("Enter the email id: ")
    (username, domain) = email_id.split('@')

    (domain, extention) = domain.split('.')
    print("User Name: ", username)
    print("Domain: ", domain)
    print("Extention: ", extention )
main()
