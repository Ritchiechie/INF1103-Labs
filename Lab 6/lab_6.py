class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        if quantity < 0:
            print("Stock cannot be negative.")
        else:
            self.__stock = quantity
            print("Stock updated successfully!")

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def get_product_id(self):
        return self.__product_id

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        print("Current Inventory")
        print("-" * 50)
        for product in self.__products:
            product.display_information()
        print("-" * 50)

inventory = Inventory()
product1 = Product("P001", "Laptop", 1200.00, 15)
product2 = Product("P002", "Mouse", 25.50, 40)
inventory.add_product(product1)
inventory.add_product(product2)

inventory.display_all()

found = inventory.search_product("P999")
if found is not None:
    found.update_stock(50)
inventory.display_all()