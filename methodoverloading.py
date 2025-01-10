#from multipledispatch import dispatch
import threading
import time

def hi():
    for a in range(5):
        time.sleep(1)
        print("Hi")

def hello():
    for a in range(5):
        print("Hello")
        time.sleep(1)

#hi()
#hello()

t1=threading.Thread(target=hi)
t2=threading.Thread(target=hello)

t1.start()
t2.start()
