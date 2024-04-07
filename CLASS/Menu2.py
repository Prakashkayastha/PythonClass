import tkinter as tk
from tkinter import messagebox
a=tk.Tk()
a.title("My work")
a.geometry("500x600")
v1=tk.StringVar()
v2=tk.StringVar()
v3=tk.StringVar()
def add():
    n1=int(v1.get())
    n2=int(v2.get())
    r=n1+n2
    v3.set(str(n1)+"+"+str(n2)+"="+str(r))
def sub():
    n1=int(v1.get())
    n2=int(v2.get())
    r=n1-n2
    v3.set(str(n1)+"-"+str(n2)+"="+str(r))
pnb=tk.Menu(a)
op=tk.Menu(pnb, tearoff=0)
op.add_command(label="Addition", command=add)
op.add_command(label="Substraction", command=sub)
pnb.add_cascade(label="Arithmatic Operation", menu=op)
l1=tk.Label(a, text="Number One")
l2=tk.Label(a, text="Number Two")
l1.place(x=10, y=20)
l2.place(x=10, y=60)
e1=tk.Entry(a, textvariable=v1)
e2=tk.Entry(a, textvariable=v2)
e1.place(x=100,y=20)
e2.place(x=100,y=60)

l3=tk.Label(a,textvariable=v3)
l3.place(x=10,y=100)
a.config(menu=pnb)
a.mainloop()