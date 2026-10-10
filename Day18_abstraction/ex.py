from abc import ABC, abstractmethod                        #a
class Parent(ABC):                     #creating abstract class
    def display(self):
        print('this is concrete method')        #concrete method          (concrete class is a class that has a concrete method)
    @abstractmethod
    def show(self):
        pass                                    #abstract method         (abstract class is a class that has an abstract method and concrete method)
class child(Parent):
    def show(self):
        print('this is abstract method completed in child class')    #completing abstract method in child class
c=child()
c.display()
c.show()     



#banking process example

class bankingprocess(ABC):
    def __init__(self):
        self.name='python bank'
        self.IFSC='PYTH0001'
        print('''** welcome to python bank **''')
    def withdraw(self):
        pass
    def deposit(self):
        pass
    def check_bal(self): 
        pass
class customer(bankingprocess):
    def __init__(self):
        self.cname=input('enter your name:')
        self.cusername=input('enter your username:')
        self.password=input('enter your password:')
        confirm_password=input('confirm your password:')
        if self.password==confirm_password:
            self.balance=int(input('enter your balance:'))
        else:
            print('password did not match')
    def withdraw(self,wamount):
        if wamount>0:
            if wamount<self.balance:
                self.balance-=wamount
                print('withdraw successful')
        else:
            print('please enter amount greater than 0')
    def deposit(self,damount):
        if damount>0 :
            self.balance+=damount
            print('deposit successful')
    def check_bal(self):
        print(f'your balance is {self.balance}')
c1=customer()
c1.withdraw(40000)
c1.check_bal()
c1.deposit(25000)
c1.check_bal()                                            