
import tkinter as tk
from tkinter import ttk

from tkinter import *
import tkinter as tk
from tkinter import Tk, StringVar,ttk
import bill as b

table = {}


def select_food():
    pass


def switch_to_bill(container,frame):
    frame.grid_forget()
    b.bill_frame(container).grid(column=0, row=0)

def order_frame(container):
    table = [Label(container, text="Table 1"), Label(container, text="Table 2"), Label(container, text="Table 3"), Label(container, text="Table 4"), Label(container, text="Table 5"), Label(container, text="Table 6"), Label(container, text="Table 7"), Label(container, text="Table 8"), Label(container, text="Table 9"), Label(container, text="Table 10")]
    frame_label = Label(container, text="Ỏder", font=("Arial Bold", 20))
    frame_label.grid(column=0,row=0,columnspan=2)

    Menu = Frame(container, bd=12, relief='raise',width=200,height=200)
    Menu.grid(column=0, row=1,sticky=W,pady=100)

    f1 = Frame(Menu, bd=1, relief='raise',)#main
    f1.grid(column=0, row=0)
    f2 = Frame(Menu , bd=1, relief='raise')#extra
    f2.grid(column=1, row=0, sticky=W)
    f3 = Frame(Menu , bd=1, relief='raise')#drink
    f3.grid(column=0, row=1, sticky=W)

    Note = Frame(Menu, relief='raise')
    Note.grid(column=1, row=1,sticky=N)
    
    Seat = Frame(container,bd =12 ,relief="raise",width=200,height=200)
    Seat.grid(column=1, row=1,sticky=N,pady=100)

    

    var1 = IntVar().set(0) #phobo
    var2 = IntVar().set(0) #phoga
    var3 = IntVar().set(0) #phoxaobo
    var4 = IntVar().set(0) #photron
    var5 = IntVar().set(0) #phocuon
    var6 = IntVar().set(0) #comrang
    var7 = IntVar().set(0) #trada
    var8 = IntVar().set(0) #suaDau
    var9 = IntVar().set(0) #suaNgo
    var10 = IntVar().set(0) #coca
    var11 = IntVar().set(0) #pepsi 
    var12 = IntVar().set(0) #nuocloc
    var13 = IntVar().set(0) #quay
    var14 = IntVar().set(0) #trungtran
    var15 = IntVar().set(0) #trungnon
    var16 = IntVar().set(0) #extra
    var17 = IntVar().set(0)
    var18 = IntVar().set(0)
    
    #Main Menu
    varphoBo = StringVar().set("0")
    varphoGa = StringVar().set("0")
    varphoXaobo = StringVar().set("0")
    varphoTron = StringVar().set("0")
    varphoCuon = StringVar().set("0")
    varcomRang = StringVar().set("0")

    #Drinks
    vartraDa = StringVar().set("0")
    varsuaDau = StringVar().set("0")
    varsuaNgo = StringVar().set("0")
    varcoCa = StringVar().set("0")
    varpepSi = StringVar().set("0")
    varnuocLoc = StringVar().set("0")

    #Topping
    varQuay = StringVar().set("0")
    vartrungTran = StringVar().set("0")
    vartrungNon = StringVar().set("0")
    varExtra = StringVar().set("0")
    varExtrapho = StringVar().set("0")
    varExtracanh = StringVar().set("0")

    
    tk.Label(f1, text="    Main Dish", font=('arial', 32, 'bold')) .grid(row=0, column=0)
    phoBo = Checkbutton(f1, text="Pho bo  $50", variable=var1, onvalue=1, offvalue=0, font=('arial', 16 )).grid(row=1, sticky=W)
    txtphoBo = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoBo, width=6, justify='right', state=DISABLED)
    txtphoBo.grid(row=1, column=1,sticky = E)

    phoGa = Checkbutton(f1, text="Pho ga   $50", variable=var2, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=3, sticky=W)
    txtphoGa = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoGa, width=6, justify='right', state=DISABLED)
    txtphoGa.grid(row=3, column=1)

    phoXaobo = Checkbutton(f1, text="Pho xao bo   $50", variable=var3, onvalue=1, offvalue=0, font=('arial', 16 )).grid(row=5, sticky=W)
    txtphoXaobo = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoXaobo, width=6, justify='right', state=DISABLED)
    txtphoXaobo.grid(row=5, column=1)

    phoTron = Checkbutton(f1, text="Pho tron   $50", variable=var4, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=7, sticky=W)
    txtphoTron = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoTron, width=6, justify='right', state=DISABLED)
    txtphoTron.grid(row=7, column=1)

    phoCuon = Checkbutton(f1, text="Pho bo   $50", variable=var5, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=9, sticky=W)
    txtphoCuon = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoCuon, width=6, justify='right', state=DISABLED)
    txtphoCuon.grid(row=9, column=1)

    comRang = Checkbutton(f1, text="Com rang   $50", variable=var6, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=11, sticky=W)
    txtcomRang = Entry(f1, font=('arial', 16, 'bold'), textvariable=varcomRang, width=6, justify='right', state=DISABLED)
    txtcomRang.grid(row=11, column=1)

    tk.Label(f2, text="Topping", font=('arial', 32, 'bold')).grid(row=0, column=0)

    Quay = Checkbutton(f2, text="Quay   $50", variable=var13, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=1, sticky=W)
    txtQuay = Entry(f2, font=('arial', 16, 'bold'), textvariable=varQuay, width=6, justify='right', state=DISABLED)
    txtQuay.grid(row=1, column=1)

    trungTran = Checkbutton(f2, text="Trung tran   $50", variable=var14, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=3, sticky=W)
    txttrungTran = Entry(f2, font=('arial', 16, 'bold'), textvariable=vartrungTran, width=6, justify='right', state=DISABLED)
    txttrungTran.grid(row=3, column=1)

    trungNon = Checkbutton(f2, text="Trung tran   $50", variable=var15, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=5, sticky=W)
    txttrungNon = Entry(f2, font=('arial', 16, 'bold'), textvariable=vartrungNon, width=6, justify='right', state=DISABLED)
    txttrungNon.grid(row=5, column=1)

    Extra = Checkbutton(f2, text="Them bo/ga   $50", variable=var16, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=7, sticky=W)
    txtExtra = Entry(f2, font=('arial', 16, 'bold'), textvariable=varExtra, width=6, justify='right', state=DISABLED)
    txtExtra.grid(row=7, column=1)

    Extrapho = Checkbutton(f2, text="Them pho   $50", variable=var17, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=9, sticky=W)
    txtExtrapho = Entry(f2, font=('arial', 16, 'bold'), textvariable=varExtrapho, width=6, justify='right', state=DISABLED)
    txtExtrapho.grid(row=9, column=1)

    Extracanh = Checkbutton(f2, text="Them canh   $50", variable=var18, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=11, sticky=W)
    txtExtracanh = Entry(f2, font=('arial', 16, 'bold'), textvariable=varExtracanh, width=6, justify='right', state=DISABLED)
    txtExtracanh.grid(row=11, column=1)

    

    tk.Label(f3, text="Drinks", font=('arial', 32, 'bold')) .grid(row=0, column=3,columnspan=2)

    traDa = Checkbutton(f3, text="Tra da   $50", variable=var7, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=1, column = 3, sticky=W)
    txttraDa = Entry(f3, font=('arial', 16, 'bold'), textvariable=vartraDa, width=6, justify='right', state=DISABLED)
    txttraDa.grid(row=1, column=4)

    suaDau = Checkbutton(f3, text="Sua dau   $50", variable=var8, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=3,column = 3, sticky=W)
    txtsuaDau = Entry(f3, font=('arial', 16, 'bold'), textvariable=varsuaDau, width=6, justify='right', state=DISABLED)
    txtsuaDau.grid(row=3, column=4)

    suaNgo = Checkbutton(f3, text="Sua ngo  $50", variable=var9, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=5,column = 3, sticky=W)
    txtsuaNgo = Entry(f3, font=('arial', 16, 'bold'), textvariable=varsuaNgo, width=6, justify='right', state=DISABLED)
    txtsuaNgo.grid(row=5, column=4)

    coCa = Checkbutton(f3, text="Coca cola   $50", variable=var10, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=7,column = 3, sticky=W)
    txtcoCa = Entry(f3, font=('arial', 16, 'bold'), textvariable=varcoCa, width=6, justify='right', state=DISABLED)
    txtcoCa.grid(row=7, column=4)

    pepSi = Checkbutton(f3, text="Pepsi   $50", variable=var11, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=9,column = 3, sticky=W)
    txtpepSi = Entry(f3, font=('arial', 16, 'bold'), textvariable=varpepSi, width=6, justify='right', state=DISABLED)
    txtpepSi.grid(row=9, column=4)

    nuocLoc = Checkbutton(f3, text="Nuoc loc   $50", variable=var12, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=11,column = 3, sticky=W)
    txtnuocLoc = Entry(f3, font=('arial', 16, 'bold'), textvariable=varnuocLoc, width=6, justify='right', state=DISABLED)
    txtnuocLoc.grid(row=11, column=4)

    tk.Label(Note, text="Order Note", font=('arial', 32, 'bold')).grid(row=0, column=0)
    txtNote = Text(Note, font=('arial', 16, 'bold'), width=20, height=8)
    txtNote.grid(row=1, column=0)

    tk.Label(Seat, text="SEAT", font=('arial', 32, 'bold')).grid(row=0, column=0)
    for i in range(1,4):
            for j in range(1,7):
                table[i] = Button(Seat, text='table {} {}'.format(i, j))
                table[i].grid(column=i, row=j,padx=5, pady=5)
    
    
    
    
        

        




    
