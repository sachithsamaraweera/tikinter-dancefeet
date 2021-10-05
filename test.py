from tkinter import *
from tkinter import ttk

from database_conn import create_db


root =  Tk()
root.title("Test tree view")
root.geometry("1000x500")

my_tree = ttk.Treeview(root)

#define columns
my_tree['columns']=("First Name","Last Name","Student ID","Email","Address","DOB","Gender","Contact No")

#format columns
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("First Name",anchor=W,width=80)
my_tree.column("Last Name",anchor=W,width=120)
my_tree.column("Student ID",anchor=CENTER,width=120)
my_tree.column("Email",anchor=CENTER,width=120)
my_tree.column("Address",anchor=CENTER,width=120)
my_tree.column("DOB",anchor=CENTER,width=120)
my_tree.column("Gender",anchor=CENTER,width=120)
my_tree.column("Contact No",anchor=CENTER,width=120)

#creating heading
my_tree.heading("#0",text="",anchor=CENTER)
my_tree.heading("First Name",text="First Name",anchor=W)
my_tree.heading("Last Name",text="Last Name",anchor=W)
my_tree.heading("Student ID",text="Student ID",anchor=CENTER)
my_tree.heading("Email",text="Student ID",anchor=CENTER)
my_tree.heading("Address",text="Email",anchor=CENTER)
my_tree.heading("DOB",text="DOB",anchor=CENTER)
my_tree.heading("Gender",text="Gender",anchor=CENTER)
my_tree.heading("Contact No",text="Contact No",anchor=CENTER)



create_db.c.execute("SELECT * FROM students")
records = create_db.c.fetchall()

global count
count = 0

for record in records:
    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9]))
    count+=1
my_tree.pack()

root.mainloop()