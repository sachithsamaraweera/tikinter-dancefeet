import sqlite3
from tkinter import *
from tkinter import ttk
window = Tk()
conn = sqlite3.connect('dance_feet.db')
c = conn.cursor()
c.execute("SELECT name,hrate FROM instructors WHERE hrate<=4000")
records = c.fetchall()

testlist = []
for record in records:
    testlist.append(record[0])

cb1 = ttk.Combobox(window,values=testlist)
cb1.configure(state=NORMAL)
cb1.pack()

window.mainloop()