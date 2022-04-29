from tkinter import *
from tkinter import ttk
import employeem as e
import billmanagement as b

def to_employeemanagement(container,frame):
    frame.grid_forget()
    e.employeemanagement_frame(container).grid(column=0, row=0)

def to_billmanagement(container,frame):
    frame.grid_forget()
    b.billmanagement_frame(container).grid(column=0, row=0)


def foodmanagement_frame(container):
    container.columnconfigure(0, weight=1)
    container.rowconfigure(1, weight=2)
    frame = ttk.Frame(container)
    label = Label(frame, text="           Food management", font=("Arial Bold", 20))
    label.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

    button1 = ttk.Button(frame, text="Employee management", command=lambda: to_employeemanagement(container,frame))
    button1.grid(column=0, row=1, padx=5, pady=5)

    button2 = ttk.Button(frame, text="Bill management", command=lambda: to_billmanagement(container,frame)) 
    button2.grid(column=1, row=1, padx=5, pady=5)

    button3 = ttk.Button(frame, text = "Exit", command = container.destroy)
    button3.grid(column=2, row=1, padx=5, pady=5)

    return frame