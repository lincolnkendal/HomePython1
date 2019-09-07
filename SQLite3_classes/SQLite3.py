
# Changed 9/7/2019

import sqlite3
import os

#class Sql3Conn(dbConnection):
class SQLite:

    #yug = dbConnection()
    #yug.foo()

    # import sqlite3

    path = 'init'
    def __init__(self, in_Name: str):
        self.name = in_Name
        # groink = dbConnection("Tommy")
        # groink.foo()

    def DBconnect(self, inPath):
        path = inPath

        connection = sqlite3.connect(path)
        #connection = connect(path)

        path = os.path.abspath(path)
        cur1 = connection.cursor()
        cur1.execute("SELECT * FROM goof1")
        rows = cur1.fetchall()

        for row in rows:
            print(row)

        connection.close()
        #print(is_open(path))
