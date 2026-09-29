inventory = 0
failed_entries = 0
deliveries = 0
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
    with open("C:\\School\\Trimester 1\\INF1103-Programming Fundamentals with DevOps\\Labs\\Lab 4\\inventory.txt", "r") as file:
        data = file.read()
    print(data)
    
load_inventory()

while True:
    user_input = get_valid_input()
    
    if user_input == "quit":
            break

    elif user_input is None:
         failed_entries += 1

    else:
         product = user_input[0]
         quantity = user_input[1]
         orders.append(user_input)
         with open("C:\\School\\Trimester 1\\INF1103-Programming Fundamentals with DevOps\\Labs\\Lab 4\\inventory.txt", "a") as file:
            file.writelines(str(orders))
         print("Order added. Current orders:", orders)
