#clauser

def inc(x):
    x+=1
    print(x)
def minus(x):
    x-=1
    print(x)
def helper(func,x):
    func(x)
#ob=helper(inc,22)

#Decorator
def Show(func):
    def display():
        print('Hello')
        func()
    return display
@Show
def printer():
    print('hi how are you')
    
#printer()


def star(func):
    def inner(x):
        print('*'*30)
        func(x)
        print('*'*30)
    return inner

def percent(func):
    def inner(x):
        
        print('#'*30)
        func(x)
        print('#'*30)
    return inner

@star
@percent
def hello(msg):
    print(msg)
hello("Hello")





def show(name1,name2):
    name=''
    for x,y in zip(name1,name2):
        name=name+x+y
    if len(name1)>len(name2):
        name=name+name1[len(name2):]
    else:
        name=name+name2[len(name1):]
    print(name)
    
#obj=show('Tnymha','aa isr')





