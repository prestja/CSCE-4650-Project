import globals
import mysql.connector

class OrderMenu:
    def display(self):
        d = -0
        while d < 1:
            print("[1] View orders")
            if globals.login.employee == True:
                print("[2] Alter order")
            print("[0] Go back")
            i = int(input("Please make a selection: "))
            if i == 0:
                break
            if i == 1:
                if globals.login.employee == True:
                    print("Listing all orders in the system:")
                    query = "select * from orders"
                    globals.cursor.execute(query)
                    orders = globals.cursor.fetchall()
                    for order in orders:
                        print(order)
                else:
                    print("Listing all of your orders:")
                    query = "select * from orders where username = %(username)s"
                    globals.cursor.execute(query, {'username': globals.login.username})
                    orders = globals.cursor.fetchall()
                    for order in orders:
                        print(order)
            if i == 2:
                orderNum = int(input("Enter the order number: "))
                query = ("select * from orders where orderNum = %(orderNum)s")
                globals.cursor.execute(query, {'orderNum': orderNum})
                existingOrder = globals.cursor.fetchone()
                if existingOrder is None:
                    print("Whoops! We couldn't find that order!")
                    continue
