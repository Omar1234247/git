from tkinter import *
from tkinter import messagebox

wd = Tk()
wd.geometry("400x400")
wd.title("Is Binary")


ml = Label(wd, text="Enter your input:")
ml.place(x=100, y=100)

me = Entry(wd)
me.place(x=100, y=125)

def isbinary():
    ib = True
    
    ui = me.get()
    binary = ["2","3","4","5","6","7","8","9"]

    for i in ui:
        if i in binary:
            ib = False
            break

    messagebox.showinfo("Is Binary?", f"Your input was: {ui}\nYour input is binary: {ib}")

mb = Button(wd, text="Is Binary?", command=isbinary)
mb.place(x=100, y=150) 
