def getdata(id,name,city='Rajkot',sub='Python'): #default argument value
    print("ID:",id)
    print("Name:",name)
    print("City:",city)
    print("Subject:",sub)

#getdata(101,'Sanket')
#getdata(1,'Nirav','Surat') #positional arguments

#getdata('Sanket',12)

getdata(name='Sanket',id='101',sub='JAVA') #keyword arguments
