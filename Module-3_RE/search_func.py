import re

mystr="This is Python!"

x=re.search('This',mystr)
#x=re.search('Is',mystr)
print(x)


if x: #true (match)
    print("Match done....")
else:
    print("Error!Plz input proper string.")