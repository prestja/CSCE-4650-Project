import globals
import mysql.connector

class PartMenu ():
    def display(self):
        d = 0
        while d < 1:
            print("[1] View parts")
            print("[2] View sets")
            print("[3] Search for a part or set")
            print("[4] Add item to order")
            print("[0] Go back")
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
                name = input("Enter the name of the part or set you are interested in: ")
                globals.cursor.execute("SELECT * FROM parts WHERE name LIKE %s", ("%" + name + "%",))
                results = globals.cursor.fetchall()
                for result in results:
                    print(result)
                globals.cursor.execute("SELECT * FROM sets WHERE name LIKE %s", ("%" + name + "%",))
                results = globals.cursor.fetchall()
                for result in results:
                    print(result)

            if i == 4:
                partID = input("Enter the part ID: ")
                setID = input("Enter the set ID: ")
                findRecentOrder = ("select * from orders where username = %(username)s and status = 'open'")
                globals.cursor.execute(findRecentOrder, {'username': globals.login.username})
                recentOrder = globals.cursor.fetchone()
                # Add a new open order for this user if it does not already exist
                if recentOrder is None:
                    print("Making a new order")
                    query = ("insert into orders (username, type, status) values (%(username)s, 'cash', 'open')")
                    # Create a new open order
                    globals.cursor.execute(query, {'username': globals.login.username})
                    globals.db.commit()
                    # Fetch that order and use it as recentorder
                    globals.cursor.execute(findRecentOrder, {'username': globals.login.username})
                    recentOrder = globals.cursor.fetchone()
                
                orderNum = recentOrder[0]
                if partID == "": # if a set
                    try:
                        insert = ("insert into orderitemset (orderNum, setID) values (%(orderNum)s, %(setID)s)")
                        globals.cursor.execute(insert, {'orderNum': orderNum, 'setID': setID})
                    except mysql.connector.Error as err:
                        print("Something went wrong: {}".format(err))
                elif setID == "": # if a part
                    try:
                        insert = ("insert into orderitemset (orderNum, partID) values (%(orderNum)s, %(partID)s)")
                        globals.cursor.execute(insert, {'orderNum': orderNum, 'partID': partID})
                    except mysql.connector.Error as err:
                        print("Something went wrong: {}".format(err))
                globals.db.commit()
