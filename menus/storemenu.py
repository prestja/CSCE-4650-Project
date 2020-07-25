import mysql.connector
import globals
from .employeemenu import EmployeeMenu
from .ordermenu import OrderMenu
from .reportmenu import ReportMenu
from .onlinemenu import OnlineMenu

class StoreMenu:
    def display(self):
        d = 0
        while d < 1:
            print("You are logged in as employeeID {0}".format(globals.login.username))
            print("[1] Make sales")
            print("[2] Manage employees")
            print("[3] Manage orders")
            print("[4] Manage inventory")
            print("[5] Generate reports")
            print("[0] Log out")
            i = int(input("Please make a selection: "))
            if i == 0:
                globals.login = None
                break
            if i == 1:
                subMenu = OnlineMenu()
                subMenu.display()
            if i == 2:
                subMenu = EmployeeMenu()
                subMenu.display()
            if i == 3:
                subMenu = OrderMenu()
                subMenu.display()
            if i == 4:
                print("invetnory")
            if i == 5:
                subMenu = ReportMenu()
                subMenu.display()
