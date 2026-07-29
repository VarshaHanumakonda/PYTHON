#while loop(centinal loop) (works based on condition)

#print numbers from 1 to 10
i=1             # i value is the 1st no from where the loop will start
while i<11:     #checks the condition 
    print(i)    #then prints i if the condition is true
    i+=1        # adds 1 to i until the condition becomes false #when the condition becomes false then loop will terminate


#print numbers from 1 to 100
i=1
while i<101: # < symbol used for ascending order # whatever the last no is add 1 to it in the condition
    print(i)
    i+=1


#print numbers from 10 to 1
i=10
while i>0: # > symbol used for descending order # whatever the last no is subtract 1 from it in the condition
    print(i)
    i-=1    # use - symbol for descending order


#print even numbers from 1 to 20
i=2
while i<21:
    print(i)
    i+=2


#print odd numbers from 1 to 20
i=1
while i<21:
    print(i)
    i+=2




#for loop(for each loop) (works based on sequence and range)

#print numbers from 1 to 10 and characters using sequence
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)
b=['P','Y','T','H','O','N']
for i in b:
    print(i)

#print 10 numbers using range with only stop value
for i in range(11):  # range(n) only stop value is written so default start value is 0
    print(i)

#print 10 numbers using range with start and stop value
for i in range (1,11):
    print(i)

#print odd numbers from 1 to 10 using range with start, stop and step value
for i in range (1,11,2): # 1 is start value, 11 is stop value, 2 is step value
    print(i)

for i in range (0,10,1): # default step value is 1
    print(i)
