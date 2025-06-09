def display_menu():
    """
    Displays the menu options for the shopping list manager.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager.
    Initializes the shopping_list and handles user interaction.
    """
    shopping_list = [] 

    while True:
        display_menu() 
        choice = input("Enter your choice: ").strip() 

        if choice == '1':
           
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add:
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")
        elif choice == '2':
           
            if not shopping_list:
                print("Your shopping list is already empty. Nothing to remove.")
                continue 
            
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove: 
                try:
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' has been removed from your shopping list.")
                except ValueError:
                    
                    print(f"'{item_to_remove}' was not found in your shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")
        elif choice == '3':
            
            print("\n--- Your Shopping List ---")
            if not shopping_list: 
                print("Your shopping list is empty.")
            else:
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            print("--------------------------")
        elif choice == '4':
            
            print("Goodbye!")
            break 
        else:
            
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
