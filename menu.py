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
                print("[5] Manage inventory")
                print("[6] Manage orders")
                print("[7] Generate reports")
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
            if i == 0:
                quit()

class LoginMenu(BaseMenu):
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

class PartMenu (BaseMenu):
    def display(self):
        d = 0
        while d < 1:
            print("[0] Go back")
            print("[1] List parts")
            print("[2] List sets")
            i = int(input("Please make a selection: "))
            if i == 0:
                break
            if i == 1:
                query = "select * from parts"
                print("Listing all parts in the system...")
                print("---------------------\n")
                globals.cursor.execute(query)
                row = globals.cursor.fetchone()
                while row is not None:
                    print(row)
                    row = globals.cursor.fetchone()

            if i == 2:
                query = "select * from sets"
                print("Listing all sets in the system...")
                print("---------------------\n") 
                globals.cursor.execute(query)
                results = globals.cursor.fetchall()
                for r in results:
                    print(r)
                    query2 = "select * from setparts where setID = %(setID)s"
                    if r[0] is not None:
                        globals.cursor.execute(query2, {'setID': r[0]})
                        results2 = globals.cursor.fetchall()
                        for (part) in results2:
                            print("\t{}".format(part))
