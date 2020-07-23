import mysql.connector
import globals

class StoreMenu:
    def display(self):
        d = 0
        while d < 1:
            print("You are logged in as employeeID {0}".format(globals.login.username))
            print("[1] Manage employees")
            print("[2] Manage orders")
            print("[3] Manage inventory")
            print("[0] Log out")
            i = int(input("Please make a selection: "))
            if i == 0:
                globals.login = None
                break
            if i == 1:
                print("employees")
            if i == 2:
                print("orders")
            if i == 3:
                print("invetnory")