import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='newdata')
    print("Database connected!")
except Exception as e:
    print(e)


cur=db.cursor()

# Create Table
create_tbl="create table studinfo(id integer primary key auto_increment,name text, city text)"
try:
    cur.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('mitesh','surat'),('ashok','morbi'),('prasiddh','ahmedabad'),('hitesh','baroda'),('nirav','rajkot')"
try:
    cur.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

#Update Data
"""update_data="update studinfo set name='jitesh',city='jamnagar' where id=6"
try:
    cur.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""
    

#Delete Data
"""delete_data="delete from studinfo where id=6"
try:
    cur.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""


# Show Data
show_data="select * from studinfo"
try:
    cur.execute(show_data)
    data=cur.fetchall()
    #data=cur.fetchmany(3)
    #data=cur.fetchone()
    #print(data)
    for i in data:
        print(i)

except Exception as e:
    print(e)
