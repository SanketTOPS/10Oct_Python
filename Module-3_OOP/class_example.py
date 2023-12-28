class Student:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

st=Student()
#st.getdata(101,'Sanket') #static

stid=input("Enter ID:")
stnm=input("Enter Name:")
st.getdata(stid,stnm)