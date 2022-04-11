import sqlite3

class Database():

    def __init__(self):
        self.conn = sqlite3.connect('carros.db')

    def getConn(self):
        return self.conn

    def closeConn(self):
        self.conn.close()