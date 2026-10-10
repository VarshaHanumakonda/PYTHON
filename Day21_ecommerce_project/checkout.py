def checkout(username, cart):
    if not cart:
        print("\nYour cart is empty! Add products before checkout.")
        return

    total = 0

    for product in cart:
        total = total + product['price']

    print("\n----- CHECKOUT -----")
    print("Total Amount:", total)

    confirm = input("Confirm your order? (yes/no): ").lower()

    if confirm == 'yes':
        try:
            with open('orders.txt', 'a') as file:
                file.write("Username: " + username + "\n")

                for product in cart:
                    file.write(
                        product['name'] + " - " +
                        str(product['price']) + "\n"
                    )

                file.write("Total Amount: " + str(total) + "\n")
                file.write("------------------------------\n")

            print("Payment successful!")
            print("Order placed successfully!")

            cart.clear()

        except OSError:
            print("Unable to save your order. Please try again.")

    else:
        print("Order cancelled.")