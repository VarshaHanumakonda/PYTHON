'''class Student:
    def __init__(self):    #__init__ is a constructor which is used to give initial values to the object of the class
        self.name = "Varsha"
        self.age = 20

s = Student()    #calling the function means creating an object of the class  (i.e class Student)
print(s.name)



class student:
    def __init__(self):
        self.name='varsha'
        self.age=21
    def details(self):
        print(f'students name is {self.name} and age is {self.age}')
s=student()
s.details()        


#one class can have many objects and each object can have different values for the variable (inside constructor) .
class Student:

    def __init__(self, name):
        self.name = name
s1 = Student("Varsha")
print(s1.name)
s2 = Student("Mallika")
print(s2.name)
'''

'''students=[]
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def load_details(self):
        d={}
        d.update({'name':self.name,'age':self.age})
        students.append(d)
s1=student('Varsha',21)
s1.load_details()
s2=student('Mallika',21)
s2.load_details()
print(students)            '''

#class variable
class employee:
    company='google'          #class variable
    def __init__(self,name):
        self.name=name       #instance variable
e1=employee('Varsha')
e2=employee('Mallika')
print(e1.company)
print(e2.company)

#class method
class car:
    company='toyota'
    @classmethod
    def show_company(cls):
        print(cls.company)
car.show_company()  
      