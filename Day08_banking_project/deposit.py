def deposit_money(customer):
    try:
        amount = int(input("Enter deposit amount: "))

    except ValueError:
        print("Enter a valid amount.")

    else:
        if amount > 0:
            customer['balance'] += amount
            print("Amount Deposited successfully.")
            print("Current balance is:", customer['balance'])

        else:
            print("Deposit amount must be greater than 0.")

    finally:
        print("Transaction completed.")
