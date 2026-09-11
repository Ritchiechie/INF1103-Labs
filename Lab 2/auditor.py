inventory = 0

while True:
    quantity = input("Enter the quantity of items to add to inventory: ")
    if quantity == "quit":
        print("Exiting program....")
        break

    elif quantity.isdigit():
        quantity = int(quantity)
        quantity += inventory

    else: 
        print("Invalid input. Please enter a valid quantity or 'quit' to exit.")
        
        
