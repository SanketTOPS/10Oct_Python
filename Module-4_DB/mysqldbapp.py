import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='newdb')
    print("Database connected!")
except Exception as e:
    print(e)

cr=db.cursor()

# Table create
tbl_create="create table studinfo(id integer primary key auto_increment,name varchar(20),city varchar(20))"
try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)
    
# Insert Data
name=input("Enter your name:")
city=input("Enter your City:")

insert_data=f"insert into studinfo(name,city)values('{name}','{city}') "
try:
    cr.execute(insert_data)
    db.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)




