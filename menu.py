class BaseMenu:
    def display(self):
        pass

class MainMenu(BaseMenu):
    amt = 0
    def display(self):
        print("LEGO Management System")
        print("Please a selection")
        print("---------------------\n")
        print("[0] Option 0")
        print("[1] Option 1")
        print("[2] Option 2")
        print("[3] Option 3")
        print("[4] Option 4")
        print("[5] Option 5")