class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"{self.name} - ${self.price}")

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_cart(self):
        for product in self.products:
            product.show_info()

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        print(f"Total: ${total}")

product1 = Product("Laptop", 1000)
product2 = Product("Phone", 500)
product3 = Product("Mouse", 50)

cart = Cart()

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

cart.show_cart()
cart.total_price()