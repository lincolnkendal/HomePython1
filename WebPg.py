class Page1:

    # Changed 8/14/2019 10:42 PM

    age = 3

    def __init__(self, someNumber):
        self.age = someNumber
        print ("passed in value is one less than " + str(someNumber + 1))


    def fox(self):
        print (self.age - 10)
        return 3.4

    def stringLength(self, inString):
        return len(inString)
