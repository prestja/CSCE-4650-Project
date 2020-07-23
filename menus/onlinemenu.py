import mysql.connector
import globals
from .partmenu import PartMenu

class OnlineMenu:
    def display(self):
        d = 0
        while d < 1:
            print("You are logged in as user {0}".format(globals.login.username))
            print("[1] View merchandise")
            print("[2] View cart")
            print("[3] Check out")
            print("[0] Log out")
            i = int(input("Please make a selection: "))
            if i == 0:
                globals.login = None
                break
            if i == 1:
                subMenu = PartMenu()
                subMenu.display()
            if i == 2:
                self.printCart()
            if i == 3:
                self.printCart()
    def printCart(self):
        findRecentOrder = ("select * from orders where username = %(username)s and status = 'open'")
        globals.cursor.execute(findRecentOrder, {'username': globals.login.username})
        recentOrder = globals.cursor.fetchone()
        if recentOrder is None:
            print("Whoops! You don't appear to have an order.\nAdd some items to your cart to begin a new order.")
        else:
            orderNum = recentOrder[0]
            print("Order number {}".format(orderNum))
            query = ("select * in orderitemset where orderNum = %(orderNum)s")
            globals.cursor.execute(query, {'orderNum': orderNum})
            items = globals.cursor.fetchall()
            for item in items:
                print(item)