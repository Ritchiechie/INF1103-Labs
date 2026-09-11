inventory = 0

while True:
    quantity = input("Enter the quantity of items to add to inventory: ")
    if quantity == "quit":
        print("Exiting program....")
        print(inventory)
        break

    elif quantity.isdigit():
        quantity = int(quantity)
        inventory += quantity
        print(inventory)

        if inventory >= 500:
            print("Inventory limit reached!!!")
            break

    else: 
        print("Invalid input. Please enter a valid quantity or 'quit' to exit.")
        
        
