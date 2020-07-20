class BaseMenu:
    def display(self):
        pass
class MainMenu(BaseMenu):
    amt = 0
    def display(self):
        print("LEGO Management System")
        print("You are not logged in!")
        print("---------------------\n")
        print("[0] Log in as customer (online mode)")
        print("[1] Log in as employee (store mode)")
        print("[2] Exit system")
        i = input("Please make a selection: ")
		