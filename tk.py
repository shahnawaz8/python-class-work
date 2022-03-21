from tkinter import messagebox as msg
from tkinter import *
class Demo(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.l1=Label(self,text='Username',bg='cyan',fg='red',font=('elephant',14,'italic'),bd=3)
        self.l2=Label(self,text='Password',bg='cyan',fg='red',font=('algerian',14),bd=3)
        self.t1=Entry(self,justify='center',bd=8,insertwidth=4)
        self.t2=Entry(self,justify='center',show='*',bd=8,insertwidth=4) #insertwidth=cursor size
        self.b1=Button(self,text='Login',command=self.show)
        
        self.columnconfigure(0,pad=10)
        self.columnconfigure(1,pad=10)
        self.rowconfigure(0,pad=15)
        self.rowconfigure(1,pad=15)
        self.rowconfigure(2,pad=15)
        
        self.l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)
        self.l2.grid(row=1,column=0)
        self.t2.grid(row=1,column=1)
        self.b1.grid(columnspan=2)

        
        self.pack()

    def show(self):
        uid=self.t1.get()
        pas=self.t2.get()
        msg.showinfo('Your Username & Password is:','Username :-'+uid+'\n'+'Passsword :-'+pas)
        
root=Tk()
ob=Demo(root)
root.geometry('350x250')
root.title('Student')
root.state('zoomed')
root.mainloop()