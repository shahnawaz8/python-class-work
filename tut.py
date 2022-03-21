from tkinter import *
root=Tk()
root.geometry('333x343')
l1=Label(root,text='Welcome to Login Page',bg='lightgray',fg='red',font=('elephant',20,'bold')).grid(columnspan=6)

Label(root,text='Name',fg='blue').grid(row=1,column=2)
Label(root,text='Mobile',fg='blue').grid(row=2,column=2)
Label(root,text='Email',fg='blue').grid(row=3,column=2)
Label(root,text='Address',fg='blue').grid(row=4,column=2)
Button(root,text='Submit').grid(row=5,column=3)

Entry(root,bd=3).grid(row=1,column=3)
Entry(root,bd=3).grid(row=2,column=3)
Entry(root,bd=3).grid(row=3,column=3)
Entry(root,bd=3).grid(row=4,column=3)


root.title('Login')
root.state('zoomed')
root.mainloop()
