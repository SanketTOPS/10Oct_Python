import re

mystr="This is Python!14565678"

#x=re.findall('^This',mystr)
#x=re.findall('^[A-Z]',mystr)
x=re.findall('78$',mystr)
print(x)