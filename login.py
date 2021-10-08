from tkinter import *
from tkinter import messagebox
from database_conn import create_db
from admin_dashboard import admin_GUI
from instructor_dashboard import instructor_GUI
import sqlite3


class login_GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Login")
        self.window.geometry("600x400")
        self.window.configure(bg="#A2D2FF")
        photo = PhotoImage(file="Untitled-1.png")
        Label(self.window, text="Dance Feet Login", font=("Calibri", 25), height=3,bg="#A2D2FF").grid(row=1, column=1, columnspan=2)

        lbl_username = Label(self.window, text="Username", font=("Ariel", 15), width=20, height=3,bg="#A2D2FF")
        lbl_username.grid(row=2, column=0)

        self.usernameEntry = Entry(self.window, font=("Ariel", 15))
        self.usernameEntry.grid(row=2, column=1)

        lbl_password = Label(self.window, text="Password", font=("Ariel", 15),bg="#A2D2FF")
        lbl_password.grid(row=3, column=0)

        self.passwordEntry = Entry(self.window, font=("Ariel", 15), show='*')
        self.passwordEntry.grid(row=3, column=1)

        Button(self.window, text="",image=photo, font=("Ariel", 15),command=self.click,borderwidth=0,bg="#A2D2FF",activebackground="#A2D2FF").place(x=340, y=230)


        self.window.mainloop()

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
                self.window.destroy()
                instructor_GUI()
            elif records[0][2]==3:
                self.window.destroy()
                admin_GUI()
        else:
            messagebox.showerror(title="Login Error",message="Username or Password is incorrect")

login_GUI()