import tkinter as t
a=t.Tk()
a.title("My Calculator")
a.geometry('500x600')
r=t.StringVar()
n=t.StringVar()
def fact():
    d=n.get()
    d=int(d)
    f=1
    for i in range(1,(d+1)):
        f=f*i
    r.set("Fctorila of "+str(d)+" is :"+ str(f))
l1=t.Label(a,text="Fctorial of number")
l1.place(x=220,y=50)
l2=t.Label(a,text="Num")
l2.place(x=20,y=100)
e1=t.Entry(a)
e1.place(x=130,y=100)
l3=t.Label(a,text="Result",textvariable=r)
l3.place(x=20,y=140)
b1=t.Button(a,text="Find Factorial",command=fact)
b1.place(x=20,y=180)
a.mainloop()