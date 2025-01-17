import threading
import time

lock=threading.Lock()

def Hello():
    global lock
    lock.acquire()
    print("Function Started!")
    time.sleep(7)
    print("Hello World")
    lock.release()


def Hi():
   global lock
   lock.acquire()
   print("Started")
   time.sleep(5)
   print("Hi Everyone")
   lock.release()

def name():
    global lock
    lock.acquire()
    print("Chalu")
    time.sleep(2)
    print("My Name is Rohan")
    lock.release()

t1 = threading.Thread(target=Hello)
t2 = threading.Thread(target=Hi)
t3 = threading.Thread(target=name)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("done!")