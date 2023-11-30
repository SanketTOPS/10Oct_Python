def getdata(id,name,city):
    print("ID:",id)
    print("Name:",name)
    print("City:",city)


n=int(input("Enter number of students:"))

for i in range(n):
    stid=input("Enter ID:")
    stnm=input("Enter Name:")
    stcity=input("Enter City:")

    getdata(stid,stnm,stcity)