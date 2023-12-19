fl=open('hello.txt','r')

id=input("Enter ID:")
name=input("Enter Name:")
city=input("Enter City:")

if fl.writable():
    fl.write(f"ID:{id}\nName:{name}\nCity:{city}\n")
else:
    print("Error!Plz check your file mode...")
#fl.write(name)
#fl.write(city)
