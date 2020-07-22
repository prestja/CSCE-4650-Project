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