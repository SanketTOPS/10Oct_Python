stdata={'id':101,'name':'Sanket','sub':'Python'}

"""print(stdata)
print(stdata['name'])
print(stdata.get('sub'))
print(len(stdata))

print(stdata.keys())
print(stdata.values())"""

# ---------------------------------- #

print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""


"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo")"""


"""if 'Sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""

stdata["id"]=102

stdata["city"]="Rajkot"
#stdata.pop('sub')
#del stdata['sub']
stdata.clear()
print(stdata)