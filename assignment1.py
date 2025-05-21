#Assignment: Create an inventory management - Use loops to display or update a list of stock items.

print("Welcome to the Inventory Management System!")
print("To manage your inventory, please choose an option:")
print("1. View inventory")
print("2. Add item to inventory")
print("3. Remove item from inventory")
print("4. Update item quantity")
print("5. Exit")
inventory = ["bread", "milk", "eggs", "butter", "cheese"]
while True:
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        print("Current inventory:")
        for item in inventory:
            print(item)
    
    elif choice == '2':
        new_item = input("Enter the item to add: ")
        inventory.append(new_item)
        print(f"Item {new_item} added to inventory.")
    
    elif choice == '3':
        remove_item = input("Enter the item to remove: ")
        if remove_item in inventory:
            inventory.remove(remove_item)
            print(f"Item {remove_item} removed from inventory.")
        else:
            print(f"Item {remove_item} not found in inventory.")
    
    elif choice == '4':
        update_item = input("Enter the item to update: ")
        if update_item in inventory:
            new_item = input("Enter the new item: ")

            index = inventory.index(update_item)
            inventory[index] = new_item
            print(f"Item {update_item} updated to item {new_item}.")
        else:
            print(f"Item {update_item} not found in inventory.")
    
    elif choice == '5':
        print("Exiting Inventory Management System. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")