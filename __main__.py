import Admin
import MainMenu
import Classes
from lib import fdb
import os
import json


def StartUp():
    if os.path.exists(f"config.yaml"):
        with open('config.yaml', 'r') as file:
            data = file.read()
            js = json.loads(data)
            for field, value in js.items():
                if field == "restaurant":
                    restaurant.set_restaurant_name(value)

    else:
        restaurant_name = input("Please enter your restaurant name: ")
        open(f'config.yaml', 'a')
        with open(f'config.yaml', 'a') as FILE:
            data = json.dumps({"restaurant": str(restaurant_name)}, indent=4)
            FILE.write(data)

    if os.path.isdir(f"./databases/{restaurant.get_restaurant_name()}"):
        pass

    else:
        db = fdb.Structure()
        db.Create(restaurant.get_restaurant_name())
        tables = ["data", "items", "users", "time-card"]
        data_tables = ["transaction-account_id", "items", "price", "user-account_id"]
        item_tables = ["item-account_id", "item-name", "price"]
        login_items = ["user-account_id", "password", "firstname", "lastname", "email", "phone-number", "account-type"]
        timecard_items = ["user-account_id", "clock-in", "clock-out"]

        db.AddTable(restaurant.get_restaurant_name(), tables)
        db.AddField(restaurant.get_restaurant_name(), "data", data_tables)
        db.AddField(restaurant.get_restaurant_name(), "items", item_tables)
        db.AddField(restaurant.get_restaurant_name(), "users", login_items)
        db.AddField(restaurant.get_restaurant_name(), "time-card", timecard_items)

        Admin.NewAdminAccount(restaurant.get_restaurant_name())


def Loop():
    while True:
        key = str(input("Please enter your login key: "))

        db = fdb.database()
        db.SelectDB(restaurant.get_restaurant_name())
        db.SelectTable("users")
        try:

            account = db.Get({"password": key})
            if account is None:
                continue
            else:
                acct_key.set_key(account['password'])
                acct_name.set_name(account['firstname'])
                acct_type.set_type(account['account-type'])
                acct_id.set_id(account['user-id'])

        except IOError:
            Loop()

acct_type = Classes.Type()
acct_name = Classes.Name()
acct_key = Classes.Key()
acct_id = Classes.Id()
restaurant = Classes.Restaurant_Name()

if __name__ == '__main__':
    StartUp()
    Loop()
    MainMenu.Menu()
