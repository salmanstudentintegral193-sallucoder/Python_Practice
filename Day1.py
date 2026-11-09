# Abstraction learning.
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# obj = Dog()
# obj.sound()
# c = Cat()
# c.sound()                    
from abc import ABC, abstractmethod
class ATM(ABC):
    @abstractmethod
    def check_balance(self):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass
class MyATM(ATM):
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
obj = MyATM()
obj.deposit(100)
obj.check_balance()
obj.withdraw(50)
obj.check_balance()       