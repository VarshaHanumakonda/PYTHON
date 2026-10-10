
from registration import registration_customer
from login import login_customer
from withdraw import withdraw_money
from deposit import deposit_money

customers={}

while True:
 print(''' welcome to python bank
 1. register
 2.login
 3.exit
''')
 choice=int(input('enter your choice:'))
 match choice:
     case 1:
            registration_customer(customers)
            print(customers)


     case 2:
            customer = login_customer(customers)
            if customer is not None:
                while True:
                    print('''
    1. withdraw
    2. deposit
    3. balance enquiry
    4. exit
''')
                    choice=int(input('enter your choice:'))
                    match choice:
                           case 1:
                            withdraw_money(customer)


                           case 2:

                            deposit_money(customer)


                           case 3:

                            print(
                                'Your current balance is:',
                                customer['balance']
                            )


                           case 4:

                            print('Logged out successfully!')
                            break


                           case _:

                            print('Invalid choice')


     case 3:
       print('thank you!')
       break
     case _:
       print('you have entered an invalid choice')
                             
                      

                                    
