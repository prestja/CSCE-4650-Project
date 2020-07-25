import mysql.connector

db = None
cursor = None
login = None

class Login:
    username = None
    password = None
    employee = False
    def __init__(self, u, p, e):
        self.username = u
        self.password = p
        self.employee = e

def getRecentOrder():
    findRecentOrder = ("select * from orders where username = %(username)s and status = 'open'")
    cursor.execute(findRecentOrder, {'username': login.username})
    recentOrder = cursor.fetchone()
    return recentOrder

def getPriceOfRecentOrder(): # Returns the total of the total contents of an order, consisting of parts and/or sets
    total = 0
    recentOrder = getRecentOrder()
    if recentOrder is not None:
        orderNum = recentOrder [0]
        query = ("select * from orderitemset where orderNum = %(orderNum)s")
        cursor.execute(query, {'orderNum': orderNum})
        setparts = cursor.fetchall()
        for setpart in setparts:
            if setpart[1] is not None: # if a part
                pquery = ("select * from parts where partID = %(partID)s")
                cursor.execute(pquery, {'partID': setpart[0]})
                setpart = cursor.fetchone()
                total += setpart[2]
            elif setpart[2] is not None: # if a set
                squery = ("select * from sets where setID = %(setID)s")
                cursor.execute(squery, {'setID': setpart[2]})
                set = cursor.fetchone()
                quantity = setpart[2]
                spquery = ("select * from setparts where setID = %(setID)s")
                cursor.execute(spquery, {'setID': setpart[2]})
                setparts = cursor.fetchall()
                for setpart in setparts: # for each part in set
                    pquery = ("select * from parts where partID = %(partID)s") # find the part
                    cursor.execute(pquery, {'partID': setpart[1]})
                    part = cursor.fetchone()
                    total += part[2] * setpart[2] # and add its price
                    print("set {} has {} of part {} worth {} apiece".format(setpart[1], quantity, part[0], part[2]))
    return total