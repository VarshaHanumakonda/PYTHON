#syntax for creating a function
'''def function_name(parameters):  #parameter is the variable passed to the function
    block of code'''
#for calling a function
'''function_name(arguments)'''    #argument is the actual value passed when calling the function

#creating a simple function
def wish():  
    print ('good morning')
wish()  #calling the function 

#function with return statement
def wish():
    return 'hello good morning'
wish() #calling the function but it will not print anything because it is returning a value
print(wish()) #to print the returned value we need to use print statement

#creating a function with parameters
def wish(name):
    print('good morning',name)
wish('varsha')  #calling the function with an argument 

#check the given no is prime or not
def check_prime(a):
      count=0
      i=1
      while i<=a:
        if a%i==0:
            count+=1
        i+=1
      if count==2:
           return f'{a} is a prime number'
      else:
            return f'{a} is a composite number'
print(check_prime(7))
print(check_prime(4))    

#function with multiple return statements
def math(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    return add,sub,mul
print(math(10,2))