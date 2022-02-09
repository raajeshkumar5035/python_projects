from time import *
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("myhello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("my hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(1)
t2.start()

t1.join()
t2.join()
