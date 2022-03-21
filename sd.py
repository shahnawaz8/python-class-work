from tkinter import *
from pymysql import *
from tkinter import messagebox as msg
class Login(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.ui
    def ui(self):
        self.lblName=Lable(self,text='Name')
        self.lblUserid=Lable(self,text='User name')
        self.lblPassword=Lable(self,text='Password')
        
        self.txt.Name=Entry(self)
        self.txt.Userid=Entry(self)
        self.txt.Password=Entry(self,show='*')
        
        self.btnSave=Button(self,text='Save',command=self.save)
        
        self.rowconfigure(0,pad=10)
        self.rowconfigure(1,pad=10)
        self.rowconfigure(2,pad=10)
        self.rowconfigure(3,pad=10)
        
        self.columnconfigure(0,pad=10)
        self.columnconfigure(1,pad=10)
        self.columnconfigure(2,pad=10)
        self.columnconfigure(3,pad=10)
        
        
        self.lblName.grid(row=0,column=0)
        self.txtName.grid(row=0,column=1)
        
        self.lblUserid.grid(row=1,column=0)
        self.txtUserid.grid(row=1,column=1)
        
        self.lblPassword.grid(row=2,column=0)
        self.lblPassword.grid(row=2,column=1)
        
        self.btnSave.grid(columnspan=2)
        self.pack()
    def save(self):
        con=connect(db='Facebook',user='root',passwd='root',host='localhost')
        cur=con.cursor()
        name=self.txtName.get()
        name=self.txtUserid.get()
        name=self.txtPassword.get()
        
        i=cur.execute("insert into login values('%s','%s','%s')"%(name,uname,password)) #same as database
        
        if i>=1:
            con.commit()
            msg.showinfo('Information','Record Saved')
            con.close()
            self.txtName.delete(0,'end')
            self.txtPassword.delete(0,'end')
            self.txtUserid.delete(0,'end')
            self.txtName.focus()
        
root=Tk()
ob=Login(root)
root.title('Login Form')
root.geometry('250x150')
root.mainloop()
        