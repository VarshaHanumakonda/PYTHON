def login_customer():
    Username = input('Enter your user name: ')
    password = input('Enter your password: ')

    try:
        with open('users.txt', 'r') as file:
            for line in file:
                details = line.rstrip('\n').split('|')

                if len(details) == 3:
                    if details[1] == Username and details[2] == password:
                        print("Login successful! Welcome", details[0])
                        return details[1]

        print("Login failed! Invalid username or password.")
        return None

    except FileNotFoundError:
        print("No registered customers found. Please register first.")
        return None