from tkinter import *
master=Tk()
cwidth=400
cheight=400
w=Canvas(master,width=cwidth,height=cheight)
w.pack()
#w.create_line(0,40,400,40,fill='blue')
#img=PhotoImage(file='new-icon.gif')
#w.create_image(0,0,anchor=NW,image=img)

img1=PhotoImage(file='searcg2.gif')
blabel=Label(master,image=img1)
blabel.place(x=0,y=0,relwidth=1,relheight=1)
mainloop()