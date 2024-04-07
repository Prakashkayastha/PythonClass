#widget = tk.menu(window,option)
#syntax
#menu.add_command(label="menu_name",command=function)
#menu.add_radiobutton(lable="manu_name",command=function)
#menu.add_checkbutton(label="menu_name",command=function)
#menu.add_separator(label="manu_name",command=function)
#manu.add_cascade(label="manu_name",manu=manu object)

#WAP To design a follwoing window
import tkinter as tk
from tkinter import messagebox
a=tk.Tk()
a.title("My work")
a.geometry("500x600")
def func():
    messagebox.showinfo("Hello")
    
pnb=tk.Menu(a)
fm=tk.Menu(pnb, tearoff=0)
fm.add_command(label="New",command=func)
fm.add_command(label="Open",command=func)
fm.add_separator()
fm.add_command(label="save",command=func)
fm.add_command(label="save As", command=func)
fm.add_separator()
fm.add_command(label="Exit", command=func)
pnb.add_cascade(label="File", menu=fm)

em=tk.Menu(pnb,tearoff=0)
em.add_command(label="Cut", command=func)
em.add_command(label="Past", command=func)
em.add_command(label="Copy", command=func)
em.add_separator()
em.add_command(label="Replace", command=func)
pnb.add_cascade(label="Edit", menu=em)


hm=tk.Menu(pnb, tearoff=0)
hm.add_command(label="About", command=func)
hm.add_command(label="Contact", command=func)
pnb.add_cascade(label="Help", menu=hm)

a.config(menu=pnb)
a.mainloop()


