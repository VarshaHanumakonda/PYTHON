#set methods

#difference
s1={1,2,3,4,5}
s2={3,1,6,8,9}
print(s1.difference(s2)) #checks the 2 sets and prints the elements of 1st set that are NOT common in 2 sets 

#intersection
s1={1,2,3,4,5}
s2={3,1,6,8,9}
print(s1.intersection(s2)) #gives the common elements that are present in both the sets 

#union
s1={1,2,3,4,5}
s2={3,1,6,8,9}
print(s1.union(s2)) #gives all the elements from both the sets in a new set without repeating the elements

#isdisjoint
s1={1,2,3,4,5}
s2={3,1,6,8,9}
print(s1.isdisjoint(s2)) #gives True if both the sets have no common elements otherwise gives False

#issubset
s1={1,2,3,4,5}
s2={3,1,6,8,9}
print(s1.issubset(s2)) #gives True if all the elements of the first set are present in the second set otherwise gives False

#issuperset
s1={1,2,3,4,5}
s2={3,1,6,8,9}
print(s1.issuperset(s2)) #gives True if all the elements of the second set are present in the first set otherwise gives False

#symmetric_difference
s1={1,2,3,4,5}
s2={3,1,6,8,9}
print(s1.symmetric_difference(s2)) #gives the different elements from both sets.

#intersection_update
s1={1,2,3,4,5}
s2={3,1,6,8,9}
print(s1.intersection_update(s2)) #same like intersection but updates the first set with the result and returns none

#difference_update
s1={1,2,3,4,5}
s2={3,1,6,8,9}
print(s1.difference_update(s2)) #same like difference but updates the first set with the result and returns none

#symmetric_difference_update
s1={1,2,3,4,5}
s2={3,1,6,8,9}
print(s1.symmetric_difference_update(s2)) #gives the different elements from both sets and updates the first set with the result

#pop
s1={1,2,3,4,5}
s2={3,1,6,8,9}
print(s1.pop()) #removes any one element from the mentioned set .mentioned element cannot be removed in pop method

#discard
s1={1,2,3,4,5}
s2={3,1,6,8,9}
print(s1.discard(4)) #removes the element from the set if present otherwise does nothing

#update
s1={1,2,3,4,5}
s2={3,1,6,8,9}
print(s1.update({9,10})) #adds the elements from the given set to the first set

#set operations
'''print(s1 | s2)  # union
print(s1 & s2)  # intersection
print(s1 - s2) ''' # difference


#dictionary
'''d={1:'one',2:'2','data':[1,2,3]}
print(d[1])'''

#dictionary methods

#1) from keys
key=('name','roll no','branch')
d=dict.fromkeys(key,'unknown') #creates a dictionary with the given keys and assigns the same value to all the keys
print(d)

#2) get
keys={'name':'varsha','roll no':123,'branch':'ece'}
d=dict.get(keys,'name')  #gives the value of the key written
print(d)

#3) items
keys={'name':'varsha','roll no':123,'branch':'ece'}
d=dict.items(keys)  #gives the key value pairs in the form of tuples in a list
print(d)

#4) keys
keys={'name':'varsha','roll no':123,'branch':'ece'}
d=dict.keys(keys)  #gives the keys of the dictionary in the form of a list
print(d)

#5) values
keys={'name':'varsha','roll no':123,'branch':'ece'}
d=dict.values(keys)  #gives the values of the dictionary in the form of a list
print(d)

#6) pop
keys={'name':'varsha','roll no':123,'branch':'ece'}
d=dict.pop(keys,'roll no')  #removes the specified key and returns its value
print(d)

#7) popitem
keys={'name':'varsha','roll no':123,'branch':'ece'}
d=dict.popitem(keys)  #removes and returns last key-value pair from the dictionary
print(d)

#8) setdefault
keys={'name':'varsha','roll no':123,'branch':'ece'}
d=dict.setdefault(keys,'age',21)  #returns the value of the key if it exists, otherwise adds the key with the specified value and returns it
print(d)




