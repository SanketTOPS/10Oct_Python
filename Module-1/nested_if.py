s1=int(input("Enter Subject 1 Mark:"))
s2=int(input("Enter Subject 2 Mark:"))
s3=int(input("Enter Subject 3 Mark:"))
s4=int(input("Enter Subject 4 Mark:"))


if s1>=40 and s2>=40 and s3>=40 and s4>=40: #root (parent)

    total=s1+s2+s3+s4
    print("Total:",total)

    pr=total/4
    print("PR:",pr)

    if pr>=70: #child
        print("Result:A+")
    elif pr>=60: #child
        print("Result:A")
    elif pr>=50: #child
        print("Result:B")
    elif pr>=40: #child
        print("Result:C")
        
else:
    print("Result:FAIL")


