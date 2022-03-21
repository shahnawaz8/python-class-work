       #INTANCE_VARIABLE
class abc:
    def __init__(self):
        self.name='Makhan lal'
    def show(self):
        print('hello',self.name,'ji')
obj=abc()
obj.show()
print(obj.name) #direct acces by object anywhere

       #CLASS_VARIABLE
class xyz:
    x=10 #class variable
    def __init__(self):
        self.x=10 #intance variable
    def add(self):
        xyz.x+=1  #(class_name.variable_name)
        self.x+=1 #(self.variable_name)
        print('class',xyz.x)
        print('Instance',self.x)
ob1=xyz()
ob2=xyz()
ob3=xyz()
ob1.add()
ob2.add()
ob3.add()

        #PRIVATE VARIABLE

class wcd:
    def __init__(self):
        self.__x=10 #Private variable
        self.public=20
    def maz(self):
        print('private',self.__x)
        print('Instance',self.public)
        
ob=wcd()
ob.maz()




         #globle variable
class student:
    def info(self):
        global name,age
        name=input('Enter Name')
        age=int(input('Enter Age'))
class marks(student):
    def getmarks(self):
        global p,c,m
        p=int(input('Phy'))
        c=int(input('Che'))
        m=int(input('Math'))
class finalstudent(marks):
    def show(self):
        print('Name',name)
        print('Age',age)
        print('Total Marks',(p+c+m))
ob=finalstudent()
ob.info()
ob.getmarks()
ob.show()
