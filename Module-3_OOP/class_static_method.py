class Student:
    @staticmethod
    def getdata(id,name):
        print("ID:",id)
        print("Name:",name)

st=Student() #namespace
st.getdata(12,'Snaket')