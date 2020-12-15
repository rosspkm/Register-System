import __main__
import Admin


def Menu():
    print("Main Menu: Choose from the following options")
    print("[1] New Point of sale")
    print("[2] Log out")
    account = __main__.Account()
    print(account)
    if __main__.Account == "A":
        print("[3] Admin Panel")

    choice = input("Choose an option[1-2]: ")

    if choice == '3' and __main__.Account() != "A":
        pass

    elif choice == '3' and __main__.Account() == "A":
        Admin.AdminPanel()
