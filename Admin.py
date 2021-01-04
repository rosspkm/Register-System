import random
import __main__
import string
import json
from lib import fdb


def rnd():
    return''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))


def NewAdminAccount(name):
    password = input("Please enter a login key: ")
    first_name = input("Please enter your first name: ")
    last_name = input("please enter your last name: ")
    email = input("please enter your email: ")
    phone_number = input("please enter your phone number(ex: xxxxxxxxxx): ")
    db = fdb.database()
    db.SelectDB(name)
    db.SelectTable("users")
    db.Insert({
        "user-account_id": rnd(),
        "firstname": first_name,
        "lastname": last_name,
        "email": email,
        "phone-number": phone_number,
        "account-type": "A",
        "password": password
    })
    print("Admin Account successfully created")


def CreateNewUser():
    password = input("Please enter a login key: ")
    first_name = input("Please enter your first name: ")
    last_name = input("please enter your last name: ")
    email = input("please enter your email: ")
    phone_number = input("please enter your phone number(ex: xxxxxxxxxx): ")
    db = fdb.database()
    db.SelectDB(__main__.restaurant.get_restaurant_name())
    db.SelectTable("users")
    db.Insert({
        "user-account_id": rnd(),
        "firstname": first_name,
        "lastname": last_name,
        "email": email,
        "phone-number": phone_number,
        "account-type": "U",
        "password": password
    })


def ChangeUserType():
    db = fdb.database()
    db.SelectDB(__main__.restaurant.get_restaurant_name())
    db.SelectTable("users")
    password = input("Please enter a login key: ")

    account = db.Get({
        "password": password
    })
    account = json.loads(account)

    print("What kind of account are you changing this to?\n[1] Admin\n[2] Manager \n[3] Employee ")
    x = input("Enter your choice [1-3]: ")

    while True:
        if x == 1:
            account_type = "A"
            break
        elif x == 2:
            account_type = "M"
            break
        elif x == 3:
            account_type = "U"
            break
        else:
            print("Invalid choice")

    db.Delete({
        "password": password
    })

    first_name = account['firstname']
    last_name = account['lastname']
    email = account['email']
    phone_number = account['phone-number']

    db.Insert({
        "user-account_id": rnd(),
        "firstname": first_name,
        "lastname": last_name,
        "email": email,
        "phone-number": phone_number,
        "account-type": account_type,
        "password": password
    })


def DeleteUser():
    db = fdb.database()
    db.SelectDB(__main__.restaurant.get_restaurant_name())
    db.SelectTable("users")
    password = input("Please enter a login key: ")

    db.Delete({
        "password": password
    })


def ShowUsers():
    print("test")


def AdminPanel():
    print("test")
