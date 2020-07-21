import menu
import globals
import mysql.connector

def main():
    a = menu.MainMenu()
    a.display()
	
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="CSce4650!",
  database="lego"
)

globals.cursor = db.cursor()

print(db)
main()