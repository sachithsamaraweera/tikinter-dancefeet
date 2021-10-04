from tkinter import *
from tkinter import ttk
from database_conn import create_db

class admin_GUI:
    def __init__(self):
        window = Tk()
        window.geometry("1400x1000")
        window.title("Admin")

        title = Label(window,text="DanceFeet Management",font=("Arial",25),border=5,relief=SUNKEN,bg="#F5C2C1")
        title.pack(side=TOP,fill=X)

        mainframe = Frame(window,border=5,relief=SUNKEN)
        mainframe.place(x=0, y=50, width=1400, height=1000)

        notebook = ttk.Notebook(mainframe)
        tab1 = Frame(notebook)
        tab2 = Frame(notebook)
        tab3 = Frame(notebook)
        notebook.add(tab1, text="Student Registration")
        notebook.add(tab2, text="Instructor Registration")
        notebook.add(tab3, text="Lesson Booking")
        notebook.pack(expand=True, fill="both")

        detail_frame_student =  LabelFrame(tab1,text="Enter details",font=("Arial",20),border=5,relief=SUNKEN)
        detail_frame_student.place(x=20,y=5,width=500,height=800)

        detail_frame_instructor =  LabelFrame(tab2,text="Enter details",font=("Arial",20),border=5,relief=SUNKEN)
        detail_frame_instructor.place(x=20,y=5,width=500,height=800)

        detail_frame_lesson_booking =  LabelFrame(tab3,text="Enter details",font=("Arial",20),border=5,relief=SUNKEN)
        detail_frame_lesson_booking.place(x=20,y=5,width=500,height=800)

        preview_pane_lesson_booking =  LabelFrame(tab3,text="View details",font=("Arial",20),border=5,relief=SUNKEN)
        preview_pane_lesson_booking.place(x=570,y=5,width=800,height=800)

        preview_pane =  LabelFrame(tab1,text="View details",font=("Arial",20),border=5,relief=SUNKEN)
        preview_pane.place(x=570,y=5,width=800,height=800)

        preview_pane_instructor =  LabelFrame(tab2,text="View details",font=("Arial",20),border=5,relief=SUNKEN)
        preview_pane_instructor.place(x=570,y=5,width=800,height=800)

        gender = ["male","female"]
        styles = ["Waltz", "Jive", "ChaCha", "Samba"]
        genderInt = IntVar()


        def fetach_student_details():
            create_db.c.execute(f"SELECT * from students")
            records=create_db.c.fetchall()
            print(records)



        def student_registration():
            Label(detail_frame_student, text="First Name", padx=20, pady=20, font=("calibri", 15)).grid(row=0, column=0)
            stu_entry_firstname=Entry(detail_frame_student, font=("calibri", 15))
            stu_entry_firstname.grid(row=0, column=1)

            Label(detail_frame_student, text="Last Name", font=("calibri", 15), padx=20, pady=20).grid(row=1, column=0)
            stu_entry_lastname=Entry(detail_frame_student, font=("calibri", 15))
            stu_entry_lastname.grid(row=1, column=1)

            Label(detail_frame_student, text="Email", font=("calibri", 15), padx=20, pady=20).grid(row=2, column=0)
            stu_entry_email=Entry(detail_frame_student, font=("calibri", 15))
            stu_entry_email.grid(row=2, column=1)

            Label(detail_frame_student, text="Address", font=("calibri", 15), padx=20, pady=20).grid(row=3, column=0)
            stu_entry_address=Entry(detail_frame_student, font=("calibri", 15))
            stu_entry_address.grid(row=3, column=1)

            Label(detail_frame_student, text="DOB", font=("calibri", 15), padx=20, pady=20).grid(row=4, column=0)
            stu_entry_dob=Entry(detail_frame_student, font=("calibri", 15))
            stu_entry_dob.grid(row=4, column=1)

            Label(detail_frame_student, text="Gender", font=("calibri", 15), padx=10, pady=20).grid(row=5, column=0)

            radiobtn = Radiobutton(detail_frame_student, text='male', value=1,variable=genderInt)
            radiobtn.grid(row=5, column=1, sticky="NW", pady=10)

            radiobtn2 = Radiobutton(detail_frame_student, text='female', value=0,variable=genderInt)
            radiobtn2.grid(row=5, column=1, sticky="SW")

            Label(detail_frame_student, text="Contact No", font=("calibri", 15), padx=20, pady=20).grid(row=6, column=0)
            stu_entry_contact=Entry(detail_frame_student, font=("calibri", 15))
            stu_entry_contact.grid(row=6, column=1)

            Label(detail_frame_student, text="", font=("calibri", 15), padx=10, pady=5).grid(row=7, column=0)

            def add_student_record():

                first_name = stu_entry_firstname.get()
                lastname = stu_entry_lastname.get()
                email = stu_entry_email.get()
                gender = ''
                dob = stu_entry_dob.get()
                contact = stu_entry_contact.get()
                address = stu_entry_address.get()



                if genderInt.get()==1:
                    gender="Male"
                else:
                    gender="Female"

                create_db.c.execute(f"INSERT INTO students('first_name','last_name','email','gender','dob','contact','address') VALUES('{first_name}','{lastname}','{email}','{gender}','{dob}','{contact}','{address}')")
                create_db.conn.commit()


            Button(detail_frame_student, text="Add Record", padx=5, pady=5,command=add_student_record).grid(row=8, column=0)
            Button(detail_frame_student, text="Update Record", padx=5, pady=5).grid(row=8, column=1)
            Button(detail_frame_student, text="Delete Record", padx=5, pady=5).grid(row=8, column=2)

        student_registration()



        def instructor_tab():
            Label(detail_frame_instructor, text="Name", padx=20, pady=20, font=("calibri", 15)).grid(row=0, column=0)
            Entry(detail_frame_instructor, font=("calibri", 15)).grid(row=0, column=1)

            Label(detail_frame_instructor, text="Password", font=("calibri", 15), padx=20, pady=20).grid(row=1, column=0)
            Entry(detail_frame_instructor, font=("calibri", 15)).grid(row=1, column=1)

            Label(detail_frame_instructor, text="Gender", font=("calibri", 15), padx=10, pady=20).grid(row=2, column=0)

            radiobtn = Radiobutton(detail_frame_instructor, text='male', value=0)
            radiobtn.grid(row=2, column=1, sticky="NW", pady=10)

            radiobtn = Radiobutton(detail_frame_instructor, text='female', value=1)
            radiobtn.grid(row=2, column=1, sticky="SW")

            Label(detail_frame_instructor, text="Styles", font=("calibri", 15), padx=20, pady=20).grid(row=3, column=0)
            cmb = ttk.Combobox(detail_frame_instructor, value=styles, width=10, font=("calibri", 12))
            cmb.grid(row=3, column=1)
            cmb.current(0)

            Label(detail_frame_instructor, text="Tel", font=("calibri", 15), padx=20, pady=20).grid(row=4, column=0)
            Entry(detail_frame_instructor, font=("calibri", 15)).grid(row=4, column=1)

            Label(detail_frame_instructor, text="H/Rate", font=("calibri", 15), padx=20, pady=20).grid(row=5, column=0)
            Entry(detail_frame_instructor, font=("calibri", 15)).grid(row=5, column=1)

            Label(detail_frame_instructor, text="Availability", font=("calibri", 15), padx=20, pady=20).grid(row=6,
                                                                                                             column=0)
            Entry(detail_frame_instructor, font=("calibri", 15)).grid(row=6, column=1)

            Label(detail_frame_instructor, text="", font=("calibri", 15), padx=10, pady=5).grid(row=7, column=0)

            Button(detail_frame_instructor, text="Add Record", padx=5, pady=5).grid(row=8, column=0)
            Button(detail_frame_instructor, text="Update Record", padx=5, pady=5).grid(row=8, column=1)
            Button(detail_frame_instructor, text="Delete Record", padx=5, pady=5).grid(row=8, column=2)
        instructor_tab()



        # Button(top_frame,text="Student Management",padx=5,pady=5).pack(side="left")
        # Button(top_frame,text="Instructor Management",padx=5,pady=5).pack(side="left")
        # Button(top_frame,text="Book a Lesson",padx=5,pady=5).pack(side="left")



        window.mainloop()


admin_GUI()


