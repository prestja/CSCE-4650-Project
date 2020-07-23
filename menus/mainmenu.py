import globals
from .loginmenu import LoginMenu
from .partmenu import PartMenu
from .ordermenu import OrderMenu

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
            else:
                print("You are logged in as {0}".format(globals.login.username))    
                print("[3] Log out")
            if globals.login is not None:
                print("[4] View items")
                print("[5] View orders")
                print("[6] View reports")
            print("[0] Exit system")
            i = int(input("Please make a selection: "))
            if i == 1:
                subMenu = LoginMenu(0)
                subMenu.display()
            if i == 2:
                subMenu = LoginMenu(1)
                subMenu.display()
            if i == 3:
                globals.login = None
            if i == 4:
                subMenu = PartMenu()
                subMenu.display()
            if i == 5:
                subMenu = OrderMenu()
                subMenu.display()
            if i == 0:
                quit()