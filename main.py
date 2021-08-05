from tkinter import *
import sqlite3

root = Tk()
root.title("Database Address Book")
root.iconbitmap('database.ico')
root.geometry('800x600')

conn = sqlite3.connect("address_book.db")
c = conn.cursor()
'''
#CREATE TABLE
c.execute("""CREATE  TABLE adresses(
    firstnametext,
    lastnametext,
    city text,
    age integer,
    )""")
'''
#print("Table Created Successfully")


fnamelabel=Label(root,text="FirstName") .pack()
fnameentry=Entry(root,text="").pack()
lnamelabel=Label(root,text="LastName") .pack()
lnameentry=Entry(root,text="").pack()
citylabel=Label(root,text="City") .pack()
cityentry=Entry(root,text="").pack()
agelabel=Label(root,text="AGE") .pack()
ageentry=Entry(root,text="").pack()
button1=Button(root,text="Register",relief=FLAT).pack()


#change commit
conn.commit()
#closing database
conn.close()
mainloop()
