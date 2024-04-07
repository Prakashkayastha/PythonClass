from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import tkinter as tk
a=tk.Tk()
a.title("My Work")
a.geometry("500x600")
def getinfo():
    fn=askopenfilename()
    ot="select files"+str(fn)
    messagebox.showinfo(ot)
b=tk.Button(a,text="Get Info", command=getinfo)
b.place(x=30,y=50)
a.mainloop()