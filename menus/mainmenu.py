import globals
import mysql.connector
from .loginmenu import LoginMenu
from .storemenu import StoreMenu
from .onlinemenu import OnlineMenu

class MainMenu:
    subMenu = None
    def display(self):
        d = 0
        while d < 1:
            i = -1
            print("LEGO Management System")
            print("---------------------\n")            
            if globals.login is None:
                print("You are not logged in!")
                print("[1] Log in as customer (online mode)")
                print("[2] Log in as employee (store mode)")
                print("[0] Exit system")
                i = int(input("Please make a selection: "))
                if i == 1:
                    subMenu = LoginMenu(0)
                    subMenu.display()
                if i == 2:
                    subMenu = LoginMenu(1)
                    subMenu.display()
                if i == 0:
                    quit()
            elif globals.login is not None:
                if globals.login.employee is True:
                    subMenu = StoreMenu()
                    subMenu.display()
                else:
                    subMenu = OnlineMenu()
                    subMenu.display()
                    