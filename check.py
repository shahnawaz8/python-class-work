from tkinter import messagebox as msg
from tkinter import *
class Demo(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.l1=Label(self,text='CURRICULUM VITAE',fg='black',font=('Trebuchet MS',14,'bold'))
        self.l2=Label(self,text='CAREER OBJECTIVE',bg='lightgray',bd=2,font=('Times New Romon',14))
        self.l3=Label(self,text='To work in chellenging position for an organization tha provides the best opportunities to utilize my telent and leadership skills for professional and personal development Motivated achiver who is recongnized for combining program excellence,integrity and innovatin with best practice and disiplined attention to achiving immediate and long term goals and objectives.',bg='lightgray',bd=2,font=('Times New Romon',14))
        
        
        
        
        
        
        #self.t1=Entry(self,justify='center',bd=8,insertwidth=4)
        #self.t2=Entry(self,justify='center',show='*',bd=8,insertwidth=4) #insertwidth=cursor size
        #self.b1=Button(self,text='Login',command=self.show)
         
    
        
        self.l1.grid(row=0,column=1)
        #self.t1.grid(row=1,column=1)
        self.l2.grid(row=2,column=0)
        self.l3.grid(row=3,column=0)
        
        #$self.t2.grid(row=2,column=1)
        #self.b1.grid(columnspan=2)

        
        self.pack()

    def show(self):
        uid=self.t1.get()
        pas=self.t2.get()
        msg.showinfo('Your Username & Password is:','Username :-'+uid+'\n'+'Passsword :-'+pas) #for information
        
        msg.showerror('Title','Information') #for error
        
root=Tk()
ob=Demo(root)
root.geometry('350x250')
root.title('Student')
root.state('zoomed')
root.mainloop()