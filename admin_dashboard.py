from tkinter import *
from tkinter import ttk
from database_conn import create_db
from tkinter import messagebox
import sqlite3

class admin_GUI:
    def __init__(self):
        window = Tk()
        window.geometry("1400x1000")
        window.title("Admin")

        title = Label(window,text="DanceFeet Management",font=("Arial",25),border=5,relief=SUNKEN,bg="#F5C2C1")
        title.pack(side=TOP,fill=X)

        mainframe = Frame(window,border=5,relief=SUNKEN)
        mainframe.place(x=0, y=50, width=1380, height=1000)

        notebook = ttk.Notebook(mainframe)
        tab1 = Frame(notebook)
        tab2 = Frame(notebook)
        tab3 = Frame(notebook)
        notebook.add(tab1, text="Student Registration")
        notebook.add(tab2, text="Instructor Registration")
        notebook.add(tab3, text="Lesson Booking")
        notebook.pack(expand=True, fill="both")

        detail_frame_student =  LabelFrame(tab1,text="Enter details",font=("Arial",20),border=5,relief=SUNKEN)
        detail_frame_student.place(x=20,y=5,width=400,height=800)

        detail_frame_instructor =  LabelFrame(tab2,text="Enter details",font=("Arial",20),border=5,relief=SUNKEN)
        detail_frame_instructor.place(x=20,y=5,width=500,height=800)

        detail_frame_lesson_booking =  LabelFrame(tab3,text="Enter details",font=("Arial",20),border=5,relief=SUNKEN)
        detail_frame_lesson_booking.place(x=20,y=5,width=500,height=800)

        preview_pane_lesson_booking =  LabelFrame(tab3,text="View details",font=("Arial",20),border=5,relief=SUNKEN)
        preview_pane_lesson_booking.place(x=420,y=5,width=1000,height=800)

        preview_pane =  LabelFrame(tab1,text="View details",font=("Arial",20),border=5,relief=SUNKEN)
        preview_pane.place(x=420,y=5,width=1000,height=800)

        preview_pane_instructor =  LabelFrame(tab2,text="View details",font=("Arial",20),border=5,relief=SUNKEN)
        preview_pane_instructor.place(x=420,y=5,width=1000,height=800)

        gender = ["male","female"]
        styles = ["Waltz", "Jive", "ChaCha", "Samba"]
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday" , "Saturday","Sunday"]
        genderInt = IntVar()
        selected_student_id = 0
        selected_instructor_id = 0




        def student_registration_tab():
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

            Label(detail_frame_student, text="Styles", font=("calibri", 15), padx=20, pady=20).grid(row=7, column=0)
            cmb = ttk.Combobox(detail_frame_student, value=styles, width=10, font=("calibri", 12))
            cmb.grid(row=7, column=1)
            cmb.current(0)

            Label(detail_frame_student, text="H/rate", font=("calibri", 15), padx=20, pady=20).grid(row=8, column=0)
            stu_entry_hourly_rate=Entry(detail_frame_student, font=("calibri", 15))
            stu_entry_hourly_rate.grid(row=8, column=1)


# displaying the tree view
            my_tree = ttk.Treeview(preview_pane,height=36)
            # define columns
            my_tree['columns'] = (
                "Student ID", "First Name", "Last Name", "Email", "Address", "DOB", "Gender", "Contact No", "Style",
                "H/rate")

            # format columns
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Student ID", anchor=CENTER, width=80)
            my_tree.column("First Name", anchor=W, width=80)
            my_tree.column("Last Name", anchor=W, width=80)
            my_tree.column("Email", anchor=CENTER, width=120)
            my_tree.column("Address", anchor=CENTER, width=120)
            my_tree.column("DOB", anchor=CENTER, width=80)
            my_tree.column("Gender", anchor=CENTER, width=80)
            my_tree.column("Contact No", anchor=CENTER, width=120)
            my_tree.column("Style", anchor=CENTER, width=80)
            my_tree.column("H/rate", anchor=CENTER, width=80)

            # creating heading
            my_tree.heading("#0", text="", anchor=CENTER)
            my_tree.heading("Student ID", text="Student ID", anchor=CENTER)
            my_tree.heading("First Name", text="First Name", anchor=W)
            my_tree.heading("Last Name", text="Last Name", anchor=W)
            my_tree.heading("Email", text="Email", anchor=CENTER)
            my_tree.heading("Address", text="Address", anchor=CENTER)
            my_tree.heading("DOB", text="DOB", anchor=CENTER)
            my_tree.heading("Gender", text="Gender", anchor=CENTER)
            my_tree.heading("Contact No", text="Contact No", anchor=CENTER)
            my_tree.heading("Style", text="Style", anchor=CENTER)
            my_tree.heading("H/rate", text="H/rate", anchor=CENTER)
            my_tree.place(x=20, y=20)

