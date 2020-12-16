import Admin
import MainMenu
import Account


def StartUp():
    try:
        with open('data.txt', 'r'):
            print("New Key Created")
    except IOError:
        open("data.txt", "x")
        print("New Key Created")
        pass

    try:
        with open('login.txt'):
            print("Login DB Loaded")
    except IOError:
        open("login.txt", "x")
        print("Welcome to your new register system.\nNew Login Database Created")
        Admin.NewAdminAccount()


class_type = Account.Type()
class_key = Account.Key()
class_name = Account.Name()


def VerifyKey(key):
    users = []

    with open("login.txt", 'r') as FILE:
        lines = FILE.readlines()
        for i in lines:
            g = i.split(":")
            users.append(g)

    users_map = (map(list, users))

    for i in users_map:

        if key == i[0]:
            print(f'Welcome {i[1]}')
            # set key to key class
            class_key.set_key(key)

            # set name to name class
            name = i[1]
            class_name.set_name(name)

            # set type to type class
            account_type = i[2]
            class_type.set_type(account_type)

        else:
            print("Invalid login")
            Loop()


def Loop():
    while True:
        key = str(input("Please enter your 6 digit login pin: "))

        if len(key) == 6:
            VerifyKey(key)
            break

        else:
            print("Invalid Login pin")


if __name__ == '__main__':
    StartUp()
    Loop()
    MainMenu.Menu()
