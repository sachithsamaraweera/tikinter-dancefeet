from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from database_conn import create_db
def instructor_registration_tab(detail_frame_instructor,styles,preview_pane_instructor,genderInt,days):
    Label(detail_frame_instructor, text="Name", padx=20, pady=20, font=("calibri", 15)).grid(row=0, column=0)
    ins_entry_name =Entry(detail_frame_instructor, font=("calibri", 15))
    ins_entry_name.grid(row=0, column=1)

    Label(detail_frame_instructor, text="Password", font=("calibri", 15), padx=20, pady=20).grid(row=1, column=0)
    ins_entry_password =Entry(detail_frame_instructor, font=("calibri", 15))
    ins_entry_password.grid(row=1, column=1)

    Label(detail_frame_instructor, text="Gender", font=("calibri", 15), padx=10, pady=20).grid(row=2, column=0)

    radiobtn = Radiobutton(detail_frame_instructor, text='male', value=1 ,variable=genderInt)
    radiobtn.grid(row=2, column=1, sticky="NW", pady=10)

    radiobtn = Radiobutton(detail_frame_instructor, text='female', value=0 ,variable=genderInt)
    radiobtn.grid(row=2, column=1, sticky="SW")

    Label(detail_frame_instructor, text="Styles", font=("calibri", 15), padx=20, pady=20).grid(row=3, column=0)
    cmb_styles = ttk.Combobox(detail_frame_instructor, value=styles, width=10, font=("calibri", 12))
    cmb_styles.grid(row=3, column=1)
    cmb_styles.current(0)

    Label(detail_frame_instructor, text="Tel", font=("calibri", 15), padx=20, pady=20).grid(row=4, column=0)
    ins_entry_contact =Entry(detail_frame_instructor, font=("calibri", 15))
    ins_entry_contact.grid(row=4, column=1)

    Label(detail_frame_instructor, text="H/Rate", font=("calibri", 15), padx=20, pady=20).grid(row=5, column=0)
    ins_entry_hrate =Entry(detail_frame_instructor, font=("calibri", 15))
    ins_entry_hrate.grid(row=5, column=1)

    Label(detail_frame_instructor, text="Availability", font=("calibri", 15), padx=20, pady=20).grid(row=6 ,column=0)
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
        "Instructor ID", "Name", "Password", "Gender", "Styles" ,"Contact", "Availability" ,"H/Rate")

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
                record[0], record[1], record[2], record[3], record[4], record[5], record[6] ,record[7]))
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

            create_db.c.execute(
                f"INSERT INTO users('username','password','level') VALUES('{name}','{password}','2')")
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

    def refresh():
        ins_entry_name.delete(0, END)
        ins_entry_hrate.delete(0, END)
        ins_entry_contact.delete(0, END)
        ins_entry_password.delete(0, END)
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

    Button(detail_frame_instructor, text="Add Record", padx=5, pady=5 ,command=add_instructor_record).place(x=5 ,y=620)
    Button(detail_frame_instructor, text="Update Record", padx=5, pady=5 ,command=update_instructor).place(x=135 ,y=620)
    Button(detail_frame_instructor, text="Refresh", padx=5, pady=5, command=refresh).place(x=140, y=670)
    Button(detail_frame_instructor, text="Delete Record", padx=5, pady=5 ,command=delete_instructor).place(x=285 ,y=620)
