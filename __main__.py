# Username: rQl2YoK6Wc
# Database name: rQl2YoK6Wc
# Password: KymKNAw4LO
# Server: remotemysql.com
# Port: 3306

import mysql.connector
import os
import MainMenu
import Admin


class User:
    def __init__(self, x):
        self.status = ""
        self._users = []
        self._key = x

    def FindUser(self):
        with open("login.txt", 'r') as FILE:
            lines = FILE.readlines()
            for x in lines:
                x = x.split(":")
                self._users.append(x)
        users = (map(list, self._users))
        for i in users:
            status = i[2]
            if self._key == i[0]:
                print(f'Welcome {i[1]}')
                Name = i[1]
                User.AccountType(status)
                return Name
            else:
                print("Invalid login")
                StartUp()

    def AccountType(self, status):
        self.status = status
        return self.status


def StartUp():
    if __name__ == '__main__':
        try:
            with open('data.txt', 'r') as f:
                print("New Key Created")
        except IOError:
            file = open("data.txt", "x")
            print("New Key Created")
            pass

        try:
            with open('login.txt') as f:
                print("Login DB Loaded")
        except IOError:
            file = open("login.txt", "x")
            print("Welcome to your new register system.\nNew Login Database Created")
            Admin.NewAdminAccount()

        while True:
            key = str(input("Please enter your 6 digit login key: "))
            user = User(key)
            name = user.FindUser
            Account()
            return name


def Account():
    account = User.AccountType
    print(f"Account type {account}")
    return account


StartUp()
MainMenu.Menu()
