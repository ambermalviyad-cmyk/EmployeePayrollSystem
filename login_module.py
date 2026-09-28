# Login AND PASSWORD MODULE

def login():
    password = input("Enter password: ")

    if password == "admin123":
        print("\nLogin successful!")
        return True
    else:
        print("\nIncorrect password.")
        return False