import mysql.connector as sql

con = sql.connect(host="localhost",user="root",password="",database="abhi")
cursor = con.cursor()
def insert():
    id =int(input("enter the id:"))
    name=input("enter name:")
    year=input("enter the year of study:")
    query ="insert into info values({},'{}',{})".format(id,name,year)
    cursor.execute(query)
    con.commit()

def delete():
    id = int(input("enter the id:"))
    query = "delete from info where id='{}'".format(id)
    cursor.execute(query)
    con.commit()

def update():
    column=input("enter the column name:")
    value=input("enter value:")
    id = int(input("enter the id:"))
    query= "update info set {}='{}' where id={}".format(column,value,id)
    cursor.execute(query)
    con.commit()
while(True):
    ch = int(input("enter your choice:"))
    if (ch==1):
        insert()
    elif(ch==2):
        delete()
    elif(ch==3):
        update()

