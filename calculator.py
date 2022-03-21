from tkinter import *
from tkinter import messagebox as msg



class main(Frame):
    def __init__(self,master):
        super().__init__(master)
        f4=Frame(root,bg='grey')
        self.lblName=Label(root,text='Casio 991x',font='lucida 20 italic',fg='white',bg='black')
        self.lblName.pack(fill=X)
        self.screen=Entry(root,font='lucida 20 bold',fg='red')
        self.screen.pack(fill=X)
        f4.pack()
        self.btn
    def btn(self):
        f1=Frame(root,bg='grey')
        self.btn9=Button(f1,text='9',font='lucida 20 bold',bd=9,bg='orange',command=self.Nine)
        self.btn9.pack(side='left',ipadx=12)
        
        btn8=Button(f1,text='8',font='lucida 20 bold',bd=9,bg='orange',command=self.Eight)
        btn8.pack(side='left',ipadx=12)
        
        btn7=Button(f1,text='7',font='lucida 20 bold',bd=9,bg='orange',command=self.Seven)
        btn7.pack(side='left',ipadx=12)
        
        f1.pack()
        
        f1=Frame(root,bg='grey')
        btn6=Button(f1,text='6',font='lucida 20 bold',bd=9,command=self.Six)
        btn6.pack(side='left',ipadx=12)
        
        btn5=Button(f1,text='5',font='lucida 20 bold',bd=9,command=self.Five)
        btn5.pack(side='left',ipadx=12)
        
        btn4=Button(f1,text='4',font='lucida 20 bold',bd=9,command=self.Four)
        btn4.pack(side='left',ipadx=12)
        
        f1.pack()
        
        f1=Frame(root,bg='grey')
        btn3=Button(f1,text='3',font='lucida 20 bold',bd=9,bg='green',command=self.Three)
        btn3.pack(side='left',ipadx=12)
        
        btn2=Button(f1,text='2',font='lucida 20 bold',bd=9,bg='green',command=self.Two)
        btn2.pack(side='left',ipadx=12)
        
        btn1=Button(f1,text='1',font='lucida 20 bold',bd=9,bg='green',command=self.One)
        btn1.pack(side='left',ipadx=12)
        
        f1.pack()
        
        f1=Frame(root,bg='grey')
        btnPls=Button(f1,text='+',font='lucida 20 bold',bd=9,bg='red',command=self.pr)
        btnPls.pack(side='left',ipadx=12)
        
        btn0=Button(f1,text='0',font='lucida 20 bold',bd=11,bg='red',command=self.Zero)
        btn0.pack(side='left',ipadx=12)
        
        btnEql=Button(f1,text='=',font='lucida 20 bold',bd=11,bg='red',command=self.Equal)
        btnEql.pack(side='left',ipadx=7)
        
        f1.pack()
        
    def Nine(self):
        value=self.screen.insert(50,[9])
    
    def Eight(self):
        value=self.screen.insert(50,[8])
    def Seven(self):
        value=self.screen.insert(50,[7])
        
    def Six(self):
        value=self.screen.insert(50,[6])
    
    def Five(self):
        value=self.screen.insert(50,[5])
    def Four(self):
        value=self.screen.insert(50,[4]) 
        
    def Three(self):
        value=self.screen.insert(50,[3])
    
    def Two(self):
        value=self.screen.insert(50,[2])
    def One(self):
        value=self.screen.insert(50,[1])
    def Zero(self):
        value=self.screen.insert(50,[0])
    def Plus(self):
        value=self.screen.insert(50,['+'])
    def Equal(self):
        value=self.screen.insert(50,['='])
        
    
        
    def pr(self):
        MainValue=self.screen.get()
        for x in MainValue:
            if x.isdigit():
                print('nothing')
            elif x=='=':
                print('Nine')
            
    
root=Tk()
root.title('Calculator')
obj=main(root)
root.geometry('240x355')
root.maxsize(240,355)
root.minsize(240,355)
obj.btn()
root.mainloop()