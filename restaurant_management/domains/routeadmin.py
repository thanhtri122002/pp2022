from tkinter import *
from tkinter import messagebox,ttk
import billmanagement as b
import employeem as e
import foodm as f

def to_employee(container,frame):
    frame.grid_forget()
    e.employeemanagement_frame(container).grid(column=0, row=0)

def to_billmanagement(container,frame):
    frame.grid_forget()
    b.billmanagement_frame(container).grid(column=0, row=0)

def to_food(container,frame):
    frame.grid_forget()
    f.foodmanagement_frame(container).grid(column=0, row=0)

def admin_access(container):
    frame = ttk.Frame(container)
    label = Label(frame, text="           Food management", font=("Arial Bold", 20))
    label.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
    button1 = Button(frame, text="Employee ", command=lambda:to_employee(container,frame))
    button1.grid(column=0, row=1, padx=5, pady=5)
    button2 = Button(frame, text="Bills", command=lambda:to_billmanagement(container,frame))
    button2.grid(column=1, row=1, padx=5, pady=5)
    button3 = Button(frame, text="Food", command=lambda:to_food(container,frame))
    button3.grid(column=2, row=1, padx=5, pady=5)
    return frame
    