#select record from the treeview


#fetch from the database to the tree view
            def fetch_to_tree():
                conn = sqlite3.connect('dance_feet.db')
                c = conn.cursor()
                c.execute("SELECT * FROM students")
                records = c.fetchall()

                global count
                count = 0

                for record in records:
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(
                        record[0], record[1], record[2], record[3], record[7], record[5], record[4], record[6],
                        record[8],
                        record[9]))
                    count += 1

                    conn.commit()

# END displaying the tree view

            fetch_to_tree()

# select and fill the entry boxes
            def select_record(e):
                stu_entry_firstname.delete(0,END)
                stu_entry_lastname.delete(0,END)
                stu_entry_email.delete(0,END)
                stu_entry_dob.delete(0,END)
                stu_entry_contact.delete(0,END)
                stu_entry_address.delete(0,END)
                stu_entry_hourly_rate.delete(0,END)

                #grab record number
                selected = my_tree.focus()
                #grab record values
                values = my_tree.item(selected,'values')

                #output to entries
                stu_entry_firstname.insert(0,values[1])
                stu_entry_lastname.insert(0,values[2])
                stu_entry_email.insert(0,values[3])
                stu_entry_dob.insert(0,values[5])
                stu_entry_contact.insert(0,values[7])
                stu_entry_address.insert(0,values[4])
                stu_entry_hourly_rate.insert(0,values[9])
                global selected_student_id
                selected_student_id= values[0]
                if values[6]=="Male":
                    genderInt.set(1)
                else:
                    genderInt.set(0)

                if values[8]=="Waltz":
                    cmb.current(0)
                elif values[8]=="Jive":
                    cmb.current(1)
                elif values[8]=="ChaCha":
                    cmb.current(2)
                elif values[8]=="Samba":
                    cmb.current(3)

# adding students to the database
            def add_student_record():
                first_name = stu_entry_firstname.get()
                lastname = stu_entry_lastname.get()
                email = stu_entry_email.get()
                gender = ''
                dob = stu_entry_dob.get()
                contact = stu_entry_contact.get()
                address = stu_entry_address.get()
                hrate = stu_entry_hourly_rate.get()
                stu_style = cmb.get()

                if genderInt.get()==1:
                    gender="Male"
                else:
                    gender="Female"

                if first_name=='' or lastname=='' or email=='' or dob=='' or contact=='' or address=='' or hrate=='':
                    messagebox.showerror(title="Error", message="All field must filled")
                else:
                    create_db.c.execute(
                        f"INSERT INTO students('first_name','last_name','email','gender','dob','contact','address',style,hrate) VALUES('{first_name}','{lastname}','{email}','{gender}','{dob}','{contact}','{address}','{stu_style}','{hrate}')")
                    create_db.conn.commit()


                    stu_entry_firstname.delete(0, END)
                    stu_entry_firstname.delete(0, END)
                    stu_entry_lastname.delete(0, END)
                    stu_entry_email.delete(0, END)
                    stu_entry_dob.delete(0, END)
                    stu_entry_contact.delete(0, END)
                    stu_entry_address.delete(0, END)
                    stu_entry_hourly_rate.delete(0, END)

                    print("Record has been added successfully")

                    #clear tree view table
                    my_tree.delete(*my_tree.get_children())
                    #pull data again from database to tree view
                    fetch_to_tree()
