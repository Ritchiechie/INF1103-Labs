inventory = 0
failed_entries = 0

def get_valid_input():
    get_input = input("Enter the quantity of items to add to inventory: ")

    if get_input.isdigit():
        return int(get_input)
   
    elif get_input == "quit":
        return "quit"
    else:
        print("Invalid input. Please enter a valid quantity or 'quit' to exit.")
        return None

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    print("Inventory updated. Current total:", new_total)
    return new_total 

while True:
    user_input = get_valid_input()
    
    if user_input == "quit":
            print("Exiting program....")
            print("Total units processed: ", inventory)
            print("Failed/Rejected entries: ", failed_entries)
            break

    elif user_input is None:
         failed_entries += 1

    else:
        inventory = process_delivery(inventory, user_input)

   
        
        
        
