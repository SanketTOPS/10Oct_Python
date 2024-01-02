import re

mystr="This is Python!"

x=re.match('is',mystr)
print(x)


if x: #true (match)
    print("Match done....")
else:
    print("Error!Plz input proper string.")