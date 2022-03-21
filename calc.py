from tkinter import *
from tkinter import messagebox as msg
class Employee(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        
        
        self.txt=Entry(self,justify='left',bd=4,font=('lucida 20 bold'))
        self.txt.grid(row=1,columnspan=6)
        
        
        self.bclr=Button(self,text='C',bd=4,font=('lucida 20 bold'))
        self.bbrct=Button(self,text='( )',bd=4,font=('lucida 20 bold'))
        self.bprcntg=Button(self,text='%',bd=4,font=('lucida 20 bold'))
        self.bdiv=Button(self,text='/',bd=4,font=('lucida 20 bold'))
        
        
        self.bclr.grid(row=2,column=1)
        self.bbrct.grid(row=2,column=2)
        self.bprcntg.grid(row=2,column=3)
        self.bdiv.grid(row=2,column=4,)
        
        
        self.b7=Button(self,text='7',bd=4,font=('lucida 20 bold'))
        self.b8=Button(self,text='8',bd=4,font=('lucida 20 bold'))
        self.b9=Button(self,text='9',bd=4,font=('lucida 20 bold'))
        self.bmul=Button(self,text='*',bd=4,font=('lucida 20 bold'))
        self.b7.grid(row=3,column=1)
        self.b8.grid(row=3,column=2)
        self.b9.grid(row=3,column=3)
        self.bmul.grid(row=3,column=4)
        
        
        self.b4=Button(self,text='4',bd=4,font=('lucida 20 bold'))
        self.b5=Button(self,text='5',bd=4,font=('lucida 20 bold'))
        self.b6=Button(self,text='6',bd=4,font=('lucida 20 bold'))
        self.bsub=Button(self,text='-',bd=4,font=('lucida 20 bold'))
        self.b4.grid(row=4,column=1)
        self.b5.grid(row=4,column=2)
        self.b6.grid(row=4,column=3)
        self.bsub.grid(row=4,column=4)
        
        self.b1=Button(self,text='1',bd=4,font=('lucida 20 bold'))
        self.b2=Button(self,text='2',bd=4,font=('lucida 20 bold'))
        self.b3=Button(self,text='3',bd=4,font=('lucida 20 bold'))
        self.bpls=Button(self,text='+',bd=4,font=('lucida 20 bold'))
        self.b1.grid(row=5,column=1)
        self.b2.grid(row=5,column=2)
        self.b3.grid(row=5,column=3)
        self.bpls.grid(row=5,column=4)
        
        self.bplsm=Button(self,text='+/-',bd=4,font=('lucida 18 bold'))
        self.b0=Button(self,text='0',bd=4,font=('lucida 20 bold'))
        self.bdot=Button(self,text='.',bd=4,font=('lucida 20 bold'))
        self.beql=Button(self,text='=',bg='lightblue',bd=4,font=('lucida 20 bold'))
        self.bplsm.grid(row=6,column=1)
        self.b0.grid(row=6,column=2)
        self.bdot.grid(row=6,column=3)
        self.beql.grid(row=6,column=4)
        
        
        
        
        self.rowconfigure(1,pad=10)
        self.rowconfigure(2,pad=10)
        self.columnconfigure(0,pad=2)
        self.columnconfigure(1,pad=2)

        
        self.pack()

root=Tk()
obj=Employee(root)
root.title('My Calc')
root.geometry('310x390')
root.maxsize(310,390)
root.mainloop()