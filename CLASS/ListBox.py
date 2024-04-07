#It is a collection of items
#widget = tkinter.Listbox(window,open)
#selectmode=BROWSE,SINGLE,MULTIPLE,EXTENDED
#Browse is a combination of single and multiple
#Listbox.insert(position,items) item may be a number or string
#Listbox.sectorselection()returns->tuple
#item=Listbox.get(position)


#WAP to choose favourite programming subject of a student
import tkinter as tk
from tkinter import messagebox
a=tk.Tk()
a.title("My Work")
a.geometry("500x600")
s=tk.Label(a,text="subject")
s.place(x=20,y=20)
l=tk.Listbox(a,selectmode="EXTENDED")
l.insert(0,'C')
l.insert(1,'C++')
l.insert(2,'JAVA')
l.insert(3,'PYTHON')
l.insert(4,"DBMS")
l.place(x=120,y=30)
def show():
    s1=l.curselection()
    ot="my fav subject is"+str(l.get(s1[0]))
    messagebox.showinfo("status",ot)
b=tk.Button(a,text='my fav',command=show)
b.place(x=20,y=200)
a.mainloop()