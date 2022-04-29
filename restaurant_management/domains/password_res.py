
from tkinter import *
from tkinter import messagebox,ttk
import order as o
import routeadmin as ra


pass_word_list =["st21","ad21"]

#staff acces    
def switch_to_staff(container,frame):
    frame.grid_forget()
    o.order_frame(container)

#admin access

def admin_access(container,frame):
    frame.grid_forget()
    ra.admin_access(container).grid(column=0, row=0)
    
#login validation
def login_validate(pget,container,frame):
    if  pget== pass_word_list[0]:
        switch_to_staff(container,frame)
        
    elif pget == pass_word_list[1]:
        admin_access(container,frame)
    
    else:
        messagebox.showinfo("Error", "Invalid Password")

def create_frame(container):
    container.columnconfigure(0, weight=1)
    container.rowconfigure(1, weight=2)
    frame = ttk.Frame(container)
    label = Label(frame, text="           Password Generator", font=("Arial Bold", 20))
    label.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

    #Password entry
    pass_label = Label(frame,text = "Enter the password: ", font=("Arial Bold", 12))
    pass_label.grid(column = 0, row = 1,sticky = W)

    pass_entry = Entry(frame, width =30,show = "*")
    pass_entry.get()
    pass_entry.grid(column = 1, row = 1,sticky = E)

    #Button login and exit
    login_button  = Button(frame, text="Login", command =lambda:login_validate(pass_entry.get(),container, frame))
    login_button.grid(column = 0, row = 3,columnspan=4)
    
    exit_button = Button(frame, text="Exit", command = container.destroy)
    exit_button.grid(column = 1, row = 3,columnspan=4)
    return frame


def main_window():
    root = Tk()
    root.resizable(True, True)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.title("WELCOME")
    sg = ttk.Sizegrip(root)
    sg.grid(column=1, row=1, sticky=(S, E))
    frame_buttons = create_frame(root)
    frame_buttons.grid(column=0, row=0, sticky=(N, W, E, S))
    root.mainloop()

if __name__ == "__main__":
    main_window()








