from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox


class instructor_GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1400x1000")
        self.window.title("Instructor")

        title = Label(self.window,text="DanceFeet Instructor Login",font=("Arial",25),border=5,relief=SUNKEN,bg="#F5C2C1")
        title.pack(side=TOP,fill=X)

        mainframe = Frame(self.window,border=5,relief=SUNKEN)
        mainframe.place(x=5, y=50, width=1390, height=1000)

        detail_frame_instructor_login =  LabelFrame(self.window,text="Enter details",font=("Arial",20),border=5,relief=SUNKEN)
        detail_frame_instructor_login.place(x=20,y=60,width=400,height=800)

        preview_pane_instructor_login =  LabelFrame(self.window,text="View details",font=("Arial",20),border=5,relief=SUNKEN)
        preview_pane_instructor_login.place(x=420,y=60,width=1000,height=800)



        gender = ["male","female"]
        styles = ["Waltz", "Jive", "ChaCha", "Samba"]

        lesson_booking_student_id = 0
        matching_instructors_count = 0
        Label(detail_frame_instructor_login, text="First Name", padx=20, pady=20, font=("calibri", 15)).grid(row=0,
                                                                                                           column=0)
        lbooking_entry_firstname = Entry(detail_frame_instructor_login, font=("calibri", 15))
        lbooking_entry_firstname.grid(row=0, column=1)

        Label(detail_frame_instructor_login, text="Last Name", font=("calibri", 15), padx=20, pady=20).grid(row=1,
                                                                                                          column=0)
        lbooking_entry_lastname = Entry(detail_frame_instructor_login, font=("calibri", 15))
        lbooking_entry_lastname.grid(row=1, column=1)

        Label(detail_frame_instructor_login, text="Email", font=("calibri", 15), padx=20, pady=20).grid(row=2, column=0)
        lbooking_entry_email = Entry(detail_frame_instructor_login, font=("calibri", 15))
        lbooking_entry_email.grid(row=2, column=1)

        Label(detail_frame_instructor_login, text="Contact No", font=("calibri", 15), padx=20, pady=20).grid(row=3,
                                                                                                           column=0)
        lbooking_entry_contact = Entry(detail_frame_instructor_login, font=("calibri", 15))
        lbooking_entry_contact.grid(row=3, column=1)

        Label(detail_frame_instructor_login, text="Styles", font=("calibri", 15), padx=20, pady=20).grid(row=4, column=0)
        cmb_styles = ttk.Combobox(detail_frame_instructor_login, value=styles, width=10, font=("calibri", 12))
        cmb_styles.grid(row=4, column=1)
        cmb_styles.current(0)

        Label(detail_frame_instructor_login, text="Instructor", font=("calibri", 15), padx=20, pady=20).grid(row=5,
                                                                                                           column=0)
        cmb_instructors = ttk.Combobox(detail_frame_instructor_login, width=10, font=("calibri", 12))
        cmb_instructors.grid(row=5, column=1)

        Label(detail_frame_instructor_login, text="H/rate", font=("calibri", 15), padx=20, pady=20).grid(row=6, column=0)
        lbooking_entry_hourly_rate = Entry(detail_frame_instructor_login, font=("calibri", 15))
        lbooking_entry_hourly_rate.grid(row=6, column=1)

        # displaying the student tree view
        my_tree = ttk.Treeview(preview_pane_instructor_login, height=35)
        # define columns
        my_tree['columns'] = (
            "Student ID", "First Name", "Last Name", "Email", "Contact No", "Style", "H/rate", "Instructor")

        # format columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Student ID", anchor=CENTER, width=80)
        my_tree.column("First Name", anchor=W, width=80)
        my_tree.column("Last Name", anchor=W, width=80)
        my_tree.column("Email", anchor=CENTER, width=120)
        my_tree.column("Contact No", anchor=CENTER, width=120)
        my_tree.column("Style", anchor=CENTER, width=80)
        my_tree.column("H/rate", anchor=CENTER, width=80)
        my_tree.column("Instructor", anchor=CENTER, width=80)

        # creating heading
        my_tree.heading("#0", text="", anchor=CENTER)
        my_tree.heading("Student ID", text="Student ID", anchor=CENTER)
        my_tree.heading("First Name", text="First Name", anchor=W)
        my_tree.heading("Last Name", text="Last Name", anchor=W)
        my_tree.heading("Email", text="Email", anchor=CENTER)
        my_tree.heading("Contact No", text="Contact No", anchor=CENTER)
        my_tree.heading("Style", text="Style", anchor=CENTER)
        my_tree.heading("H/rate", text="H/rate", anchor=CENTER)
        my_tree.heading("Instructor", text="Instructor", anchor=CENTER)
        my_tree.place(x=20, y=20)

        # select record from the treeview

        # fetch from the database to the tree view
        def fetch_to_tree():
            conn = sqlite3.connect('dance_feet.db')
            c = conn.cursor()
            c.execute("SELECT * FROM students")
            records = c.fetchall()

            global count
            count = 0

            for record in records:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(
                    record[0], record[1], record[2], record[3], record[6], record[8], record[9], record[10]))
                count += 1

                conn.commit()

        # END displaying the tree view

        fetch_to_tree()

        def select_booking_records(e):

            lbooking_entry_email.delete(0, END)
            lbooking_entry_lastname.delete(0, END)
            lbooking_entry_contact.delete(0, END)
            lbooking_entry_firstname.delete(0, END)
            lbooking_entry_hourly_rate.delete(0, END)

            # grab record number
            selected = my_tree.focus()
            # grab record values
            values = my_tree.item(selected, 'values')

            # output to entries
            lbooking_entry_firstname.insert(0, values[1])
            lbooking_entry_lastname.insert(0, values[2])
            lbooking_entry_email.insert(0, values[3])
            lbooking_entry_contact.insert(0, values[4])
            lbooking_entry_hourly_rate.insert(0, values[6])

            stu_hourly_rate = values[6]
            global lesson_booking_student_id
            global matching_instructors_count
            lesson_booking_student_id = values[0]

            lbooking_student_style = ""

            if values[5] == "Waltz":
                cmb_styles.current(0)
                lbooking_student_style = "Waltz"
            elif values[5] == "Jive":
                cmb_styles.current(1)
                lbooking_student_style = "Jive"
            elif values[5] == "ChaCha":
                cmb_styles.current(2)
                lbooking_student_style = "ChaCha"
            elif values[5] == "Samba":
                cmb_styles.current(3)
                lbooking_student_style = "Samba"

            conn = sqlite3.connect('dance_feet.db')
            c = conn.cursor()
            c.execute(
                f"SELECT name,hrate FROM instructors WHERE hrate<='{stu_hourly_rate}' AND styles='{lbooking_student_style}'")
            records = c.fetchall()
            avail_instructors = []
            if len(records) != 0:
                matching_instructors_count = 1
                for record in records:
                    avail_instructors.append(record[0])
            else:
                matching_instructors_count = 0
                avail_instructors.append('None')

            cmb_instructors.configure(values=avail_instructors)
            cmb_instructors.current(0)

        def add_lessons():
            global lesson_booking_student_id
            global matching_instructors_count

            if matching_instructors_count != 0:
                conn = sqlite3.connect('dance_feet.db')
                c = conn.cursor()

                c.execute(
                    f"UPDATE students SET instructor='{cmb_instructors.get()}' WHERE student_id='{lesson_booking_student_id}'")

                conn.commit()
                my_tree.delete(*my_tree.get_children())
                fetch_to_tree()
                messagebox.showinfo(title="success",message="Lesson Booked successfully")
            else:
                messagebox.showerror(title="Error", message="Unable to book a lesson - No matching instructors found")

        def refresh():
            lbooking_entry_email.delete(0, END)
            lbooking_entry_lastname.delete(0, END)
            lbooking_entry_contact.delete(0, END)
            lbooking_entry_firstname.delete(0, END)
            lbooking_entry_hourly_rate.delete(0, END)
            my_tree.delete(*my_tree.get_children())
            fetch_to_tree()

        def remove_booked_lessons():
            global lesson_booking_student_id
            global matching_instructors_count
            if matching_instructors_count != 0:
                conn = sqlite3.connect('dance_feet.db')
                c = conn.cursor()
                c.execute(f"UPDATE students SET instructor='None' WHERE student_id='{lesson_booking_student_id}'")

                conn.commit()
                my_tree.delete(*my_tree.get_children())
                fetch_to_tree()
            else:
                messagebox.showerror(title="Error",
                                     message="Cannot Remove booked lessons - No instructors was assigned")

        my_tree.bind("<Double 1>", select_booking_records)

        Button(detail_frame_instructor_login, text="Book Lesson", padx=5, pady=5, command=add_lessons).place(x=5, y=580)
        Button(detail_frame_instructor_login, text="Remove Booked Lesson", padx=5, pady=5,
               command=remove_booked_lessons).place(x=120, y=580)
        Button(detail_frame_instructor_login, text="Refresh", padx=5, pady=5, command=refresh).place(x=300, y=580)

        self.window.mainloop()




