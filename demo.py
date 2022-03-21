from employ import *
from pymysql import *
from tkinter import *
from tkinter import messagebox as msg
class MyMenu(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.menubar=Menu(self)
        self.filemenu=Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="New",command=self.call)
        self.filemenu.add_command(label="Close")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save")
        self.filemenu.add_command(label="Save as")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=root.quit,accelerator="Ctrl+x")
        self.filemenu.add_separator()
        
        self.menubar.add_cascade(label="File",underline=0,menu=self.filemenu)
        
        
        self.editmenu=Menu(self.menubar,tearoff=0)
        self.editmenu.add_command(label="Undo")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut")
        self.editmenu.add_command(label="Copy")
        self.editmenu.add_command(label="Paste")
        
        self.menubar.add_cascade(label="Edit",menu=self.editmenu)
        
        self.editmenu=Menu(self.menubar,tearoff=0)
        self.editmenu.add_command(label="Check for Update")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="About us")
        self.menubar.add_cascade(label="Help",menu=self.editmenu)
        
        
        
        frame1=Frame(root,bg='gray')
        
        
        frame1.pack()

    def call(self):
        root=Tk()
        obj=Employee(root)
        root.title('Employee Data')
        root.geometry('355x380')
        root.mainloop()
        
        
        
        
        
        
        
root=Tk()
My=MyMenu(root)
root.config(menu=My.menubar)
root.title('MenuBar')
root.geometry('650x500')



root.mainloop()
        
        