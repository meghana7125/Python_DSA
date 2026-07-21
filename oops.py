#access modifiers
'''class A:
    def __init__(self,name,age,gender):
        constructor
           self.name=name
           self.age=age
           self.gender=gender
a1=A("sriram",21,"male")
a2=A("divya",21,"female")
print(a1.__name)
print(a2._age)
print(a3.gender)'''
from abc import ABC,abstractmethod
class BankAccount:
    def __init__(Self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balnce-=amount
    def getBalance(self):
        return self.__balance
    @abstractmethod
    def interestcalc(self):
        pass
class SavingAccount(BankAccount):

#POLYMORPHISM
class Animal:
    print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("woof")
class 
