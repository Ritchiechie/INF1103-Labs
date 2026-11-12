import json
import os

from product import Product
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

def load_inventory() -> Inventory:
    inventory = Inventory()
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            data = json.load(file)
        suppliers: dict[str, Supplier] = {}
        for item in data:
            s = item["supplier"]
            if s["id"] not in suppliers:
                suppliers[s["id"]] = Supplier(s["id"], s["name"], s["contact_email"])
            supplier = suppliers[s["id"]]
            if item["type"] == "physical":
                product = PhysicalProduct(item["id"], item["name"], item["price"],
                                          item["stock"], supplier, item["weight"])
            elif item["type"] == "digital":
                product = DigitalProduct(item["id"], item["name"], item["price"],
                                         item["stock"], supplier, item["download_size"])
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
            print("1. Physical Product")
            print("2. Digital Product")
            product_type = input("Choose product type: ")
            product_id = input("Product ID: ")
            name = input("Product Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock Quantity: "))
            supplier_id = input("Supplier ID: ")
            supplier_name = input("Supplier Name: ")
            supplier_email = input("Supplier Email: ")
            supplier = Supplier(supplier_id, supplier_name, supplier_email)

            if product_type == "1":
                weight = float(input("Weight (kg): "))
                product = PhysicalProduct(product_id, name, price, stock, supplier, weight)
                inventory.add_product(product)
                print("Product added successfully!")
            elif product_type == "2":
                download_size = float(input("Download Size (MB): "))
                product = DigitalProduct(product_id, name, price, stock, supplier, download_size)
                inventory.add_product(product)
                print("Product added successfully!")
            else:
                print("Invalid product type.")

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