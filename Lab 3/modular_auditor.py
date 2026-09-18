inventory = 0
failed_entries = 0

def get_valid_input():
    return input("Enter the quantity of items to add to inventory: ")


while True:
    quantity = get_valid_input()

    if quantity == "quit":
        print("Exiting program....")
        print("Total units processed: ", inventory)
        print("Failed/Rejected entries: ", failed_entries)
        break

    elif quantity.isdigit():
        quantity = int(quantity)
        inventory += quantity
        if inventory >= 500:
            print("Inventory limit reached!!!")
            print(inventory)    
            break

    else: 
        failed_entries += 1
        print("Invalid input. Please enter a valid quantity or 'quit' to exit.")
        
        
