f=open('hello.txt','a')


n=int(input("Enter number of students:"))

for i in range(n):
    id=input("Enter your ID:")
    name=input("Enter your Name:")

    f.write(f"ID:{id}\nName:{name}\n")


