import sqlite3

try:
    db=sqlite3.connect("stdata.db")
    print("Database connected!")
except Exception as e:
    print(e)

#Table Create
    
tbl_create="create table studinfo(id integer primary key autoincrement,name text,city text)"
try:
    db.execute(tbl_create)
    print("Table created...")
except Exception as e:
    print(e)

#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('nirav','surat'),('ashok','morbi'),('hitesh','ahmedabad'),('darshan','rajkot'),('gopal','baroda')"
try:
    db.execute(insert_data)
    db.commit()
    print("Data inserted!")
except Exception as e:
    print(e)"""

#Update Data
"""update_data="update studinfo set name='mitesh',city='jamnagar' where id=12"
try:
    db.execute(update_data)
    db.commit()
    print("Data updated!")
except Exception as e:
    print(e)"""


#Delete Data
delete_data="delete from studinfo where name='darshan'"
try:
    db.execute(delete_data)
    db.commit()
    print("Data deleted!")
except Exception as e:
    print(e)

#Select Data
show_data="select * from studinfo"
cur=db.cursor()
try:
    cur.execute(show_data)
    data=cur.fetchall()
    #data=cur.fetchmany(3)
    #data=cur.fetchone()
    #print(data)

    for i in data:
        print(i[2])

except Exception as e:
    print(e)
