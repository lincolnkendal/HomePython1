import datetime
#import WebPg
from WebPg import Page1

#from Gen_DB_classes import dbConnection
from Gen_DB_classes import *

# 8/16/2019 9:46 PM

curTime = datetime.datetime.now()
print ("Time is " + str(curTime))

#x = WebPg.Page1(38)
x = Page1(38)

print (x.fox())
print (x.stringLength("seven"))
