from employ import *
from pymysql import *

from tkinter import *
from tkinter import messagebox as msg
class MyMenu(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.val=StringVar(self)
        choices={'Python','Ds','ML','Java','AI'}
        self.val.set('--select--')
        self.pm=OptionMenu(self,self.val,*choices,command=self.select)
        self.lblx=Label(self,text='Choose a language')
        self.lblx.grid(row=1,column=1)
        self.pm.grid(row=2,column=1)
        self.pack()
        
    def select(self,event):
        nam=self.val.get()
        nam1='MR Mohan'
        msg.showinfo('Information','Thanks for joining '+nam+'\n'+ nam1)
       
        
        
        
        
root=Tk()
My=MyMenu(root)
#root.config(menu=My.menubar)
root.title('MenuBar')
root.geometry('650x500')



root.mainloop()
        
        