from concurrent.futures import ThreadPoolExecutor 
import time


def Hello():
    print("Function Started!")
    time.sleep(2)
    return ("Hello World")


def Hi():
   print("Started")
   time.sleep(5)
   return ("Hi Everyone")

def name():
    print("Chalu")
    time.sleep(7)
    return ("My Name is Rohan")

def sq(numbers):
   for val in numbers:
      ret = val*val
      time.sleep(2)
      print("Number:{} Square:{}".format(val, ret))

def cu(numbers):
   for val in numbers:
      ret = val*val*val
      time.sleep(2)
      print("Number:{} Cube:{}".format(val, ret))

def demo2():
    with ThreadPoolExecutor() as exc: 
        l2=[sq,cu]
        numbers = [1,2,3]      
        results=[]
        for b in l2:
            res1=exc.submit(b,numbers)
            results.append(res1)
            #results.append(list(exc.map(b,numbers)))
        for result in results:
            result.result()

def demo1():
    with ThreadPoolExecutor() as exc:
        l=[Hello,Hi,name]
        results=[]
        for a in l: 
            res1=exc.submit(a)
            results.append(res1)
        for result in results:
            print(result.result())

demo1()

