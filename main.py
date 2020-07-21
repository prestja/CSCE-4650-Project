from menu import *
import mysql.connector

def main():
    a = MainMenu()
    a.display()
	


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="CSce4650!",
  database="lego"
)

print(db)
main()