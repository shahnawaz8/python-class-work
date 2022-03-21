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
        per=(p+c+m)/3
        if per>=60:
            print('Division:','First')
        elif per>=45 and per<60:
            print('Division:','2nd')
        elif per>=33 and per<45:
            print('Division:','3nd')
        print('Total Marks',(p+c+m))
ob=finalstudent()
for x in range(3):
    ob.info()
    ob.getmarks()
    ob.show()
