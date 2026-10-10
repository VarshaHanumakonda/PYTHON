#string methods
a=10
s='Hello world'
print(a.__sizeof__())        #__sizeof__() method is used to return the size of the object in bytes
print(s.__sizeof__())

#formatting methods
s='hello world'
print(len(s))
print(s.ljust(15,'$'))    #ljust() method is used to adjust the str to left and fill the remaining space with mentioned character
print(s.rjust(15,'$'))    #rjust() method is used to adjust the str to right and fill the remaining space with mentioned character
print(s.zfill(15))         #zfill() method is used to fill the remaining space with zeros (same like rjust it adjust str to right)

#searching methods
s='achieversIT'
s1=s.find('e')          #find() method is used to find the index of the mentioned letter or chr in str
print(s1)
print(s.rfind('e'))     #rfind() method is used to find the index from right side of the str
print(s.index('v'))     #index() method is used to return the index value of the mentioned chr
print(s.count('e'))      #count() method is used to count how mant times the chr or letter is repeated in str

#prefix and suffix methods
s='achieversIT'
print(s.startswith('a'))  #startswith() method is used to check whether the str starts with the mentioned letter or not
print(s.endswith('T'))    #endswith() method is used to check whether the str ends with the mentioned letter or not
print(s.removeprefix('ach'))  #removeprefix() method is used to remove the mentioned prefix from the str
print(s.removesuffix('IT'))  #removesuffix() method is used to remove the mentioned suffix from the str

#case conversion methods
s='achieversIT'
print(s.upper())    #upper() method is used to convert the whole str into capital letters
print(s.lower())    #lower() method is used to convert the whole str into small letters
print(s.capitalize())   #capitalize() method is used to convert the first letter of the str into capital letter
print(s.swapcase())    #swapcase() method is used to convert the capital letters into small letters and small letters into capital letters
s1='today is a good day'
print(s1.title())   #title() method is used to convert the first letter of each word in sentence into capital letter

#splitting and joining methods
s='/'
s1='abc'
print(s.join(s1))   #join() method is used to join the str with the mentioned chr or letter
a='peter parker jason is good'
print(a.split())    #split() method is used to split the str into words and returns a list of words
print(a.rsplit())  #rsplit() method is used to split the str into words from right side and returns a list of words
print(a.partition('jason')) #partition() method is used to split the str into 3 parts  and returns a tuple of 3 parts
print(a.rpartition('peter')) #rpartition() method is used to split the str into 3 parts from right side and returns a tuple of 3 parts
b='''hi there,
how are you?
 welcome to vs code'''
print(b.splitlines())  #splitlines() method is used to split the str into lines and returns in form of a list of lines





#string formatting methods

product='Hard disk'
size=500
price=199.23

#1) c style formatting (%)
print('%s of %i GB is costing about %g dollers' %(product,size,price))

#2) .format (.format())
print('{0} of {1} GB is costing about {2} dollers'.format (product,size,price))

#3) f string formatting (f')
print(f'{product} of {size} GB is costing about {price} dollers')