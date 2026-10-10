def remove_from_cart(cart):
    if not cart:
        print("\nYour cart is empty!")
        return

    print("\n----- YOUR SHOPPING CART -----")

    for index, product in enumerate(cart, start=1):
        print(index, ".", product['name'], "-", product['price'])

    try:
        choice = int(input('Enter the item number to remove: '))

        if choice < 1 or choice > len(cart):
            print("Invalid item number!")
            return

        removed_product = cart.pop(choice - 1)

        print(removed_product['name'], "removed from cart successfully!")

    except ValueError:
        print("Please enter a valid number.")