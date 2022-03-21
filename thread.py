#create thread
#intanciation

from threading import *
from datetime import *
import time
class Abc(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.dt=datetime.now()
        self.hh=self.dt.hour
        self.mm=self.dt.minute
        self.ss=self.dt.second
    def run(self):
        while True:
            for h in range(self.hh,24):
                for m in range(self.mm,61):
                    for s in range(self.ss,61):
                        ntime=str(h)+":"+str(m)+":"+str(s)
                        print(ntime)
                        time.sleep(1)
                    self.ss=1
                self.mm=1
            self.hh=1
ob=Abc()
ob.start()





