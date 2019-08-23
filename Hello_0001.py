import datetime
import WebPg

#from Gen_DB_classes import dbConnection
from Gen_DB_classes import *

curTime = datetime.datetime.now()
print ("Time is " + str(curTime))

x = WebPg.Page1(38)
print (x.fox())
print (x.stringLength("seven"))
