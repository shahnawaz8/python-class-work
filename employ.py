from pymysql import *
from tkinter import *
from tkinter import messagebox as msg
class Employee(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        #label
        self.lblWelcome=Label(self,text='Welcome to Python.org',font=('lucida 20 bold'),bg='cyan')
        self.lblWelcome.grid(row=0,column=0,columnspan=3)
        
        self.lblEno=Label(self,text='Employee Num.',bg='lightblue')
        self.lblName=Label(self,text='Employee Name',bg='lightblue')
        self.lblSalary=Label(self,text='Employee Salary.',bg='lightblue')
        self.lblDes=Label(self,text='Employee desg',bg='lightblue')
        #textBox
        self.txtEno=Entry(self)
        self.txtName=Entry(self)
        self.txtSalary=Entry(self)
        self.txtDes=Entry(self)
        
        #Button
        self.btnSave=Button(self,text='Save',command=self.save)
        self.btnSearch=Button(self,text='Search',command=self.search)
        self.btnDelete=Button(self,text='Delete')
        self.btnUpdate=Button(self,text='Update')
        self.btnExit=Button(self,text='Exit',command=self.quit)
        self.btnShow=Button(self,text='Show All')
        
        
        self.rowconfigure(0,pad=7)
        self.rowconfigure(1,pad=7)
        
        self.rowconfigure(2,pad=7)
        self.rowconfigure(3,pad=7)
    
        self.rowconfigure(4,pad=7)
        self.rowconfigure(5,pad=7)
        
        self.columnconfigure(0,pad=7)
        self.columnconfigure(2,pad=7)
        self.columnconfigure(3,pad=7)
        
        
        self.lblEno.grid(row=1,column=0)
        self.lblName.grid(row=2,column=0)
        self.lblSalary.grid(row=3,column=0)
        self.lblDes.grid(row=4,column=0)
        
        self.txtEno.grid(row=1,column=1)
        self.txtName.grid(row=2,column=1)
        self.txtSalary.grid(row=3,column=1)
        self.txtDes.grid(row=4,column=1)

        
        self.btnSave.grid(row=5,column=0)
        self.btnDelete.grid(row=5,column=1)
        self.btnSearch.grid(row=5,column=2)
        self.btnUpdate.grid(row=6,column=0)
        self.btnExit.grid(row=6,column=1)
        self.btnShow.grid(row=6,column=2)
        
        self.pack()
        
    def clear(self):
        self.txtEno.delete(0,'end')
        self.txtName.delete(0,'end')
        self.txtSalary.delete(0,'end')
        self.txtDes.delete(0,'end')
    def connect(self):
        self.con=connect(db='employ',user='root',passwd='',host='localhost')
        self.cur=self.con.cursor()
    def save(self):
        self.connect()
        empno=(int)(self.txtEno.get())
        ename=self.txtName.get()
        esalary=(int)(self.txtSalary.get())
        edes=(int)(self.txtDes.get())
        
        i=self.cur.execute("insert into emp values(%d,'%s',%f,'%s')"%(empno,ename,esalary,edes))
        if i>=1:
            self.con.commit()
            msg.showinfo('Confirmation','Record Saved')
            self.clear()
            self.txtEno.focus()
            self.con.close()
            
    def search(self):
        self.connect()
        empno=(int)(self.txtEno.get())
        self.cur.execute("select * from emp where E_no=%d"%(empno))
        rs=self.cur.fetchall()
        if len(rs)>0:
            self.txtName.insert(0,rs[0])
            self.txtSalary.insert(0,rs[0])
            self.txtDes.insert(0,rs[0])
        else:
            msg.showerror('Error','Record Not found')
        
    

        
        