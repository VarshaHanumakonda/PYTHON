def add_to_cart(products, cart):
    try:
        product_id = int(input('Enter the product ID: '))

        selected_product = None

        for product in products:
            if product['id'] == product_id:
                selected_product = product
                break

        if selected_product is None:
            print("Invalid product ID!")
            return

        quantity = int(input('Enter quantity: '))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        for i in range(quantity):
            cart.append(selected_product.copy())

        print("Product added to cart successfully!")

    except ValueError:
        print("Please enter a valid number.")