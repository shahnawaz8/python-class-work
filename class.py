class abc:
#constructor
    def __init__(self):
        print('Constructor from class abc')
    def show(self):
        print('From class Abc')
class xyz(abc):
#constructor
    def __init__(self):
        super().__init__()
        print('Constructor from class xyz')
    def xy(self):
        print('From class xyz')
        
class ducat(xyz): #multi-level inheritence
#constructor
    def __init__(self):
        super().__init__()
        print('Constructor from class ducat')
    def duc(self):
        print('From class ducat')

#Multiple Inheritence

class abc:
#constructor
    def __init__(self):
        print('Constructor from class abc')
    def show(self):
        print('From class Abc')
class xyz:
#constructor
    def __init__(self):
        #super().__init__()
        print('Constructor from class xyz')
    def xy(self):
        print('From class xyz')
        
class ducat(abc,xyz): #multiple inheritence
#constructor
    def __init__(self):
        super().__init__()
        print('Constructor from class ducat')
    def duc(self):
        print('From class ducat')
obj=ducat()
obj.show()

     #OVER RIDDING 
class base:
    def clac(self,x,y):
        k=x*y/100
        print('Output',k)
class drived(base):
    def calc(self,x,y):
        i=x*y/100
        k=x+i
        print('Intrest for',j,'%',l,'=',i)
        print('Total',k)
        
ob=drived()
j=int(input('Enter X'))
l=float(input('Enter Y'))
ob.calc(j,l)
