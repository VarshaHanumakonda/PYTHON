def login_customer(customers):

    try:
        uname = input("Username: ")
        pword = input("Password: ")

    except Exception:
        print("Login error! enter valid username or password")
        return None

    else:
        if uname in customers:

            if customers[uname]["password"] == pword:
                print("Login successful!")
                return customers[uname]

        print("Invalid username or password")
        return None

                             

