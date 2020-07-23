import mysql.connector
import globals

class OnlineMenu:
    def display(self):
        d = 0
        while d < 1:
            print("You are logged in as user {0}".format(globals.login.username))
            print("[1] View merchandise")
            print("[2] Check out")
            print("[0] Log out")
            i = int(input("Please make a selection: "))
            if i == 0:
                globals.login = None
                break
            if i == 1:
                print("merch")
            if i == 2:
                print("checkout")
        