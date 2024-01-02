class stud:
    def getdata(self,id,name): #original
        print("ID:",id)
        print("Name:",name)


class newstud(stud):
    def getdata(self, id, name): #xerox
        return super().getdata(id, name)


    
st=stud()
ne=newstud()


st.getdata(1,'Sanket')
ne.getdata(2,'Mitesh')