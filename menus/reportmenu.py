import mysql.connector
import datetime
import time
import globals

class ReportMenu:
    def display(self):
        d = 0
        while d < 1:
            print("[1] Daily Report")
            print("[2] Weekly Report")
            print("[3] Monthly Report")
            print("[0] Go back")
            i = int(input("Please make a selection: "))
            query = ("select * from orders where placed between %(then)s and %(now)s")
            now = datetime.datetime.now()
            if i == 0: # return
                break
            if i == 1: # daily
                then = now - datetime.timedelta(days = 1)
            elif i == 2: # weekly
                then = now - datetime.timedelta(days = 7)
            elif i == 3: # monthly
                then = now - datetime.timedelta(days = 30)
            now.strftime('%Y-%m-%d %H:%M:%S')
            then.strftime('%Y-%m-%d %H:%M:%S')
            globals.cursor.execute(query, {'then': then, 'now': now})
            orders = globals.cursor.fetchall()
            count = 0
            for order in orders:
                count = count + 1
                print(order) 
            print("There have been {0} orders within  this timespawn".format(count))
            
