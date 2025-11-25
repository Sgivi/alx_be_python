def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            item_name = input("Enter item name: ")
            shopping_list.append(item_name)
            print(f"{item_name} added!")
            
        elif choice == 2:
            item_name = input("Enter item name to remove: ")
            if item_name in shopping_list:
                shopping_list.remove(item_name)
                print(f"{item_name} removed!")
            else:
                print(f"{item_name} not found in the list.")
            
        elif choice == 3:
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is empty.")
            
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()