import datetime
import WebPg

curTime = datetime.datetime.now()
print ("Time is " + str(curTime))

x = WebPg.Page1(38)

print (x.fox())
print (x.stringLength("seven"))
