'''class Parent:
    def display(self):
        print("This is a parent class")


class Child(Parent):
    def display(self):
        print("This is a child class")


c = Child()
c.display()'''




#method overloading
  
class Demo:
    def display(self, *args):
        print(args)


d = Demo()
d.display(10)
d.display(10, 20)