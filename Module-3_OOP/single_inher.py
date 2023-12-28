class Father:

    car=0
    bal=0

    def getata(self):
        self.car=input("Enter car details:")
        self.bal=input("Enter bank balance details:")

class Son(Father):
    def printdata(self):
        print("Total Car:",self.car)
        print("Total Balance:",self.bal)

sn=Son()
sn.getata()
sn.printdata()