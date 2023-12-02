#Function defining

def myfunc():
    print("This is function!")

def getmul(a,b):
    print("Mul:",a*b)

def getdata(id,name,city):
    print("ID:",id)
    print("Name:",name)
    print("City:",city)

#Calling a Functions
myfunc()
getmul(23,45)
#getdata(101,'Sanket','Rajkot') #static


id=input("Enter ID:")
name=input("Enter Name:")
city=input("Enter City:")

getdata(id,name,city) #dynamic
