def view_cart(cart):
    if not cart:
        print("\nYour cart is empty!")
        return

    total = 0

    print("\n----- YOUR SHOPPING CART -----")
    print("Product Name\t\tPrice")

    for product in cart:
        print(product['name'], "\t\t", product['price'])
        total = total + product['price']

    print("------------------------------")
    print("Total Amount:", total)