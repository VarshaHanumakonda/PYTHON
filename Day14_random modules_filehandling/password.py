#password using letters and digits
import random
import string
characters=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(8):
    password+=random.choice(characters)
print('your password is:',password)

#password using only numbers
import random
password=random.randint(100000,999999)
print('your password is:',password)