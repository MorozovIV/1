from threading import *
from time import time, sleep

def one(num):
    sleep(num)

def two(num):
    sleep(num)

t1 = Thread(target=one, args = (1,))
t2 = Thread(target=two, args = (1,))


x1 = time()

t1.start()
t2.start()

t1.join()
t2.join()


x2 = time()

input(x2-x1)