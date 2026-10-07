import json
import os

def display_all(inventory):
    print("Current Inventory")
    print("-" * 50)
    for product in inventory:
        print(f"ID {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}, Stock: {product['stock']}")
    print("-" * 50)


def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    new_product = {"id": product_id, "name": name, "price": price, "stock": stock}
    inventory.append(new_product)
    print("Product added successfully!")


def update_stock(inventory):
    print("Update Stock")
    while True:
        product_id = input("Enter Product ID: ")
        found = False
        if product_id == "quit":
            break
        for product in inventory:
            if product["id"] == product_id:
                found = True
                print(f"Product found:\nName: {product['name']}\nCurrent Stock: {product['stock']}\n")
                new_stock = int(input("New Stock Quantity: "))
                product["stock"] = new_stock
                print("Stock updated successfully!")
                return
        if not found:
            print("Product not found. Please try again.")


def search_product(inventory):
    print("Search Product")
    while True:
        search_id = input("Enter Product ID: ")
        search = False
        if search_id == "quit":
            break
        for product in inventory:
            if product["id"] == search_id:
                search = True
                print("Product found\n")
                print("-" * 50)
                print(f"ID: {product['id']}\nName: {product['name']}\nPrice: ${product['price']:.2f}\nStock: {product['stock']}")
                print("-" * 50)
                return
        if not search:
            print("Product not found. Please try again.")


def load_inventory():
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
        print("inventory/json found.")
        print("Inventory loaded successfully.")

    else:
        inventory = []
        print("inventory.json not found. Starting with an empty inventory.")
    return inventory


inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
]

display_all(inventory)
search_product(inventory)
display_all(inventory)