#arithmetic operator
a=40
b=30
c=a+b      # + operator
print(c)
c=a-b      # - operator
print(c)
c=a*b      # * operator
print(c)
c=a/b      # / operator gives float value as output
print(c)
c=a//b     # // operator gives integer value as output
print(c)
c=a%b      # % operator gives remainder value as output
print(c)
c=a**b     # ** operator gives power value as output
print(c)

#assignment operator
a=15
print(id(a),a)
a+=5           # a=a+5 a=15+5=20
print(id(a),a)
a-=5         # a=a-5 a=20-5=15
print(id(a),a)
a*=5         # a=a*5 a=15*5=75
print(id(a),a)
a/=5         # a=a/5 a=75/5=15.0
print(id(a),a)
a//=5        # a=a//5 a=15.0//5=3.0
print(id(a),a)
a%=5         # a=a%5 a=3.0%5=3.0
print(id(a),a)

#comparison/relational operator
a=20
b=10
print(a==b)      #gives boolean value as output
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)

#logical operator
a=20
b=10
print(a>b and a<b)  #gives boolean value as output if both conditions are true
a=30
b=40
print(a<b or a>b)   #gives boolean value as output if at least one condition is true
a=50
b=20
print(not a>b)     #gives opposite boolean value as output

#membership operator
l=[10,20,30,40,50,60,70,80]
print(30 in l)   #gives boolean value true as output if 30 is present in list l
print(90 not in l)  #gives boolean value true as output if 90 is not present in list l
print(90 in l)   #gives boolean value false as output if 90 is not present in list l

#identity operator
a=10
b=10
print(a is b) #gives boolean value true as output if both a and b are same

print(a is not b) #gives boolean value false as output if both a and b are not same
