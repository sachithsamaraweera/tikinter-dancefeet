from tkinter import *

class ins_GUI:
    def __init__(self):
        window = Tk()
        window.geometry("1000x800")
        window.title("Instructor")
        title_frame = Frame(window, bg="#F5C2C1", relief=SUNKEN)
        left_frame = Frame(window, bg="#FFF0C1", relief=SUNKEN)
        right_frame = Frame(window, bg="#D2E2FB", relief=SUNKEN)
        top_frame = Frame(window, bg="#CCE4CA", relief=SUNKEN)

        Label(title_frame, text="Instructor Login", bg="#F5C2C1", font=("calibri", 20)).pack()

        title_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
        top_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
        left_frame.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
        right_frame.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)

        window.grid_rowconfigure(0, weight=1)
        window.grid_rowconfigure(1, weight=1)
        window.grid_rowconfigure(2, weight=10)
        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=2)


