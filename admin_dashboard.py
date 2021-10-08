from tkinter import *
from tkinter import ttk
import sqlite3
import lessonbooking
import  student_registration
import instructor_registration
class admin_GUI:
    def __init__(self):
        window = Tk()
        window.geometry("1400x1000")
        window.title("Admin")

        title = Label(window,text="DanceFeet Management",font=("Arial",25),border=5,relief=SUNKEN,bg="#A4EBF3")
        title.pack(side=TOP,fill=X)

        mainframe = Frame(window,border=5,relief=SUNKEN)
        mainframe.place(x=0, y=50, width=1380, height=1000)

        notebook = ttk.Notebook(mainframe)
        tab1 = Frame(notebook)
        tab2 = Frame(notebook)
        tab3 = Frame(notebook)
        tab4 = Frame(notebook)
        notebook.add(tab1, text="Student Registration")
        notebook.add(tab2, text="Instructor Registration")
        notebook.add(tab3, text="Lesson Booking")
        notebook.add(tab4, text="Booked Lessons")
        notebook.pack(expand=True, fill="both")

        detail_frame_student =  LabelFrame(tab1,text="Enter details",font=("Arial",20),border=5,relief=SUNKEN)
        detail_frame_student.place(x=20,y=5,width=400,height=800)

        detail_frame_instructor =  LabelFrame(tab2,text="Enter details",font=("Arial",20),border=5,relief=SUNKEN)
        detail_frame_instructor.place(x=20,y=5,width=500,height=800)

        detail_frame_lesson_booking =  LabelFrame(tab3,text="Enter details",font=("Arial",20),border=5,relief=SUNKEN)
        detail_frame_lesson_booking.place(x=20,y=5,width=500,height=800)

        preview_pane_lesson_booking =  LabelFrame(tab3,text="View details",font=("Arial",20),border=5,relief=SUNKEN)
        preview_pane_lesson_booking.place(x=420,y=5,width=1000,height=800)

        preview_pane_booked_lessons =  LabelFrame(tab4,text="View details",font=("Arial",20),border=5,relief=SUNKEN)
        preview_pane_booked_lessons.place(x=10,y=5,width=1300,height=800)

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

        student_registration.student_registration_tab(detail_frame_student,styles,preview_pane,genderInt)
        # Instructor registration Starts

        # Instructor registration END
        instructor_registration.instructor_registration_tab(detail_frame_instructor,styles,preview_pane_instructor,genderInt,days)

        def booked_lessons_tab():
            # displaying the tree view
            my_tree = ttk.Treeview(preview_pane_booked_lessons, height=35)
            # define columns
            my_tree['columns'] = (
            "Student ID", "Student First Name", "Student Styles", "Student Contact", "Booked Date", "H/Rate",
            "Instructor Name", "Instructor Contact")

            # format columns
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Student ID", anchor=CENTER, width=80)
            my_tree.column("Student First Name", anchor=W, width=120)
            my_tree.column("Student Styles", anchor=W, width=80)
            my_tree.column("Student Contact", anchor=CENTER, width=120)
            my_tree.column("Booked Date", anchor=CENTER, width=120)
            my_tree.column("H/Rate", anchor=CENTER, width=120)
            my_tree.column("Instructor Name", anchor=CENTER, width=80)
            my_tree.column("Instructor Contact", anchor=CENTER, width=80)

            # creating heading
            my_tree.heading("#0", text="", anchor=CENTER)
            my_tree.heading("Student ID", text="Student ID", anchor=CENTER)
            my_tree.heading("Student First Name", text="Student First Name", anchor=W)
            my_tree.heading("Student Styles", text="Student Styles", anchor=W)
            my_tree.heading("Student Contact", text="Student Contact", anchor=W)
            my_tree.heading("Booked Date", text="Booked Date", anchor=CENTER)
            my_tree.heading("H/Rate", text="H/Rate", anchor=CENTER)
            my_tree.heading("Instructor Name", text="Instructor Name", anchor=CENTER)
            my_tree.heading("Instructor Contact", text="Instructor Contact", anchor=CENTER)
            my_tree.place(x=20, y=20, width=1200)

            def fetch_to_tree():
                conn = sqlite3.connect('dance_feet.db')
                c = conn.cursor()
                c.execute(
                    "SELECT s.student_id,s.first_name,s.style,s.contact,i.available,s.hrate,i.name,i.contact FROM students s,instructors i WHERE s.instructor = i.name")
                records = c.fetchall()
                global count
                count = 0
                for record in records:
                    my_tree.insert(parent='', index='end', iid=count, text="", values=(
                    record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]))
                    count += 1
                    conn.commit()

            # END displaying the tree view
            fetch_to_tree()

            def refresh():
                my_tree.delete(*my_tree.get_children())
                fetch_to_tree()

            Button(preview_pane_booked_lessons, text="Refresh", padx=5, pady=5, command=refresh).place(x=600, y=670)

        booked_lessons_tab()

        lessonbooking.lesson_booking_tab(detail_frame_lesson_booking,styles,preview_pane_lesson_booking)
        window.mainloop()




