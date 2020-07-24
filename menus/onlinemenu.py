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
                recentOrder = self.getRecentOrder()
                if recentOrder is None:
                    return
                print("Please enter your billing information")
                billingAddress = input("Billing address: ")                
                cardNumber = int(input("Card Number: "))
                pin = int(input("Card PIN: "))
                print("[1] Amex")
                print("[2] MC")
                print("[3] Vista")
                print("[4] Other")
                cardType = input("Please select from the list of card providers: ")
                


    def getRecentOrder(self):
        findRecentOrder = ("select * from orders where username = %(username)s and status = 'open'")
        globals.cursor.execute(findRecentOrder, {'username': globals.login.username})
        recentOrder = globals.cursor.fetchone()
        return recentOrder

    def printCart(self):
        recentOrder = self.getRecentOrder()
        if recentOrder is None:
            print("Whoops! You don't appear to have an order.\nAdd some items to your cart to begin a new order.")
        else:
            orderNum = recentOrder[0]
            print("Order number {}".format(orderNum))
            query = ("select * from orderitemset where orderNum = %(orderNum)s")
            globals.cursor.execute(query, {'orderNum': orderNum})
            items = globals.cursor.fetchall()
            for item in items:
                if item[2] is None:
                    query = ("select * from parts where partID = %(partID)s")
                    globals.cursor.execute(query, {'partID': item[1]})
                    part = globals.cursor.fetchone()
                    print("\t{}".format(part))
                elif item[1] is None:
                    query = ("select * from sets where setID = %(setID)s")
                    globals.cursor.execute(query, {'setID': item[2]})
                    set = globals.cursor.fetchone()
                    print("\t{}".format(set))
                #print(item)