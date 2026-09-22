inventory = 0
failed_entries = 0
deliveries = 0

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

def calculate_tax(amount):
    tax = amount * 0.1
    return tax

def generate_report(total_units, failed_attempts):
    print("Generating report...")
    print("Total units processed: ", total_units)
    print("Failed/Rejected entries: ", failed_attempts)

while True:
    user_input = get_valid_input()
    
    if user_input == "quit":
            generate_report(deliveries, failed_entries)
            break

    elif user_input is None:
         failed_entries += 1

    else:
        inventory = process_delivery(inventory, user_input)
        tax_amount = calculate_tax(user_input)
        print("Tax amount for this delivery: ", tax_amount)
        deliveries += 1


   
        
        
        
