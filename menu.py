import globals

class BaseMenu:
    def display(self):
        pass
class MainMenu(BaseMenu):
    subMenu = None
    def display(self):
        d = 0
        while d < 1:
            i = -1
            print("LEGO Management System")
            print("You are not logged in!")
            print("---------------------\n")
            print("[1] Log in as customer (online mode)")
            print("[2] Log in as employee (store mode)")
            print("[3] Exit system")
            i = int(input("Please make a selection: "))
            if i == 1:
                subMenu = LoginMenu(0)
                subMenu.display()
            if i == 2:
                subMenu = LoginMenu(1)
                subMenu.display()
            if i == 3:
                quit()

class LoginMenu(BaseMenu):
    asEmployee = 0

    def __init__(self, asEmp):
        self.asEmployee = asEmp

    def display(self):
        if self.asEmployee == 1:
            print("Login as employee")
            id = input("Enter your employee ID: ")
            pswd = input("Enter your password: ")
        else:
            print ("Login as customer")
            usr = input("Enter your username: ")
            pswd = input("Enter your password: ")
            query = "select * from customers where username = %(username)s"
            for result in globals.cursor.execute(query, {'username': usr}, multi=True):
                print("result")
