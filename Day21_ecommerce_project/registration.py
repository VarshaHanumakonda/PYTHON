def registration_customer():
    Name = input('Enter your Name: ')
    Username = input('Enter your user name: ')
    password = input('Enter your password: ')

    if not Name or not Username or not password:
        print("Registration failed! All fields are required.")
        return

    try:
        with open('users.txt', 'r') as file:
            for line in file:
                details = line.rstrip('\n').split('|')

                if len(details) == 3 and details[1] == Username:
                    print("Registration failed! Username already exists.")
                    return

    except FileNotFoundError:
        pass

    with open('users.txt', 'a') as file:
        file.write(Name + '|' + Username + '|' + password + '\n')

    print("Registration successful!")