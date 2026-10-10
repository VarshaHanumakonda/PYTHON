import random


characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
captcha=" "
for i in range(8):
    captcha+=random.choice(characters) 
print('your captcha is:',captcha)

