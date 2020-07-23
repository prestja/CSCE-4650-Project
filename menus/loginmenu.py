import globals
import mysql.connector

class LoginMenu:
    asEmployee = 0
    def __init__(self, asEmp):
        self.asEmployee = asEmp
    def display(self):
        if self.asEmployee == 1:
            id = int(input("Enter your employee ID: "))
            pswd = input("Enter your password: ")
            query = "select * from employees where employeeID = %(employeeID)s and password = %(password)s"
            globals.cursor.execute(query, {'employeeID': id, 'password': pswd})
            result = globals.cursor.fetchone()
            if result is not None:
                print("Successfully logged in!")
                globals.login = globals.Login(id, pswd, True)
            else:
                print("Invalid username or password")
            print("")
        else:
            usr = input("Enter your username: ")
            pswd = input("Enter your password: ")
            query = "select * from customers where username = %(username)s and password = %(password)s"
            globals.cursor.execute(query, {'username': usr, 'password': pswd})
            result = globals.cursor.fetchone()
            if result is not None:
                print("Successfully logged in!")
                globals.login = globals.Login(usr, pswd, False)
            else:
                print("Invalid username or password")
            print("")
