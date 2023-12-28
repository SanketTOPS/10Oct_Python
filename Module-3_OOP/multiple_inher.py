class Sanket:
    sid=0
    stech=""

    def s_getdata(self):
        self.sid=input("Enter Sanket's ID:")
        self.stech=input("Enter Sanket's Technology:")

class Nirav:
    nid=0
    ntech=""

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.ntech=input("Enter Nirav's Technology:")

class Ashok:
    aid=0
    atech=""

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.atech=input("Enter Ashok's Technology:")


class Tops(Sanket,Nirav,Ashok):
    def printdata(self):
        print("----------Sanket's Data---------")
        print("Sanket's ID:",self.sid)
        print("Sanket's Technology:",self.stech)
        print("----------Nirav's Data---------")
        print("Nirav's ID:", self.nid)
        print("Nirav's Technology:", self.ntech)
        print("----------Ashok's Data---------")
        print("Ashok's ID:", self.aid)
        print("Ashok's Technology:", self.atech)

tp=Tops()
tp.s_getdata()
tp.n_getdata()
tp.a_getdata()
tp.printdata()