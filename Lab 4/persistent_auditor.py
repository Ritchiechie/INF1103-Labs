import os

inventory = 0
failed_entries = 0
order_id = 1001
orders = []

def get_valid_input():
    get_product = input("Enter the product name: ")

    if get_product == "quit":
        return "quit"
    
    get_quantity = input("Enter the quantity: ")

    if get_quantity == "quit":
            return "quit"

    if get_quantity.isdigit():
        return [get_product, int(get_quantity)]
    
    else:
        print("Invalid input. Please enter a valid quantity or 'quit' to exit.")
        return None

def load_inventory():
    if os.path.exists("inventory.txt"):
        with open("inventory.txt", "r") as file:
            data = file.read()
    else:
        data = ""
    return data

def save_inventory():
    with open("inventory.txt", "w") as file:
        file.writelines(str(orders))

print("Current Orders:")
print(load_inventory())

while True:
    user_input = get_valid_input()
    
    if user_input == "quit":
            break

    elif user_input is None:
         failed_entries += 1

    else:
         product = user_input[0]
         quantity = user_input[1]
         orders.append([order_id, product, quantity])
         order_id += 1
         save_inventory()
         print("New Order Added:\n", orders)
