import json
import os

def load_inventory():
    inventory = Inventory()
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            data = json.load(file)
        for item in data:
            product = Product(item["id"], item["name"], item["price"], item["stock"])
            inventory.add_product(product)
        print("inventory.json found.")
        print("Inventory loaded successfully.")
    else:
        print("inventory.json not found. Starting with an empty inventory.")
    return inventory

def save_inventory(inventory):
    data = []
    for product in inventory.get_products():
        data.append(product.to_dict())
    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Inventory saved successfully to inventory.json.")

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

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

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

    def get_products(self):
        return self.__products

inventory = load_inventory()
inventory.display_all()
save_inventory(inventory)
