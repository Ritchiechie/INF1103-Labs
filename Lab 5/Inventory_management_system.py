import json
import os

def display_all(inventory):
    print("\nCurrent Inventory")
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
    print("\nProduct added successfully!")


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
        print("inventory.json found.")
        print("Inventory loaded successfully.")

    else:
        inventory = []
        print("\ninventory.json not found. Starting with an empty inventory.\n")
    return inventory


def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file)
    print("Inventory saved successfully to inventory.json.")


def menu():
    print("=" * 50)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)
    
    inventory = load_inventory()   

    while True:
        print("----------MENU----------")
        print("1. Display All Products")
        print("2. Add Product")     
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Quit") 

        option = input("\nEnter option: ")

        if option.isdigit():
            option = int(option)
            if option == 1:
                display_all(inventory)
            elif option == 2:
                add_product(inventory)
            elif option == 3:
                update_stock(inventory)
            elif option == 4:
                search_product(inventory)
            elif option == 5:
                print("Saving inventory...")
                save_inventory(inventory)
            elif option == 6:
                print("\nSaving Inventory before exit...")
                save_inventory(inventory)
                print("\nThank you for using the Inventory Management System.")
                print("Program terminated.")
                break
        else:
            print("Invalid option. Please try again.")


menu()
