import mysql.connector as sql
from tkinter import *
import tkinter.messagebox as msgbox
def insert():
    id =eid.get()
    name = ename.get()
    phone = ephone.get()
    city=ecity.get()
    recname=ername.get()
    recphone=erphone.get()
    reccity=ercity.get()

    if(id=="" or name=="" or phone==""):
        msgbox.showinfo("Insert valid data","All fields are required")
    else:
        con = sql.connect(host="localhost",user='root',password='',database='system')

        cursor = con.cursor()
        cursor.execute("insert into clients values('" + id +"','" + name +"','" + phone +"','" + city +"','" + recname +"','" + recphone +"','" + reccity +"')")

        cursor.execute("commit")

        eid.delete(0, 'end')
        ename.delete(0, 'end')
        ephone.delete(0, 'end')
        ecity.delete(0, 'end')
        ername.delete(0, 'end')
        erphone.delete(0, 'end')
        ercity.delete(0, 'end')
        show()
        msgbox.showinfo("insert status","insert success")
        con.close()
def delete():
    if(eid.get()==""):
        msgbox.showinfo("delete status","ID is compolsary for delete")
    else:
        con = sql.connect(host="localhost", user='root', password='', database='system')
        cursor = con.cursor()
        cursor.execute("delete from clients where id='"+ eid.get()+"'")

        cursor.execute("commit")

        eid.delete(0, 'end')
        ename.delete(0, 'end')
        ephone.delete(0, 'end')
        ecity.delete(0, 'end')
        ername.delete(0, 'end')
        erphone.delete(0, 'end')
        ercity.delete(0, 'end')
        show()
        msgbox.showinfo("delete status", "Deleted successfully")
        con.close()

def update():
    id = eid.get()
    name = ename.get()
    phone = ephone.get()
    city = ecity.get()
    recname = ername.get()
    recphone = erphone.get()
    reccity = ercity.get()

    if (id == "" or name == "" or phone == ""):
        msgbox.showinfo("update status", "All fields are required")
    else:
        con = sql.connect(host="localhost", user='root', password='', database='system')
        cursor = con.cursor()
        cursor.execute("update clients set custname='"+name+"',custphone='"+phone+"',custphone='"+phone+"',custcity='"+city+"',recname='"+recname+"',recphone='"+recphone+"',reccity='"+reccity+"' where id='"+ id +"'")
        cursor.execute("commit")

        eid.delete(0, 'end')
        ename.delete(0, 'end')
        ephone.delete(0, 'end')
        ecity.delete(0, 'end')
        ername.delete(0, 'end')
        erphone.delete(0, 'end')
        ercity.delete(0, 'end')
        show()

        msgbox.showinfo("update status", "updated successfully")
        con.close()

def get():
    if (eid.get() == ""):
        msgbox.showinfo("fetch statue", "ID is compolsary ")
    else:
        con = sql.connect(host="localhost", user='root', password='', database='system')
        cursor = con.cursor()
        cursor.execute("select * from clients where id='"+eid.get()+"'")
        rows= cursor.fetchall()

        for row in rows:
            ename.insert(0,row[1])
            ephone.insert(0,row[2])
            ecity.insert(0, row[3])
            ername.insert(0,row[4])
            erphone.insert(0,row[5])
            ercity.insert(0,row[6])
        con.close()

def show():
    con = sql.connect(host="localhost", user='root', password='', database='system')
    cursor=con.cursor()
    cursor.execute("select * from clients")
    rows = cursor.fetchall()
    list.delete(0,list.size())


    for row in rows:
        insertData =str(row[0])+'  ' +row[1]
        list.insert(list.size(),insertData)
    con.close()

root=Tk()
root.geometry("600x400")
root.title("window")
root.config(bg='sky blue')

#initial
id = Label(root,text="Enter id",font=('bold',10))
id.place(x=20,y=30)

name = Label(root,text="Name",font=('bold',10))
name.place(x=20,y=60)

phone = Label(root,text="phone",font=('bold',10))
phone.place(x=20,y=90)

# Destination
city = Label(root,text="customer city",font=('bold',10))
city.place(x=20,y=130)

recname= Label(root,text="recipient name ",font=('bold',10))
recname.place(x=20,y=160)

recphone = Label(root,text="recipient phone",font=('bold',10))
recphone.place(x=20,y=190)

reccity= Label(root,text="destination city",font=('bold',10))
reccity.place(x=20,y=220)

eid = Entry()
eid.place(x=150,y=30)

ename=Entry()
ename.place(x=150,y=60)

ephone=Entry()
ephone.place(x=150,y=90)

ecity=Entry()
ecity.place(x=150,y=130)

ername=Entry()
ername.place(x=150,y=160)

erphone=Entry()
erphone.place(x=150,y=190)

ercity=Entry()
ercity.place(x=150,y=220)


insert= Button(root,text='Insert',font=("italic",10),bg="white",command=insert)
insert.place(x=20,y=260)

delete= Button(root,text='Delete',font=("italic",10),bg="white",command=delete)
delete.place(x=70,y=260)

update= Button(root,text='Update',font=("italic",10),bg="white",command=update)
update.place(x=130,y=260)

get= Button(root,text='Get',font=("italic",10),bg="white",command=get)
get.place(x=190,y=260)

list = Listbox(root)
list.place(x=290,y=30)
show()
root.mainloop()




