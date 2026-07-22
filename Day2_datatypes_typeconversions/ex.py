f=12.59
print(type(f))
f1=1259e-2
print(f1)

c=12+5j
print(type(c))
print(c)
print(id(c))

b=True
print(type(b))
print(id(b))

s='AchiversIT'
s1='''this represents a multi line string'''
print(type(s))
print(s)
print(id(s))
print(type(s1))
print(s1)
print(id(s1))

#type conversions
#int
#str
#float
#bool
#complex

#type conversions(int)
#conversion of str to int
s='32'
i=int(s)
print(type(i),i)
print(id(i))
#conversion of float to int
f=12.59
i=int(f)
print(type(i),i)
print(id(i))
#conversion of bool to int
b1=True
b2=False
i=int(b1)
print(type(i),i)
i1=int(b2)
print(type(i1),i1)
#conversion of complex to int
# c=12+5j
# i=int(c)
# print(type(i),i)
# print(id(i))

#type conversions(str)
#conversion of int to str
i=32
s=str(i)
print(type(s),s)
print(id(s))
#conversion of float to str
f=12.59
s=str(f)
print(type(s),s)
print(id(s))
#conversion of bool to str
b1=True
b2=False
s1=str(b1)
print(type(s1),s1)
print(id(s1))
s2=str(b2)
print(type(s2),s2)
print(id(s2))
#conversion of complex to str
c=12+5j
s=str(c)
print(type(s),s)
print(id(s))
#type conversions(float)
#conversion of int to float
i=32
f=float(i)
print(type(f),f)
print(id(f))
#conversion of str to float
s='12.59'                     #str having decimal can be converted but str having char
f=float(s)
print(type(f),f)
print(id(f))
#conversion of bool to float
b1=True
b2=False
f1=float(b1)
print(type(f1),f1)
print(id(f1))
f2=float(b2)
print(type(f2),f2)
print(id(f2))
#conversion of complex to float
# c=12+5j
# f=float(c)
# print(type(f),f)    #complex to float is not possible
# print(id(f))

#type conversions(bool)
#conversion of int to bool
i=5
b=bool(i)
print(type(b),b)
print(id(b))
i1=0
b1=bool(i1)
print(type(b1),b1)
#conversion of str to bool
s='characters'
b=bool(s)
print(type(b),b)
print(id(b))
s1=''              #empty string=false
b1=bool(s1)
print(type(b1),b1)
print(id(b1))
#conversion of float to bool
f=12.59
b=bool(f)
print(type(b),b)
print(id(b))
f1=0.0             #0.0=false for bool
b1=bool(f1)
print(type(b1),b1)
print(id(b1))
#conversion of complex to bool
c=12+5j
b=bool(c)
print(type(b),b)
print(id(b))
#type conversions(complex)
#conversion of int to complex
i=5
c=complex(i)
print(type(c),c)
print(id(c))
#conversion of str to complex
s='12+5j'
c=complex(s)
print(type(c),c)
print(id(c))
#conversion of float to complex
f=12.59
c=complex(f)
print(type(c),c)
print(id(c))
#conversion of bool to complex
b1=True
b2=False
c1=complex(b1)
print(type(c1),c1)
print(id(c1))
c2=complex(b2)
print(type(c2),c2)
print(id(c2))