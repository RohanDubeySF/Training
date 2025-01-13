# Create an abstract base class Account with abstract methods deposit() and withdraw(). Then, create two derived classes, SavingsAccount and CheckingAccount, that implement the deposit() and withdraw() methods. The SavingsAccount should have an additional method add_interest() that adds interest to the balance. The CheckingAccount should have an additional method deduct_fees() that deducts a fixed fee from the balance. Finally, create instances of SavingsAccount and CheckingAccount, perform some transactions, and demonstrate the functionality.

from abc import ABC, abstractmethod

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
        self.balance+=amount
        print("Amount Added Successfully!")
        print(f"Total balance :  {self.balance}")
    
    def withdraw(self,amount):
        if self.balance<amount:
            print("Insufficient Balance")
        else :
            self.balance-=amount
            print("Amount Withdrawn Successfully!")
            print(f"Total balance :  {self.balance}")

    def interest(self,rate):
        self.balance*= rate


savings = Savings(1000)
savings.deposit(200)
savings.withdraw(150)
savings.interest(0.05)