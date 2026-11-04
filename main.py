# Display the seven choices for The Grill.
def show_menu():
    print("\nThe Grill - Restaurant Sales & Inventory Manager")
    print("1. View inventory")
    print("2. Add or restock an item")
    print("3. Record a sale")
    print("4. Show low-stock alerts")
    print("5. Sales report with charts")
    print("6. Run 30-day simulation")
    print("7. Save and exit")


# Repeat the menu until the user chooses to exit.
def main():
    choice = ""
    while choice != "7":
        show_menu()
        choice = input("Choose an option (1-7): ").strip()
        if choice in ["1", "2", "3", "4", "5", "6"]:
            print("Coming soon")
        elif choice == "7":
            print("Goodbye! Saving will be added in Week 3.")
        else:
            print("Please choose a menu option from 1 to 7.")


main()
