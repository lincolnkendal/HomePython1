#changed 9/7/2019

import datetime
from WebPg import *
import DB_Classes

#from DB_Classes.dbConnection import dbConn
from DB_Classes.SQLite3 import SQLite

curTime = datetime.datetime.now()
print ("Time is " + str(curTime))

x = Page1(38)

print (x.fox())
print (x.stringLength("seven"))

tiger = SQLite(r'Thomas')
tiger.DBconnect(r'C:\Users\Loseke\Desktop\Code\SQLite_DBs\scrape.db')
