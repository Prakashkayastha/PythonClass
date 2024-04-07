#WAP to generate a color code
from tkinter.colorchooser import askcolor
from tkinter import messagebox
import tkinter as tk
a=tk.Tk()
a.title("My Work")
a.geometry("500x600")
def getinfo():
    cd=askcolor()
    ot="Selected Color is:"+str(cd)
    messagebox.showinfo(ot)
b=tk.Button(a,text="Get Color",command=getinfo)
b.place(x=30,y=50)
a.mainloop()

