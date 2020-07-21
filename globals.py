import mysql.connector

db = None
cursor = None
login = None

class Login:
    username = None
    password = None
    def __init__(self, u, p):
        self.username = u
        self.password = p