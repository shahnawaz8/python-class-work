from employ import *
from pymysql import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as msg
class MyMenu(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.menubar=Menu(self)
        
#------------------------##-----------------------------#
        self.filemenu=Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="New",command=self.new_file)
        self.filemenu.add_command(label="Open",command=self.open_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save",command=self.save_file)
        self.filemenu.add_command(label="Save as",command=self.save_as)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=root.quit,accelerator="Ctrl+x")
        self.filemenu.add_separator()
#------------------------##-----------------------------#
        
        self.menubar.add_cascade(label="File",underline=0,menu=self.filemenu)
        self.editmenu=Menu(self.menubar,tearoff=0)
        self.editmenu.add_command(label="Undo")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut")
        self.editmenu.add_command(label="Copy")
        self.editmenu.add_command(label="Paste")
        self.menubar.add_cascade(label="Edit",menu=self.editmenu)
#------------------------##-----------------------------#       
        self.find=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="Find")
        
#------------------------##-----------------------------#       
        self.view=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="View")
        
#------------------------##-----------------------------#
        self.help=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="Help")
    def new_file(self):
        text.delete(0.0,END)
        
    def open_file(self):
        file1=filedialog.askopenfile(mode='r')
        data=file1.read()
        text.delete(0.0,END)
        text.insert(0.0,data)
    def save_file(self):
        filename="Untitled.txt"
        data=text.get(0.0,END)
        file1=open(filename,'w')
        file1.write(data)
    def save_as(self):
        
        file1=filedialog.asksaveasfile(mode='w')
    def call(self):
        root=Tk()
        obj=Employee(root)
        root.title('Employee Data')
        root.geometry('355x380')
        root.mainloop()
        
        
        
        
        
        
root=Tk()
My=MyMenu(root)
root.config(menu=My.menubar)
root.title('Typing Guru')

text=Text(root)
text.pack()

root.geometry('650x400')
root.mainloop()
        
        