file=open('sample.txt','w')
file.write('''hi there!
how are you doing
i am doing great
thank you''')
print(file.tell())
file.close()

file=open('sample.txt','r')
txt=file.readlines()
print(txt)
file.close()