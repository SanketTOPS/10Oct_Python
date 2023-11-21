data=['c++','python','php','java','node']

#print(data)
"""print(data[0])
print(data[-1])
print(data[0:3])
print(data[2:])
print(data[:3])"""

"""data[2]='angular'
print(data)"""

#print(len(data))

# ----------------------------------------- #

print(data)

"""if 'Python' in data:
    print("Yes...")
else:
    print("Noo")"""

"""for i in data:
    print(i)"""


#print(data[0])
#print(data.index('c++'))
#print(data.index('python'))

"""for i in data:
    #print(i)
    #print(i,"=",data.index(i))
    print(f"{i}={data.index(i)}")"""

n=0
for i in data:
    print(f"{i}={n}")
    n+=1