# END adding students to the database


            def delete_student():
                global selected_student_id
                conn = sqlite3.connect('dance_feet.db')
                c = conn.cursor()

                c.execute(
                    f"DELETE FROM students WHERE student_id={selected_student_id}")
                conn.commit()
                my_tree.delete(*my_tree.get_children())
                fetch_to_tree()



            def update_student():
                conn = sqlite3.connect('dance_feet.db')
                c = conn.cursor()

                first_name = stu_entry_firstname.get()
                lastname = stu_entry_lastname.get()
                email = stu_entry_email.get()
                gender = ''
                dob = stu_entry_dob.get()
                contact = stu_entry_contact.get()
                address = stu_entry_address.get()
                hrate = stu_entry_hourly_rate.get()
                stu_style = cmb.get()

                if genderInt.get()==1:
                    gender="Male"
                else:
                    gender="Female"
                global selected_student_id
                c.execute(f"UPDATE students SET first_name='{first_name}',last_name='{lastname}',email='{email}',dob='{dob}',contact='{contact}',address='{address}',gender='{gender}',style='{stu_style}',hrate='{hrate}' WHERE student_id='{selected_student_id}'")

                conn.commit()
                my_tree.delete(*my_tree.get_children())
                fetch_to_tree()

            my_tree.bind("<Double 1>",select_record)


            Button(detail_frame_student, text="Add Record", padx=5, pady=5,command=add_student_record).place(x=5,y=680)
            Button(detail_frame_student, text="Update Record", padx=5, pady=5,command=update_student).place(x=135,y=680)
            Button(detail_frame_student, text="Delete Record", padx=5, pady=5,command=delete_student).place(x=285,y=680)

        student_registration_tab()



        def instructor_registration_tab():
            Label(detail_frame_instructor, text="Name", padx=20, pady=20, font=("calibri", 15)).grid(row=0, column=0)
            ins_entry_name=Entry(detail_frame_instructor, font=("calibri", 15))
            ins_entry_name.grid(row=0, column=1)

            Label(detail_frame_instructor, text="Password", font=("calibri", 15), padx=20, pady=20).grid(row=1, column=0)
            ins_entry_password=Entry(detail_frame_instructor, font=("calibri", 15))
            ins_entry_password.grid(row=1, column=1)

            Label(detail_frame_instructor, text="Gender", font=("calibri", 15), padx=10, pady=20).grid(row=2, column=0)

            radiobtn = Radiobutton(detail_frame_instructor, text='male', value=1,variable=genderInt)
            radiobtn.grid(row=2, column=1, sticky="NW", pady=10)

            radiobtn = Radiobutton(detail_frame_instructor, text='female', value=0,variable=genderInt)
            radiobtn.grid(row=2, column=1, sticky="SW")

            Label(detail_frame_instructor, text="Styles", font=("calibri", 15), padx=20, pady=20).grid(row=3, column=0)
            cmb_styles = ttk.Combobox(detail_frame_instructor, value=styles, width=10, font=("calibri", 12))
            cmb_styles.grid(row=3, column=1)
            cmb_styles.current(0)

            Label(detail_frame_instructor, text="Tel", font=("calibri", 15), padx=20, pady=20).grid(row=4, column=0)
            ins_entry_contact=Entry(detail_frame_instructor, font=("calibri", 15))
            ins_entry_contact.grid(row=4, column=1)

            Label(detail_frame_instructor, text="H/Rate", font=("calibri", 15), padx=20, pady=20).grid(row=5, column=0)
            ins_entry_hrate=Entry(detail_frame_instructor, font=("calibri", 15))
            ins_entry_hrate.grid(row=5, column=1)


            Label(detail_frame_instructor, text="Availability", font=("calibri", 15), padx=20, pady=20).grid(row=6,column=0)
            cmb_availability = ttk.Combobox(detail_frame_instructor, value=days, width=10, font=("calibri", 12))
            cmb_availability.grid(row=6, column=1)
            cmb_availability.current(0)

            # ins_entry_availability=Entry(detail_frame_instructor, font=("calibri", 15))
            # ins_entry_availability.grid(row=6, column=1)

            Label(detail_frame_instructor, text="", font=("calibri", 15), padx=10, pady=5).grid(row=7, column=0)

            # displaying the tree view
            my_tree = ttk.Treeview(preview_pane_instructor, height=36)
            # define columns
            my_tree['columns'] = (
                "Instructor ID", "Name", "Password", "Gender", "Styles","Contact", "Availability","H/Rate")

            # format columns
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Instructor ID", anchor=CENTER, width=80)
            my_tree.column("Name", anchor=W, width=80)
            my_tree.column("Password", anchor=W, width=80)
            my_tree.column("Gender", anchor=CENTER, width=120)
            my_tree.column("Styles", anchor=CENTER, width=120)
            my_tree.column("Contact", anchor=CENTER, width=120)
            my_tree.column("Availability", anchor=CENTER, width=80)
            my_tree.column("H/Rate", anchor=CENTER, width=80)

            # creating heading
            my_tree.heading("#0", text="", anchor=CENTER)
            my_tree.heading("Instructor ID", text="Instructor ID", anchor=CENTER)
            my_tree.heading("Name", text="Name", anchor=W)
            my_tree.heading("Password", text="Password", anchor=W)
            my_tree.heading("Gender", text="Gender", anchor=CENTER)
            my_tree.heading("Styles", text="Styles", anchor=CENTER)
            my_tree.heading("Contact", text="Contact", anchor=CENTER)
            my_tree.heading("Availability", text="Availability", anchor=CENTER)
            my_tree.heading("H/Rate", text="Hourly Rate", anchor=CENTER)
            my_tree.place(x=20, y=20)

            # select record from the treeview

            # fetch from the database to the tree view
            def fetch_to_tree():
                conn = sqlite3.connect('dance_feet.db')
                c = conn.cursor()
                c.execute("SELECT * FROM instructors")
                records = c.fetchall()

                global count
                count = 0

                for record in records:
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(
                        record[0], record[1], record[2], record[3], record[4], record[5], record[6],record[7]))
                    count += 1

                    conn.commit()

            # END displaying the tree view
            fetch_to_tree()

            # select and fill the entry boxes
            def select_instructor_record(e):
                ins_entry_name.delete(0, END)
                ins_entry_hrate.delete(0, END)
                ins_entry_contact.delete(0, END)
                ins_entry_password.delete(0, END)
                global selected_instructor_id
                # grab record number
                selected = my_tree.focus()
                # grab record values
                values = my_tree.item(selected, 'values')
                selected_instructor_id = values[0]
                # output to entries
                ins_entry_name.insert(0, values[1])
                ins_entry_password.insert(0, values[2])
                ins_entry_hrate.insert(0, values[7])
                ins_entry_contact.insert(0, values[5])
                # global selected_student_id
                # selected_student_id = values[0]
                if values[3] == "Male":
                    genderInt.set(1)
                else:
                    genderInt.set(0)

                if values[4] == "Waltz":
                    cmb_styles.current(0)
                elif values[4] == "Jive":
                    cmb_styles.current(1)
                elif values[4] == "ChaCha":
                    cmb_styles.current(2)
                elif values[4] == "Samba":
                    cmb_styles.current(3)


                if values[6] == "Monday":
                    cmb_availability.current(0)
                elif values[6] == "Tuesday":
                    cmb_availability.current(1)
                elif values[6] == "Wednesday":
                    cmb_availability.current(2)
                elif values[6] == "Thursday":
                    cmb_availability.current(3)
                elif values[6] == "Friday":
                    cmb_availability.current(4)
                elif values[6] == "Saturday":
                    cmb_availability.current(5)
                elif values[6] == "Sunday":
                    cmb_availability.current(6)


            # adding students to the database
            def add_instructor_record():
                name = ins_entry_name.get()
                password = ins_entry_password.get()
                gender = ''
                ins_style = cmb_styles.get()
                contact = ins_entry_contact.get()
                hrate = ins_entry_hrate.get()
                ins_available = cmb_availability.get()

                if genderInt.get() == 1:
                    gender = "Male"
                else:
                    gender = "Female"

                if name == '' or password == '' or gender == '' or ins_style == '' or contact == '' or hrate == '' or ins_available == '':
                    messagebox.showerror(title="Error", message="All field must filled")
                else:
                    create_db.c.execute(
                        f"INSERT INTO instructors('name','password','gender','styles','contact','available','hrate') VALUES('{name}','{password}','{gender}','{ins_style}','{contact}','{ins_available}','{hrate}')")
                    create_db.conn.commit()

                    ins_entry_name.delete(0, END)
                    ins_entry_hrate.delete(0, END)
                    ins_entry_contact.delete(0, END)
                    ins_entry_password.delete(0, END)

                    print("Record has been added successfully")

                    # clear tree view table
                    my_tree.delete(*my_tree.get_children())
                    # pull data again from database to tree view
                    fetch_to_tree()

            # END adding students to the database

            def delete_instructor():
                global selected_instructor_id
                conn = sqlite3.connect('dance_feet.db')
                c = conn.cursor()
                c.execute(
                    f"DELETE FROM instructors WHERE ins_id='{selected_instructor_id}'")
                conn.commit()
                my_tree.delete(*my_tree.get_children())
                fetch_to_tree()

            def update_instructor():
                global selected_instructor_id
                conn = sqlite3.connect('dance_feet.db')
                c = conn.cursor()
                name = ins_entry_name.get()
                password = ins_entry_password.get()
                gender = ''
                ins_style = cmb_styles.get()
                contact = ins_entry_contact.get()
                hrate = ins_entry_hrate.get()
                ins_available = cmb_availability.get()

                if genderInt.get() == 1:
                    gender = "Male"
                else:
                    gender = "Female"

                global selected_student_id
                c.execute(
                    f"UPDATE instructors SET name='{name}',password='{password}',gender='{gender}',styles='{ins_style}',contact='{contact}',available='{ins_available}',hrate='{hrate}' WHERE ins_id='{selected_instructor_id}'")

                conn.commit()
                my_tree.delete(*my_tree.get_children())
                fetch_to_tree()

            my_tree.bind("<Double 1>", select_instructor_record)

            Button(detail_frame_instructor, text="Add Record", padx=5, pady=5,command=add_instructor_record).place(x=5,y=680)
            Button(detail_frame_instructor, text="Update Record", padx=5, pady=5,command=update_instructor).place(x=135,y=680)
            Button(detail_frame_instructor, text="Delete Record", padx=5, pady=5,command=delete_instructor).place(x=285,y=680)

        instructor_registration_tab()



        # Button(top_frame,text="Student Management",padx=5,pady=5).pack(side="left")
        # Button(top_frame,text="Instructor Management",padx=5,pady=5).pack(side="left")
        # Button(top_frame,text="Book a Lesson",padx=5,pady=5).pack(side="left")



        window.mainloop()


admin_GUI()


