def NewAdminAccount():
    code = input("Please enter a 6 digit code for your new admin login: ")
    first_name = input("Please enter your first name: ")
    last_name = input("please enter your last name: ")
    with open("login.txt", "w") as FILE:
        FILE.write(f"{code}:{first_name} {last_name}: A")
    print("Admin Account successfully created")


def CreateNewUser():
    print("test")


def AdminPanel():
    print("test")