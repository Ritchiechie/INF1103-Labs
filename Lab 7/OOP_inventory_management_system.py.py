import json
import os

from product import Product
from inventory import Inventory

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

def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    while True:
        print("----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        option = input("Enter option: ")

        if option == "1":
            inventory.display_all()

        elif option == "2":
            print("Add New Product")
            product_id = input("Product ID: ")
            name = input("Product Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock Quantity: "))
            product = Product(product_id, name, price, stock)
            inventory.add_product(product)
            print("Product added successfully!")

        elif option == "3":
            print("Update Stock")
            product_id = input("Enter Product ID: ")
            product = inventory.search_product(product_id)
            if product is None:
                print("Product not found.")
            else:
                print("Product Found:")
                print(f"Name: {product.get_name()}")
                print(f"Current Stock: {product.get_stock()}")
                new_stock = int(input("New Stock Quantity: "))
                product.update_stock(new_stock)

        elif option == "4":
            print("Search Product")
            product_id = input("Enter Product ID: ")
            product = inventory.search_product(product_id)
            if product is None:
                print("Product not found.")
            else:
                print("Product Found")
                print("-" * 50)
                product.display_information()
                print("-" * 50)

        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)

        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please try again.")

main()