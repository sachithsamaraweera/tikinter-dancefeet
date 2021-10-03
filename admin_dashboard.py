from tkinter import *

class admin_GUI:
    def __init__(self):
        window = Tk()
        window.geometry("1000x800")
        window.title("Admin")
        title_frame = Frame(window,bg="#F5C2C1",relief=SUNKEN)
        left_frame = Frame(window,bg="#FFF0C1",relief=SUNKEN)
        right_frame = Frame(window,bg="#D2E2FB",relief=SUNKEN)
        top_frame = Frame(window,bg="#CCE4CA",relief=SUNKEN)


        Label(title_frame,text="Admin Login",bg="#F5C2C1",font=("calibri",20)).pack()

        title_frame.grid(row=0,column=0,columnspan=2,sticky="nsew",padx=2,pady=2)
        top_frame.grid(row=1,column=0,columnspan=2,sticky="nsew",padx=2,pady=2)
        left_frame.grid(row=2,column=0,sticky="nsew",padx=2,pady=2)
        right_frame.grid(row=2,column=1,sticky="nsew",padx=2,pady=2)

        ############################################################################
        Button(top_frame,text="Student Management",padx=5,pady=5).pack(side="left")
        Button(top_frame,text="Instructor Management",padx=5,pady=5).pack(side="left")
        Button(top_frame,text="Book a Lesson",padx=5,pady=5).pack(side="left")


        ###########################################################################
        Label(left_frame,text="First Name",padx=20,font=("calibri",15)).grid(row=0,column=0)
        Entry(left_frame,font=("calibri",15)).grid(row=0,column=1)

        Label(left_frame,text="Last Name",font=("calibri",15)).grid(row=1,column=0)
        Entry(left_frame,font=("calibri",15)).grid(row=1, column=1)

        Label(left_frame,text="Email",font=("calibri",15)).grid(row=2,column=0)
        Entry(left_frame,font=("calibri",15)).grid(row=2, column=1)

        Label(left_frame,text="Gender",font=("calibri",15)).grid(row=2,column=0)
        Entry(left_frame,font=("calibri",15)).grid(row=2, column=1)


        window.grid_rowconfigure(0,weight=1)
        window.grid_rowconfigure(1,weight=1)
        window.grid_rowconfigure(2,weight=10)
        window.grid_columnconfigure(0,weight=1)
        window.grid_columnconfigure(1,weight=15)

        window.mainloop()

admin_GUI()

