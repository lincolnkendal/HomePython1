#changed 9/21/2019

# Learn this:
# 1. Project container & Management in Atom
#       Atom has no projects, only folders.
# 2. Commiting Code changes into github.com from within Atom
#       See video -->> https://www.youtube.com/watch?v=HZV7OKoD1Hc
#       Push to Github from Atom
#       Problem button says --> "Create detached commit"
# 3. Master Python import tech well enough to use a separate class for the SQLite connection
# 4. Debugging Python in Atom

import datetime
from WebPg import *
import DB_Classes

#from DB_Classes. import dbConn
from DB_Classes.SQLite3 import KSQLite

curTime = datetime.datetime.now()
print ("Time is " + str(curTime))

x = Page1(38)

print (x.fox())
print (x.stringLength("seven"))

tiger = KSQLite(r'Thomas')
tiger.DBconnect(r'C:\Users\Loseke\Desktop\Code\SQLite_DBs\scrape.db')
