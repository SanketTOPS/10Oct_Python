class student:
    stid:int
    stnm:str

    def getdata(self):
        self.stid=input("Enter your ID:")
        self.stnm=input("Enter your Name:")

    def printdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

st=student()
st.getdata()
st.printdata()




