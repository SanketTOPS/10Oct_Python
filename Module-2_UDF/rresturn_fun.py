"""def getsum(a,b):
    return a+b
    print("Hello Student!")
    
def answer():
    x=getsum(23,45)
    print(x)
   
answer()"""


def getdata(id,name):
    return id,name

def printdata():
    x=getdata(101,'Sanket')
    print("ID:",x[0])
    print("Name:",x[1])

printdata()