import multiprocessing
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

p1 = multiprocessing.Process(target=Hello)
p2 = multiprocessing.Process(target=Hi)
p3 = multiprocessing.Process(target=name)

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

print("Done!")