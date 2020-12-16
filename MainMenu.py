import __main__
import Admin


def Menu():

    while True:
        print("Main Menu: Choose from the following options")
        print("[1] New Point of sale")
        print("[2] Clock in")# make clock in system
        print("[2] Log out")
        if __main__.class_type.get_type() == "A":
            print("[3] Admin Panel")

        choice = input("Choose an option[1-2]: ")

        if choice == '1':
            PointOfSale()

        elif choice == '2':
            quit()

        elif choice == '3' and __main__.class_type.get_type() != "A":
            continue

        elif choice == '3' and __main__.class_type.get_type() == "A":
            Admin.AdminPanel()

        else:
            print("Invalid choice")


def PointOfSale():
    print("empty")
