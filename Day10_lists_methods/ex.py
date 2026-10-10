#list methods

#append
l=[1,2,3,4,5,6,7,8,9,10]
l.append(11)    #append() method is used to add the mentioned element at the end of the list
print(l)

#copy
l=[1,2,3,4,5,6,7,8,9,10]
l1=l
l2=l.copy()  #copy() method is used to return a shallow copy of the list(half address is same for both list and half is different)
print(id(l))
print(id(l2))
print(l2)

#extend
l=[1,2,3,4,5,6,7,8,9,10]
l.extend('python')  #extend() method is used to add the elements at the end of the list
print(l)

#insert
l=[1,2,3,4,5,6,7,8,9,10]
l.insert(3,15)  #insert() method is used to add the mentioned element at the mentioned index in the list
print(l)

#count
l=[1,2,3,4,5,6,7,8,9,10,5,5,5]
print(l.count(5))

#remove
l=[1,2,3,4,5,6,7,8,9,10]
l.remove(5)  #remove() method is used to remove the first occurrence of the mentioned element from the list
print(l)

#pop
l=[1,2,3,4,5,6,7,8,9,10]
l.pop()  #pop() method is used to remove the last element from the list
print(l)

#reverese
l=[1,2,3,4,5,6,7,8,9,10]
l.reverse()  #reverse() method is used to reverse the elements of the list
print(l)

#sort
l=[90,50,40,10,70,20,60,80,100,30]
l.sort()   #sort() method is used to sort the elements of the list in ascending order
print(l)
l.sort(reverse=True)  #sort() method is used to sort the elements of the list in descending order
print(l)

#clear
l=[1,2,3,4,5,6,7,8,9,10]
l.clear()  #clear() method is used to remove all the elements from the list but the list will still exist[]
print(l)

#delete
l=[1,2,3,4,5,6,7,8,9,10]
del l  #del() method is used to delete the list completely
