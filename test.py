import tkinter as tk

root = tk.Tk()
root.geometry("900x600")

treeview_frame = tk.Frame(root, background="#FFF0C1", bd=1, relief="sunken")
graph_frame = tk.Frame(root, background="#D2E2FB", bd=1, relief="sunken")
text_frame = tk.Frame(root, background="#CCE4CA", bd=1, relief="sunken")
button_frame = tk.Frame(root, background="#F5C2C1", bd=1, relief="sunken")

treeview_frame.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
graph_frame.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
text_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=2, pady=2)
button_frame.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=2, pady=2)

root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=2)

root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=2)
root.grid_columnconfigure(2, weight=3)

root.mainloop()