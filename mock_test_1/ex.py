'''
1.python is a high level object-oriented interpreted programming language.
  features of python:
  it is dynamically typed,platform independant.
  advantages:
  can work on different OS since it is platform independant
  applications:
  python is used various applications like developing an app

2.compiled programming language: is the programming language that reads and understands the entire code and then executes the code.
  interpreted programming language: is the programming language that reads and executes the code line by line.
  python is an interpreted programming language because it reads the code line by line and executes the code line by line.

4. variables are the values given to the identifier
rules: a.variables should have alpha-numeric values or can start with '_'
       b.variables should not start with numbers
       c.variables are case sensitive

5. built-in data types are the data types which are pre-defined by python language.
   built-in data types include int,str,float,bool,complex which are immutable and built-in dt like list,tuple,set,dictionary are mutuable data types.

6. list: contains values in a sequential order ex:[1,2,3,4]
   set: contains values in a non sequential order ex:{1,7,4}
   dictionary: stores values in a key:value pair format ex:(number,12)

7. type conversions are defined as conversion of one data type to another data types 
   explicit type conversions are the conversions done forcefully by python

8. int():is used to enter integer values ex: a=12..print(int(a))
   float():is used to enter decimal values ex: a=12.4...print(float(a))
   str():is used for characters
   bool():used to give boolean statements like true or false
   list(): used to enter sequential values ex:l=[1,2,3,4]

9. arithmetic operators:used to perform mathematical calculations like add,sub,multiply,divide etc ex:a=2,b=3,print(a+b) gives o/p as 5
   assignment operators:used to assign values ex:+=,-=,*=,/=
   comparision operators:used to compare b/w two operands ex:>,<,==,>=,<=,!=
   logical operators:used to perform and satisfy given conditions like AND,OR,NOT 
   membership operators:used to check whether the condition is true or not ex: is,is not  o/p= T or F
   identity operators: used to check the memory address is true or no ex:in,not in

11. input() function is used to enter the input
    print() function is used to print the given condition 

12. conditional statements are the statements that work based on the given conditions
    if statement: executes only if the given condition is true
    if else: executes when the if condition is not true it executes the 2nd condition(else)
    if-elif-else: used to check multiple conditions

13. looping statements are the statements that gets executed in loops
    while loop:also called as centinal loop..executes the code until the given condition is true 
    for loop:executes code for each loop written

14.pass:used to pass the condition when written
   continue:used to skip the condition when written
   break: used to stop the condition

15. a)false, b)true, c) <class 'float'> <class 'int', d) true,true
'''
#coding

#1.program to accept two numbers and perform all arithmetic operations
'''number1=int(input('enter a number:'))
number2=int(input('enter a number:'))
print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1/number2)
print(number1//number2)
print(number1**number2)'''

#2.program to check whether a given number is positive, negative, or zero
'''number=int(input('enter a number:'))
if number>0:
    print(number,'is positive')
elif  number<0:
     print(number,'is negative')
else:
     print(number,'is zero')'''

#4.program to find the largest of three numbers without using max()
'''number1=int(input('enter a number:'))
number2=int(input('enter a number:'))
number3=int(input('enter a number:'))
if number1>=number2 and number1>=number3:
   print(largest=number1)
elif number2>=number1 and number2>=number3:
   print(largest=number2)
else:
  
   print('number3 is largest')'''

    
#7.program to generate the following patterns
'''i=1
while i<6:
    j=1
    while j<6:
        if j<=i:
         print('*',end='')
        j+=1
    print( )
    i+=1 '''

#8.program to generate the following patterns

'''i=1
while i<=6:
    j=1
    while j<=6:
        if j<=i:
         print(j,end=' ')
         
        j+=1
    print( )
    i+=1'''