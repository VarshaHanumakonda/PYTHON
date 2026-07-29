name=input('enter your name:')
username=input('enter your username:')
password=input('enter your password:')
balance=int(input('enter your balance:'))
print('registration succesful')
uname=input('username:')
pword=input('password:')
if uname==username and pword==password:
    print('login successful')
while True:
    print('''welcome to python bank
    1. withdraw
    2. deposit
    3. balance enquiry
    4. exit
''')
    choice=int(input('enter your choice:'))
    match choice:
        case 1:
            wamount=int(input('enter the withdrawal amount:'))
            if balance>=wamount:
                balance-=wamount
                print('your money has been withdraw and your current balance is',balance)
            else:
                print('insufficent balance')
        case 2:
            damount=int(input('enter the depositing amount:'))
            if damount>0:
                balance+=damount
                print('your money has been deposited and your current balance is',balance)
            else:
                print('deposit unsuccesful')
        case 3:
            print('your current balance is',balance)
        case 4:
            print('thank you!!')
            break
                                    
