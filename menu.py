class BaseMenu:
    def display(self):
        pass
class MainMenu(BaseMenu):
    def display(self):
        i = -1
        print("LEGO Management System")
        print("You are not logged in!")
        print("---------------------\n")
        print("[1] Log in as customer (online mode)")
        print("[2] Log in as employee (store mode)")
        print("[3] Exit system")
        i = int(input("Please make a selection: "))
        while i < 1 or i > 3:
            i = int(input("Please make a selection: "))
        if i == 1:
            print("Selection 1")
        if i == 2:
            print("Selection 2")
        if i == 3:
            print("Selection 3")