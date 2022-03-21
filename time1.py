import time
from turtle import *

sec=57
mint=59
hr=12

setup()
t1=Turtle()
"""time1=time.time()
print(time1)

local=time.localtime(time.time())
print(local)"""


while True:
    t1.clear()
    t1.write(str(hr).zfill(2)+":"+str(mint).zfill(2)+":"+str(sec).zfill(2),font=('lucida 20 bold'))
    time.sleep(1)
    sec=sec+1
    if sec==60:
        sec=0
        mint=mint+1
    if mint==60:
        mint=0
        hr=hr+1
    if hr==13:
        hr=1
        
        