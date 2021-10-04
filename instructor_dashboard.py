from tkinter import *
from tkinter import ttk


class instructor_GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1400x1000")
        self.window.title("Instructor")

        gender = ["male","female"]
        styles = ["Waltz", "Jive", "ChaCha", "Samba"]

        title_frame = Frame(self.window,bg="#F5C2C1",relief=SUNKEN)
        left_frame = Frame(self.window,bg="#FFF0C1",relief=SUNKEN)
        right_frame = Frame(self.window,bg="#D2E2FB",relief=SUNKEN)
        top_frame = Frame(self.window,bg="#CCE4CA",relief=SUNKEN)


        Label(title_frame,text="Instructor Login",bg="#F5C2C1",font=("calibri",20)).pack()

        title_frame.grid(row=0,column=0,columnspan=2,sticky="nsew",padx=2,pady=2)
        top_frame.grid(row=1,column=0,columnspan=2,sticky="nsew",padx=2,pady=2)
        left_frame.grid(row=2,column=0,sticky="nsew",padx=2,pady=2)
        right_frame.grid(row=2,column=1,sticky="nsew",padx=2,pady=2)

        #############################################################################

        def instructor_view():
            Label(left_frame, text="Name", padx=20, pady=20, font=("calibri", 15)).grid(row=0, column=0)
            Entry(left_frame, font=("calibri", 15)).grid(row=0, column=1)

            Label(left_frame, text="Password", font=("calibri", 15), padx=20, pady=20).grid(row=1, column=0)
            Entry(left_frame, font=("calibri", 15)).grid(row=1, column=1)

            Label(left_frame, text="Gender", font=("calibri", 15), padx=10, pady=20).grid(row=2, column=0)

            radiobtn = Radiobutton(left_frame, text='male', value=0)
            radiobtn.grid(row=2, column=1, sticky="NW", pady=10)

            radiobtn = Radiobutton(left_frame, text='female', value=1)
            radiobtn.grid(row=2, column=1, sticky="SW")

            Label(left_frame, text="Styles", font=("calibri", 15), padx=20, pady=20).grid(row=3, column=0)
            cmb = ttk.Combobox(left_frame, value=styles, width=10, font=("calibri", 12))
            cmb.grid(row=3, column=1)
            cmb.current(0)

            Label(left_frame, text="Tel", font=("calibri", 15), padx=20, pady=20).grid(row=4, column=0)
            Entry(left_frame, font=("calibri", 15)).grid(row=4, column=1)

            Label(left_frame, text="H/Rate", font=("calibri", 15), padx=20, pady=20).grid(row=5, column=0)
            Entry(left_frame, font=("calibri", 15)).grid(row=5, column=1)

            Label(left_frame, text="Availability", font=("calibri", 15), padx=20, pady=20).grid(row=6, column=0)
            Entry(left_frame, font=("calibri", 15)).grid(row=6, column=1)

            Label(left_frame, text="", font=("calibri", 15), padx=10, pady=5).grid(row=7, column=0)

            Button(left_frame, text="Add Record", padx=5, pady=5).grid(row=8, column=0)
            Button(left_frame, text="Update Record", padx=5, pady=5).grid(row=8, column=1)
            Button(left_frame, text="Delete Record", padx=5, pady=5).grid(row=8, column=2)




        ############################################################################

        instructor_view()
        Button(top_frame,text="Student Management",padx=5,pady=5,command=student_view).pack(side="left")
        Button(top_frame,text="Instructor Management",padx=5,pady=5,command=instructor_view).pack(side="left")
        Button(top_frame,text="Book a Lesson",padx=5,pady=5).pack(side="left")


        ###########################################################################

        self.window.grid_rowconfigure(0,weight=1)
        self.window.grid_rowconfigure(1,weight=1)
        self.window.grid_rowconfigure(2,weight=10)
        self.window.grid_columnconfigure(0,weight=1)
        self.window.grid_columnconfigure(1,weight=15)
        self.window.mainloop()




instructor_GUI()



