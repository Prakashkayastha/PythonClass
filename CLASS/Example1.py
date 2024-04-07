from tkinter.simpledialog import askinteger,askfloat,askstring
from tkinter import messagebox
import tkinter as tk
a=tk.Tk()
a.title("My Work")
a.geometry("500x600")
def MyInfo():
    nm=askstring("MyInfo", "What is your Name:")
    age=askinteger("MyInfo", "What is your Age:")
    wt=askfloat("MyInfo", "What is your Weight")
    ot="I am"+nm+"with age"+str(age)+"and weight is"+ str(wt)
    messagebox.showinfo(ot)
b=tk.Button(a,text="Get Info", command=MyInfo)
b.place(x=30, y=50)
a.mainloop()