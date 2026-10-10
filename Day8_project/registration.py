def registration_customer(customers):
    Name = input('Enter your Name: ')
    Username = input('Enter your user name: ')
    password = input('Enter your password: ')

    try:
        balance = int(input('Enter your Balance: '))

        if balance < 0:
            print("Registration failed! Balance cannot be less than zero!")
            return      
    except ValueError:
            print(" registration failed! enter valid amount.")
            return
    else:
            customers[Name] = {
            'Username': Username,
            'password': password,
            'balance': balance
        }

            print("Registration successful!")
           
   
     