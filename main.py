from tkinter import *
import sqlite3

root = Tk()
root.title("Database Address Book")
root.iconbitmap('database.ico')
root.geometry('800x600')

conn = sqlite3.connect("address_book.db")
c = conn.cursor()

#CREATE TABLE
c.execute(""" CREATE TABLE adress(
fname text,
lname text,
city text,
age integer ,
 )""")


def register():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    c.execute("INSERT INTO adress VALUES(:fname,:lname,:city,:age)",{
        "fname":fnameentry.get(),
        "lname":lnameentry.get(),
        "city":cityentry.get(),
        "age":ageentry.get()
             })
    print("Registered Successfully")
    conn.commit()
    conn.close()
    fnameentry.delete(0, END)
    lnameentry.delete(0, END)
    cityentry.delete(0, END)
    ageentry.delete(0, END)

#query
def query():
    conn=sqlite3.connect("address_book.db")
    c=conn.cursor()
    c.execute("SELECT*, oid from adress")
    records=c.fetchall()
    print(records)
    conn.commit()
    conn.close()


    print_records=""
    for record in records:
        print_records+=str("record") + "\n"







#print("Table Created Successfully")

#designing
fnamelabel=Label(root,text="FirstName")
fnamelabel.pack()
fnameentry=Entry(root,text="")
fnameentry.pack()
lnamelabel=Label(root,text="LastName")
lnamelabel.pack()
lnameentry=Entry(root,text="")
lnameentry.pack()
citylabel=Label(root,text="City")
citylabel.pack()
cityentry=Entry(root,text="")
cityentry.pack()
agelabel=Label(root,text="AGE")
agelabel.pack()
ageentry=Entry(root,text="")
ageentry.pack()
button1=Button(root,text="Register",relief=FLAT,command=register).pack()
queryBtn=Button(root,text="Show Records",relief=FLAT,command=query).pack()


#change commit
conn.commit()
#closing database
conn.close()
mainloop()
