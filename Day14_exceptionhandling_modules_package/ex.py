#method1
'''try:
    a=int(input('enter a variable value:'))
    b=int(input('enter b variable value:'))
    c=a/b
    print(c)
except ZeroDivisionError:
    print('you cannot divide a value with zero')
except ValueError:
    print('instead of int you are entering characters')     '''  



#method2 (genric error exception statement)
'''try:
    a=int(input('enter a variable value:'))
    b=int(input('enter b variable value:'))
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print(e)
except ValueError as v:
    print(v)    
'''
#method3(single exception statement)
'''try:
    a=int(input('enter a variable value:'))
    b=int(input('enter b variable value:'))
    c=a/b
    print(c)
except (ZeroDivisionError,ValueError) as e:
    print(e) '''  


try:
    a=int(input('enter a variable value:'))
    b=int(input('enter b variable value:'))
    c=a/b
    print(c)
except Exception as e:
    print(e) 
