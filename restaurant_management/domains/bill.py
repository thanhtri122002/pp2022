import tkinter as tk
from tkinter import ttk
import order as o

def switch_to_order(container,frame):
    frame.grid_forget()
    o.order_frame(container).grid(column=0, row=0)

def bill_frame(container):
    frame = ttk.Frame(container)
    label = tk.Label(frame, text="           Bill", font=("Arial Bold", 20))
    label.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
    id_label = tk.Label(frame, text="ID: ", font=("Arial Bold", 12))
    id_label.grid(column = 0, row = 1)
    order_back = ttk.Button(frame, text="Back", command = lambda: switch_to_order(container,frame))
    order_back.grid(column = 0, row = 3)

    button3 = ttk.Button(frame, text = "Exit", command = container.destroy)
    button3.grid(column=2, row=1, padx=5, pady=5)

    return frame