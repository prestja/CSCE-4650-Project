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
                globals.printCart()
            if i == 3:
                globals.printCart()
                recentOrder = globals.getRecentOrder()
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
                amount = globals.getPriceOfRecentOrder()
                query = ("update orders set status = 'transit', type = 'card', cardType = %(cardType)s, cardNumber = %(cardNumber)s, pin = %(pin)s, billingAddress = %(billingAddress)s, amount = 9.99, placed = %(placed)s, delivered = %(delivered)s, amount = %(amount)s where orderNum = %(orderNum)s")
                globals.cursor.execute(query, {'cardType': cardType, 'cardNumber': cardNumber, 'pin': pin, 'billingAddress': billingAddress, 'placed': placed, 'delivered': delivered, 'amount': amount, 'orderNum': recentOrder[0]})
                globals.db.commit()
                print("Thank you!\nYour order will now be processed")

