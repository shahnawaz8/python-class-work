import threading
import time
def print_cube(num):
    for x in range(num):
        print('cube',x*x*x)
        time.sleep(1)
def print_square(num):
    for x in range(3):
        print("Square:{}".format(num*num))
        time.sleep(2)
if __name__=="__main__":
    #creating thread
    t1=threading.Thread(target=print_square,args=(7,))
    t2=threading.Thread(target=print_cube,args=(5,))
    
    #starting thread 1
    t1.start()
    #starting thread2
    t2.start()
    #wait untill thread 1 is completely execute
    t1.join()
    print('Thread 1 is completed')
    #wait untill thread 2 is completely execute
    t2.join()
    print('Thread 2 is completed')
    
    print('Done!')