def withdraw_money(customer):
    try:
        amount = int(input("Enter withdrawal amount: "))

    except ValueError:
        print("Enter a valid amount.")

    else:
        if amount <= 0:
            print("Invalid amount")
        elif customer['balance'] >= amount:
            customer['balance'] -= amount
            print("Money withdrawn successfully!")
            print("Your current balance is:", customer['balance'])
        else:
            print("Insufficient balance!")

    finally:
        print("withdrawal process is completed")
