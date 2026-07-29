#patterns building
#square using while
'''i=1
while i<6:
    j=1
    while j<6:
        print('*',end=' ')
        j+=1
    print( )
    i+=1'''

#square using for loop
'''for i in range(5):
      for j in range(5):
            print('*',end=' ')
      print( )    
'''


#right angle triangle using while
'''i=1
while i<6:
    j=1
    while j<6:
        if j<=i:
         print('*',end=' ')
        j+=1
    print( )
    i+=1   '''

#right angle triangle using for loop
'''for i in range(1,6):
    for j in range(i):
        print('*',end=' ')
    print ( )'''

#revere of right angle using while
'''i=1
while i<6:
      j=1
      while j<6:
            if j>=i:
                  print('*',end=' ')
            j+=1
      print( )
      i+=1  '''  
  
# revere of right angle using for loop
'''for i in range(5,0,-1):
      for j in range(i):
            print ('*',end=' ')
      print( )'''


#right angle triangle for numbers (1 to 5) using while
'''i=1
num=1
while i<6:
   
   j=1
   while j<6:
       if j<=i:
      
        print(num,end=' ')
       j+=1 
   print( )
   num+=1
   i+=1'''

#right angle triangle for numbers (1 to 5 repeat) using for
'''num=1
for i in range(1,6):
    for j in range(i):
        print(num,end=' ')
    num+=1
    print ( )'''

#right angle triangle for 1 to 5 using while
'''i=1

while i<6:

   j=1
   while j<6:
       if j<=i:
      
        print(j,end=' ')
       j+=1 
   print( )

   i+=1'''


#right angle for 1 to 15 numbers using while
'''num=1
i=1
while i<6:
    j=1
    while j<=i:
        
            print(num,end=' ')
            num+=1
            j+=1
    print( )
    i+=1 '''      
#right angle for 1 to 15 numbers using for
'''num=1
for i in range(1,6):
    for j in range(i):
            print(num,end=' ')
            num+=1
    print( )  '''
#right angle from a to o (ascii) using while

'''ch=65
i=1
while i<6:
      j=1
      while j<=i:
            print(chr(ch),end=' ')
            ch+=1
            j+=1
      print( )
      i+=1'''

#pyramid using while loop 
'''i=1
while i<6:
      print(' '*(5-i)+'* '*i)
      i+=1'''


