from registration import registration_customer
from login import login_customer
from products import products, display_products
from add_to_cart import add_to_cart
from view_cart import view_cart
from remove_from_cart import remove_from_cart
from checkout import checkout

while True:
    print("""
===== PYTHON E-COMMERCE STORE =====
1. Register
2. Login
3. Exit
""")

    try:
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                registration_customer()

            case 2:
                username = login_customer()

                if username is not None:
                    cart = []

                    while True:
                        print("""
===== CUSTOMER MENU =====
1. View Products
2. Add to Cart
3. View Cart
4. Remove from Cart
5. Checkout
6. Logout
""")

                        try:
                            choice = int(input("Enter your choice: "))

                            match choice:
                                case 1:
                                    display_products()

                                case 2:
                                    display_products()
                                    add_to_cart(products, cart)

                                case 3:
                                    view_cart(cart)

                                case 4:
                                    remove_from_cart(cart)

                                case 5:
                                    checkout(username, cart)

                                case 6:
                                    print("Logged out successfully!")
                                    break

                                case _:
                                    print("Invalid choice!")

                        except ValueError:
                            print("Please enter a valid number.")

            case 3:
                print("Thank you for visiting our store!")
                break

            case _:
                print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number.")