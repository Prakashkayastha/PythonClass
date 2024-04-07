#widget = Menubutton(windo,option)
#test = string
#image = any.image
#direction = left,right,center(Default)
#justify = right,left,center


#Child Windo
#windo = tkinter.Toplevel()
#windo.withdraw()-hide the windo
import tkinter as tk
from tkinter import messagebox
a=tk.Tk()
a.geometry("500x600")


b1=tk.Toplevel()
b1.title("First Window")
b1.geometry("500x600")
b1.withdraw()

b2=tk.Toplevel()
b2.title("Second window")
b2.geometry("500x600")
b2.withdraw()

b1=tk.Toplevel()
b1.title("First Window")
b1.geometry("500x600")
b1.withdraw()

def first():
    b2.withdraw()
    b1.iconify()
    b1.configure(bg="red")

def second():
    b1.withdraw()
    b2.iconify()
    b2.configure(bg="green")

mb=tk.Menubutton(a,text="Choose one")
mb.place(x=20,y=30)
m=tk.Menu(mb,tearoff=0)
m.add_command(label="First Window",command=first)
m.add_command(label="Second Window",command=second)
mb['menu']=m
a.mainloop()
