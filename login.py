from tkinter import *
from tkinter import messagebox
from database_conn import create_db
from admin_dashboard import admin_GUI
import sqlite3



class login_GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Login")
        self.window.geometry("800x600")

        Label(self.window, text="Dance Feet Login", font=("Calibri", 25), height=3).grid(row=1, column=1, columnspan=2)

        lbl_username = Label(self.window, text="Username", font=("Ariel", 15), width=30, height=3)
        lbl_username.grid(row=2, column=0)

        self.usernameEntry = Entry(self.window, font=("Ariel", 15))
        self.usernameEntry.grid(row=2, column=1)

        lbl_password = Label(self.window, text="Password", font=("Ariel", 15))
        lbl_password.grid(row=3, column=0)

        self.passwordEntry = Entry(self.window, font=("Ariel", 15), show='*')
        self.passwordEntry.grid(row=3, column=1)

        Button(self.window, text="Login", font=("Ariel", 15),command=self.click).place(x=400, y=260)
        Button(self.window, text="Direct login", font=("Ariel", 15),command=self.direct).place(x=400, y=350)

        self.window.mainloop()

    #this is for testing purpose only
    def direct(self):
        admin_GUI()
        self.window.destroy()

    def click(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        conn = sqlite3.connect('dance_feet.db')
        c = conn.cursor()
        c.execute(f"SELECT * from users WHERE username='{username}' AND password='{password}'")
        records = c.fetchall()
        c.close()
        if len(records)==1:
            if records[0][2]==1:
                print("Student")
            elif records[0][2]==2:
                print("Instructor")
            elif records[0][2]==3:
                self.window.destroy()
                admin_GUI()
        else:
            messagebox.showerror(title="Login Error",message="Username or Password is incorrect")



login_GUI()