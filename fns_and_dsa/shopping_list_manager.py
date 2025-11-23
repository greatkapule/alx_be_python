def display_menu():
    """Prints the main menu options."""
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("----------------------------")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter item to add: ").strip().capitalize()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
        
        elif choice == '2':
            item_to_remove = input("Enter item to remove: ").strip().capitalize()
            
            try:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            except ValueError:
                print(f"Error: '{item_to_remove}' not found in the list.")
        
        elif choice == '3':
            if shopping_list:
                print("\n🛒 Current Shopping List:")
                print("\n".join(f"{i}. {item}" for i, item in enumerate(shopping_list, 1)))
            else:
                print("Your shopping list is currently empty.")
        
        elif choice == '4':
            print("Goodbye! Thank you for using the Shopping List Manager.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()