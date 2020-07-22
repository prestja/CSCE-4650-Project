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
                print("[5] View orders")
                print("[6] View reports")
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
            if i == 5:
                subMenu = OrderMenu()
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

class OrderMenu (BaseMenu):
    def display(self):
        d = -0
        while d < 1:
            print("[0] Go back")
            print("[1] View orders")
            print("[2] Alter order")
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
                pass

class PartMenu (BaseMenu):
    def display(self):
        d = 0
        while d < 1:
            print("[0] Go back")
            print("[1] View parts")
            print("[2] View sets")
            print("[3] Add item to order")
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
                sets = globals.cursor.fetchall()
                for set in sets:
                    priceQuery = "SELECT sum(`price` * setparts.quantity) FROM parts INNER JOIN setparts ON parts.partID = setparts.partID where setID = %(setID)s;"
                    globals.cursor.execute(priceQuery, {'setID': set[0]})
                    price = globals.cursor.fetchone()[0]
                    print("SetID: {} Name: {} Price: {:.2f}".format(set[0], set[1], price))
                    query2 = "select * from setparts where setID = %(setID)s"
                    if set[0] is not None:
                        globals.cursor.execute(query2, {'setID': set[0]})
                        parts = globals.cursor.fetchall()
                        for (part) in parts:
                            query3 = "select * from parts where partID = %(partID)s"
                            globals.cursor.execute(query3, {'partID': part[0]})
                            p = globals.cursor.fetchone()
                            if p[1] is not None:
                                print("\t{}, {}".format(p[1], part[2]))
            if i == 3:
                partID = input("Enter the part ID. Leave blank if purchasing a set: ")
                setID = input("Enter the set ID. Leave blank if purchasing a part: ")
                findRecentOrder = ("select * from orders where username = %(username)s and status = 'open'")
                globals.cursor.execute(findRecentOrder, {'username': globals.login.username})
                recentOrder = globals.cursor.fetchone()
                # Add a new open order for this user if it does not already exist
                if recentOrder is None:
                    query = ("insert into orders (username, type, status) values (%(username)s, 'cash', 'open')")
                    # Create a new open order
                    globals.cursor.execute(query, {'username': globals.login.username})
                    # Fetch that order and use it as recentorder
                    globals.cursor.execute(findRecentOrder, {'username': globals.login.username})
                    recentOrder = globals.cursor.fetchone()
                orderNum = recentOrder[0]
                insert = ("insert into orderitemset (orderNum, partID, setID) values (%(orderNum)s, %(partID)s, %(setID)s)")
                if partID is None:
                    globals.cursor.execute(insert, {'orderNum': orderNum, 'partID': None, 'setID': setID})
                if setID is None:
                    globals.cursor.execute(insert, {'orderNum': orderNum, 'partID': partID, 'setID': None})
