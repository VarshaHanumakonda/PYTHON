'''class parent:
    def __init__(self):
        self.name='Babu rao'
        self.age=60
    def job(self):
        print('business man')
class child(parent):
    def __init__(self):
        super().__init__()
        self.daughter_name='Varsha'
    def study(self):
        print(self.daughter_name,'is studying ')
c=child()
print(c.name)
print(c.age)
c.job()
c.study()           '''             


'''class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)
c=Child('varsha',21)
print(c.name)
print(c.age)'''

'''#multiple inheritance

class Father:
    def display(self):
        print("This is father's method")

class Mother:
    def show(self):
        print("This is mother's method")

class Child(Father, Mother):
    def project(self):
        print("This is child's method")

c = Child()

c.display()   
c.show()      
c.project() 

#multilevel inheritance

class Grandparent:
    def display(self):
        print("This is grandparent class")

class Parent(Grandparent):
    def show(self):
        print("This is parent class")

class Child(Parent):
    def project(self):
        print("This is child class")
c = Child()

c.display()
c.show()
c.project()    

#hierarchical inheritance

class Father:
    def car(self):
        print("This is father's car")

class Child1(Father):
    def party(self):
        print("Child 1 is going to party")

class Child2(Father):
    def outing(self):
        print("Child 2 is going for outing")
c1 = Child1()
c2 = Child2()
c1.car()
c1.party()
c2.car()
c2.outing()    '''  


#hybrid inheritance

class A:
    def display1(self):
        print("This is class A")

class B(A):
    def display2(self):
        print("This is class B")

class C(A):
    def display3(self):
        print("This is class C")

class D(B, C):
    def display4(self):
        print("This is class D")
a=A()
b=B()
c=C()
d=D()
a.display1()
b.display2()
c.display3()
d.display4()
print(D.__mro__)
