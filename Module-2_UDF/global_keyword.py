a=34

print("A=",a)

def getvalue():
    global a
    a=78
    print("A=",a)

getvalue()