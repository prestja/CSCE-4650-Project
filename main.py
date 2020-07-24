# from .menu import MainMenu
from menus.mainmenu import MainMenu
import globals
import mysql.connector

def main():
    a = MainMenu()
    a.display()
    pass
	
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="CSce4650!",
  database="lego"
)

globals.cursor = db.cursor()
globals.db = db

main()