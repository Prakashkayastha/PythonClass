import tkinter as t
a=t.Tk()
a.title("My Window")
a.geometry('500x600')
l1=t.Label(a,text='LoginId')
l1.place(x=10,y=100)
e1=t.Entry(a)
e1.place(x=130,y=100)
l2=t.Label(a,text="Password")
l2.place(x=10,y=140)
e2=t.Entry(a,show="*")
e2.place(x=130,y=140)
a.mainloop()