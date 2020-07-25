import mysql.connector
import globals
import datetime
import time
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
                
                placed = datetime.datetime.now()
                delivered = placed + datetime.timedelta(days = 3) # Three days shipping by default
                placed.strftime('%Y-%m-%d %H:%M:%S')
                delivered.strftime('%Y-%m-%d %H:%M:%S')

                query = ("update orders set status = 'transit', type = 'card', cardType = %(cardType)s, cardNumber = %(cardNumber)s, pin = %(pin)s, billingAddress = %(billingAddress)s, amount = 9.99, placed = %(placed)s, delivered = %(delivered)s where orderNum = %(orderNum)s")
                globals.cursor.execute(query, {'cardType': cardType, 'cardNumber': cardNumber, 'pin': pin, 'billingAddress': billingAddress, 'placed': placed, 'delivered': delivered, 'orderNum': recentOrder[0]})
                globals.db.commit()
                print("Thank you!\nYour order will now be processed")

    def getPriceOfRecentOrder(self): # Returns the total of the total contents of an order, consisting of parts and/or sets
        total = 0
        recentOrder = self.getRecentOrder()
        if recentOrder is not None:
            orderNum = recentOrder [0]
            query = ("select * from orderitemset where orderNum = %(orderNum)s")
            globals.cursor.execute(query, {'orderNum': orderNum})
            setparts = globals.cursor.fetchall()
            for setpart in setparts:
                if setpart[0] is not None: # if a part
                    pquery = ("select * from parts where partID = %(partID)s")
                    globals.cursor.execute(pquery, {'partID': setpart[0]})
                    setpart = globals.cursor.fetchone()
                    total += setpart[2]
                elif setpart[1] is not None: # if a set
                    squery = ("select * from sets where setID = %(setID)s")
                    globals.cursor.execute(squery, {'setID': setpart[1]})
                    set = globals.cursor.fethcone()
                    quantity = set[2]
                    spquery = ("select * from setparts where setID = %(setID)s")
                    globals.cursor.execute(spquery, {'setID': setpart[1]})
                    setparts = globals.cursor.fetchall()
                    for setpart in setparts: # for each part in set
                        pquery = ("select * from parts where partID = %(partID)s") # find the part
                        globals.cursor.execute(pquery, {'partID': setpart[0]})
                        part = globals.cursor.fetchone()
                        total += part[2] * setpart[2] # and add its price
                        print("set {} has {} of part {} worth {} apiece".format(setpart[1], quantity, part[0], part[2]))
        return total


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
            print("Order number {} total price {}".format(orderNum, self.getPriceOfRecentOrder()))
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