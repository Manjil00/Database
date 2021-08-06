from tkinter import *
import sqlite3

root = Tk()

# user input
user = StringVar()
user2 = StringVar()
user3 = StringVar()
user4 = IntVar()
user4.set(12345)

a = sqlite3.connect('test.db')
c = a.cursor()

'''
c.execute(""" CREATE TABLE addresses(
         first_name text,
         last_name text,
         address text,
         zipcode integer
 )""")
'''


def save():
    a = sqlite3.connect('test.db')
    c = a.cursor()
    c.execute('INSERT INTO addresses VALUES (:a,:b,:c,:d)', {
        'a': user.get(),
        'b': user2.get(),
        'c': user3.get(),
        'd': user4.get(),
    })
    print('Success')
    a.commit()
    a.close()
    user.set('')
    user2.set('')
    user3.set('')
    user4.set('')


def show():
    pass


l1 = Label(root, text='First Name', font=('Arial', 10)).pack()
e1 = Entry(root, text=user, font=('Arial', 10))
e1.pack()
l2 = Label(root, text='Last Name', font=('Arial', 10)).pack()
e2 = Entry(root, text=user2, font=('Arial', 10))
e2.pack()
l3 = Label(root, text='Address Name', font=('Arial', 10)).pack()
e3 = Entry(root, text=user3, font=('Arial', 10))
e3.pack()
l4 = Label(root, text='Zipcode', font=('Arial', 10)).pack()
e4 = Entry(root, text=user4, font=('Arial', 10))
e4.pack()
b = Button(root, text='save', font=('Arial', 10), command=save)
b.pack()
b2 = Button(root, text='Show Records', font=('Arial', 10), command=show)
b2.pack()

mainloop()
