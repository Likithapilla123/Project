from tkinter import*
def feessubmit():
    tf=150000
    s1=int(e1.get())
    s2=int(e2.get())
    s3=int(e3.get())
    s4=int(e4.get())
    s5=int(e5.get())
    s6=int(e6.get())
    of=s1+s2+s3+s4+s5+s6
    rf=tf-of
    res='paid fees:'+str(of)+'\n pending fees:'+str(rf)
    l7.config(text=res)
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    l7.config(text=' ')
sem=Tk()
sem.title('Aditya Degree College')
sem.geometry('700x400')
l1=Label(sem,text='semester 1 fees:',font=('Times New Roman',20))
l2=Label(sem,text='semester 2 fees:',font=('Times New Roman',20))
l3=Label(sem,text='semester 3 fees:',font=('Times New Roman',20))
l4=Label(sem,text='semester 4 fees:',font=('Times New Roman',20))
l5=Label(sem,text='semester 5 fees:',font=('Times New Roman',20))
l6=Label(sem,text='semester 6 fees:',font=('Times New Roman',20))
l7=Label(sem,text='Total paid fees:',font=('Times New Roman',20))
e1=Entry(sem)
e2=Entry(sem)
e3=Entry(sem)
e4=Entry(sem)
e5=Entry(sem)
e6=Entry(sem)
b1=Button(sem,text='Submit',font=('Times New Roman',20),command=feessubmit)
b2=Button(sem,text='clear',font=('Times New Roman',20),command=clear)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
l3.grid(row=2,column=0)
e3.grid(row=2,column=1)
l4.grid(row=3,column=0)
e4.grid(row=3,column=1)
l5.grid(row=4,column=0)
e5.grid(row=4,column=1)
l6.grid(row=5,column=0)
e6.grid(row=5,column=1)
b1.grid(row=6,column=0)
b2.grid(row=6,column=1)
l7.grid(row=1,column=2)
mainloop()