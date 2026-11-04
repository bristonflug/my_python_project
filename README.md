# The Grill — Restaurant Sales & Inventory Manager

Week 2: Menu Loop and First Features

The Grill tracks menu items and stock. The final project will answer: "At what stock level should we reorder each menu item so we rarely run out?" The simulation that answers this question is planned for Week 5.

## Run on Windows in VS Code

1. Extract the entire ZIP using File Explorer's **Extract All**. Do not run the app from inside the ZIP.
2. In VS Code select **File > Open Folder**, choose the extracted `the-grill` folder, and click **Select Folder**.
3. Select **Terminal > New Terminal**.
4. Type `py main.py` and press Enter. If Windows does not recognize `py`, try `python main.py`.
5. Enter a menu number and press Enter.

The app needs Python 3 and no extra packages. The ZIP includes the `.git` folder with the actual development history. Keep that folder when moving the project.

## What works this week

- Option 1 displays each item's name, price, quantity, and reorder level.
- Option 2 restocks an existing item or adds a new item.
- Options 3–6 print `Coming soon`.
- Option 7 exits normally. Its label follows the plan, but saving begins in Week 3. Stock changes last only until this run ends.
- Invalid menu choices return to the menu. Invalid field values ask again.

Starter items: burger ($9.50, quantity 30, reorder 10), fries ($3.50, quantity 25, reorder 8), chicken sandwich ($8.50, quantity 20, reorder 6).

## Input rules

Item names are trimmed and stored in lowercase. Empty names are rejected. A new item needs a positive price of no more than 9999.99, entered using at most seven characters. Prices use a decimal point; currency symbols, commas, and scientific notation are rejected. For this milestone, a valid price is stored as entered after float conversion; it is not forced to two decimal places.

Whole-number inputs allow at most six digits. Starting stock and reorder levels allow 0–999999. Restocking requires at least one unit and cannot take total stock above 999999. A reorder level above current stock is allowed: it means stock is already below the planned threshold. Low-stock alerts arrive in a later milestone.

The digit check uses an ordinary loop over `0123456789`. This avoids accepting characters such as a superscript digit that cannot safely be converted with `int()`. Length limits prevent extremely long numbers from reaching numeric conversion. Negative values, blank input, letters, and malformed decimal prices are rejected before conversion. Like the classroom examples, the program expects a person to finish input normally and choose 7 to exit.

## Functions explained

| Function | Purpose |
| --- | --- |
| `show_menu()` | Prints the seven planned options. |
| `view_inventory(inventory)` | Loops through the dictionary and prints the details stored for each item. |
| `only_digits(text)` | Returns True only when every character is an ordinary digit and the input is not empty. |
| `read_quantity(prompt, minimum, maximum)` | Keeps asking until the text can safely become an integer within the specified range. |
| `read_price()` | Removes one decimal point for checking, validates the text, converts it to a float, and checks its range. |
| `add_item(inventory)` | Cleans the name, checks whether it exists, and updates stock or adds a nested dictionary. |
| `main()` | Repeats the menu, reads the choice, and calls the appropriate function. |

The final `main()` call starts the program. No main guard is used. Each function has a short comment above it.

## Questions to practice

**Why use a nested dictionary?** Each item name identifies a record containing its price, quantity, and reorder level.

**Why check before int() or float()?** Input is text. Checking first prevents invalid text from causing a conversion error.

**Why remove only one decimal point?** A price can have one decimal point. A second point remains and fails the digit check.

**Why strip and lowercase names?** ` BURGER ` should refer to the existing `burger` entry.

**How does restocking work?** The program adds the entered units to the quantity already stored in that item's record.

**Why pass inventory into functions?** They work with the same dictionary. Updating a value changes that dictionary, so the menu can display the updated stock.

**How does the menu stop?** Its while condition becomes false after the user enters `7`.

**What do the quantity limits do?** They keep stock nonnegative and bounded, require a positive restock amount, and keep extremely long numeric text from being converted.

**Does this version save or answer the reorder question?** Not yet. Saving and sales arrive in Week 3; the simulation arrives in Week 5.

## Week 2 rubric verification

| Category | Status and evidence |
| --- | --- |
| Menu loop | Passed: all seven choices, repeated menu, invalid choices, normal exit. |
| Data and view function | Passed: three starter items and all four details displayed. |
| Add/update function | Passed: existing stock increased and a new item appeared in inventory. |
| Validation and comments | Passed: letters, negatives, blanks, invalid menu choices, decimal quantities, malformed prices, Unicode digits, and oversized numeric text tested; comment above each function. |
| Git commits | Three real stages: menu loop; inventory/view; add/restock and validation. Each stage was run and tested before its commit. |
| Public GitHub repository | Verified public at https://github.com/bristonflug/my_python_project. All three development commits are present in the main branch history. No Canvas submission has been made. |

Development-only tests run outside this project folder using subprocess input and assertions. They are not part of the submitted application. The application imports no libraries and uses no try/except, comprehensions, lambda, classes, annotations, or type hints.

## Git history

Run these in the VS Code terminal if Git is installed:

```
git status
git log --oneline --reverse
```

The required commit messages are:

1. `Add restaurant menu loop`
2. `Add inventory data and view function`
3. `Add item restocking and input validation`

All stages were created during the current work session, without changing commit dates. They represent real development stages, not separate project weeks.
