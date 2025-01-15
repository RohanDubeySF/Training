#Banking 

import threading
from abc import ABC, abstractmethod
global lock
lock = threading.Lock()

class Account(ABC):
    def __init__(self,balance=0):
        self.balance=balance

    @abstractmethod
    def deposit():
        pass

    @abstractmethod
    def withdraw():
        pass

class Savings(Account):
    def deposit(self,amount):
        
        lock.acquire()
        self.balance+=amount
        print("Amount Added Successfully!")
        print(f"Total balance :  {self.balance}")
        lock.release()
    
    def withdraw(self,amount):
        lock.acquire()
        if self.balance<amount:
            print("Insufficient Balance")
        else :
            self.balance-=amount
            print("Amount Withdrawn Successfully!")
            print(f"Total balance :  {self.balance}")
        lock.release()



savings = Savings(1000)



t1=threading.Thread(target=savings.deposit,args=[200])
t2=threading.Thread(target=savings.withdraw,args=(150,))
t=threading.Thread(target=savings.deposit,args=[200])
t3=threading.Thread(target=savings.withdraw,args=(150,))
t4=threading.Thread(target=savings.withdraw,args=(150,))

t1.start()
t2.start()
t.start()
t3.start()
t4.start()


t.join()
t1.join()
t2.join()   
t3.join()
t4.join()


print("done")