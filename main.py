inventory = {
    "burger": {"price": 9.50, "qty": 30, "reorder": 10},
    "fries": {"price": 3.50, "qty": 25, "reorder": 8},
    "chicken sandwich": {"price": 8.50, "qty": 20, "reorder": 6}
}


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


# Display each menu item's price, quantity, and reorder level.
def view_inventory(inventory):
    print("\nCurrent inventory")
    for item in inventory:
        print("Item:", item)
        print("  Price: $", inventory[item]["price"])
        print("  Quantity in stock:", inventory[item]["qty"])
        print("  Reorder level:", inventory[item]["reorder"])


# Check that text contains only the digits used in ordinary numbers.
def only_digits(text):
    if text == "":
        return False
    for character in text:
        if character not in "0123456789":
            return False
    return True


# Ask for a whole number within the allowed range.
def read_quantity(prompt, minimum, maximum):
    while True:
        text = input(prompt).strip()
        if not only_digits(text) or len(text) > 6:
            print("Enter a whole number using at most 6 digits.")
        else:
            number = int(text)
            if number < minimum or number > maximum:
                print("Enter a number from", minimum, "to", maximum)
            else:
                return number


# Ask for a positive price before converting the text to a number.
def read_price():
    while True:
        text = input("Price (example 4.50): ").strip()
        digits = text.replace(".", "", 1)
        if not only_digits(digits) or len(text) > 7:
            print("Enter a positive price using at most 7 characters, like 4.50.")
        else:
            price = float(text)
            if price <= 0 or price > 9999.99:
                print("Price must be more than 0 and no more than 9999.99.")
            else:
                return price


# Restock an existing item or collect details for a new item.
def add_item(inventory):
    item = input("Item name: ").strip().lower()
    while item == "":
        print("Please enter an item name.")
        item = input("Item name: ").strip().lower()

    if item in inventory:
        available_space = 999999 - inventory[item]["qty"]
        if available_space == 0:
            print("This item already has the maximum stock of 999999.")
            return
        quantity = read_quantity("Units to add: ", 1, available_space)
        inventory[item]["qty"] = inventory[item]["qty"] + quantity
        print("Updated quantity for", item, ":", inventory[item]["qty"])
    else:
        price = read_price()
        quantity = read_quantity("Starting quantity: ", 0, 999999)
        reorder = read_quantity("Reorder level: ", 0, 999999)
        inventory[item] = {"price": price, "qty": quantity, "reorder": reorder}
        print("Added", item, "to inventory.")


# Repeat the menu until the user chooses to exit.
def main():
    choice = ""
    while choice != "7":
        show_menu()
        choice = input("Choose an option (1-7): ").strip()
        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice in ["3", "4", "5", "6"]:
            print("Coming soon")
        elif choice == "7":
            print("Goodbye! Saving will be added in Week 3.")
        else:
            print("Please choose a menu option from 1 to 7.")


main()
