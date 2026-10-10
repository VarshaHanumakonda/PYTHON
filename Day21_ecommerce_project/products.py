products = [
    {'id': 1, 'name': 'Laptop', 'price': 45000},
    {'id': 2, 'name': 'Mobile Phone', 'price': 20000},
    {'id': 3, 'name': 'Headphones', 'price': 1500},
    {'id': 4, 'name': 'Keyboard', 'price': 800},
    {'id': 5, 'name': 'Mouse', 'price': 500}
]


def display_products():
    print("\n----- AVAILABLE PRODUCTS -----")
    print("ID\tProduct Name\t\tPrice")

    for product in products:
        print(product['id'], "\t", product['name'], "\t\t", product['price'])