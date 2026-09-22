inventory = 0
failed_entries = 0

def get_valid_input():
    global inventory
    #global failed_entries

    quantity = input("Enter the quantity of items to add to inventory: ")
    
    if quantity.isdigit():
        quantity = int(quantity)
        inventory += quantity
        return quantity
    elif quantity == "quit":
        return "quit"
    else:
        print("Invalid input. Please enter a valid quantity or 'quit' to exit.")
        failed_entries += 1
        return failed_entries


while True:
    quantity = get_valid_input()

    if quantity == "quit":
            print("Exiting program....")
            print("Total units processed: ", inventory)
            print("Failed/Rejected entries: ", failed_entries)
            break

   
        
        
        
