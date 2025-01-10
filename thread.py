import threading
import time

def Hello():
    time.sleep(2)
    print("Hello World")


def Hi():
   time.sleep(5)
   print("Hi Everyone")

def name():
    time.sleep(7)
    print("My Name is Rohan")

t1 = threading.Thread(target=Hello)
t2 = threading.Thread(target=Hi)
t3 = threading.Thread(target=name)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

"""name()
Hello()
Hi()"""

print("Done!")