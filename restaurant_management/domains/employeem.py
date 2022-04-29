from tkinter import *
from tkinter import ttk
import foodm as f
import billmanagement as b

def to_billmanagement(container,frame):
    frame.grid_forget()
    b.billmanagement_frame(container).grid(column=0, row=0)

def to_foodmanagement(container,frame):
    frame.grid_forget()
    f.foodmanagement_frame(container).grid(column=0, row=0)

def employeemanagement_frame(container):
    frame = ttk.Frame(container)
    label = Label(frame, text="           Employee Management", font=("Arial Bold", 20))
    label.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
    button_ordermanagement = ttk.Button(frame, text="Bill Management",command = lambda: to_billmanagement(container,frame))
    button_ordermanagement.grid(column=0, row=1, padx=5, pady=5)

    button_billmanagement = ttk.Button(frame, text="Food Management",command = lambda: to_foodmanagement(container,frame))
    button_billmanagement.grid(column=1, row=1, padx=5, pady=5)

    button3 = ttk.Button(frame, text = "Exit", command = container.destroy)
    button3.grid(column=2, row=1, padx=5, pady=5)

    return frame

