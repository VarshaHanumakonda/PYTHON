#conditional statements

#if statement(executes only if the condition is true)
'''age=int(input('enter the age:'))
if age>=18:
    print('eligible to vote')'''

#if else statement(when if condition is not true else condition is executed)
'''number=10
if number%2==0:
    print('even')
else:
    print('odd')'''

#if-elif-else statement(checks for multiple conditions)
'''marks=int(input('enter the marks:'))
if marks>=90 and marks<=100:
    print('grade A+')
elif marks>=80 and marks<90:
    print('grade A')    
elif marks>=70 and marks<80:
    print('grade B+')
elif marks>=60 and marks<70:
    print('grade B')    
elif marks>=50 and marks<70:
    print('grade C')
else:
    print('grade F')'''

#match case(compares value with different cases and returns the matched case value)
day=int(input('enter a number:'))
match day:
    case 1:
     print('monday')
    case 2:
      print('tuesday')
    case 3:
      print('wednesday')
    case 4:
      print('thursday')
    case 5:
      print('friday')
    case 6:
      print('saturday')
    case 6:
          print('sunday')  
    case _:
          print('enter number between 1 to 7')