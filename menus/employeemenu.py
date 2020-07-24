import mysql.connector
import globals

class EmployeeMenu:
    def display(self):
        print("Listing all employees in the system")
        globals.cursor.execute("select * from employees")
        employees = globals.cursor.fetchall()
        for employee in employees:
            print(employee)
        employeeID = int(input("Enter an employee ID: "))
        name = input("Assign employee's name: ")
        password = input("Assign employee's password: ")
        print("[1] Physical\n[2] Online")
        storeprefs = int(input("Assign employee's store preferences: "))
        query = ("update employees set name = %(name)s, password = %(password)s, storeprefs = %(storeprefs)s where employeeID = %(employeeID)s")
        try:
            globals.cursor.execute(query, {'name': name, 'password': password, 'storeprefs': storeprefs, 'employeeID': employeeID})
            globals.db.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
