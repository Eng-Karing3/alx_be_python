

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = [] # Explicitly declared as empty list (array in some contexts)

    while True:
        display_menu() # Explicitly calling display_menu
        
        # Original skeleton implies string input, but "as a number" suggests int conversion
        # Let's try to convert to int and then compare as int
        try:
            choice = int(input("Enter your choice: ").strip()) # Ensure input is treated as a number
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue # Skip to the next loop iteration

        if choice == 1: # Compare as integer
            # Prompt for and add an item
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add:
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")
        elif choice == 2: # Compare as integer
            # Prompt for and remove an item
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
        elif choice == 3: # Compare as integer
            # Display the shopping list
            print("\n--- Your Shopping List ---")
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            print("--------------------------")
        elif choice == 4: # Compare as integer
            print("Goodbye!")
            break
        else:
            # For choices outside 1-4 but still numeric
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
