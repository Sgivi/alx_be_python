This readme contains Python tasks from the ALX Backend Python program:
an arithmetic operations function, a simple shopping list manager, and displaying current datetime with future date.

## 1. Arithmetic Operations (`arithmetic_operations.py`)

Implements `perform_operation(num1, num2, operation)` which supports:

* `add`
* `subtract`
* `multiply`
* `divide` (handles division by zero)

**Error messages:**

* `"Error: Division by zero"`
* `"Error: Invalid operation"`

Test using the provided `main.py`.

## 2. Shopping List Manager (`shopping_list_manager.py`)

A menu-driven CLI program that lets the user:

* Add an item
* Remove an item
* View the current list
* Exit the program

Uses a Python list to store and update shopping items.

## Explore Datetime

# What the script does

1. Display Current Date & Time
    - Uses datetime.now()to get the current date and time
    - Formats it as: YYYY-MM-DD HH:MM:SS
    - Prints the results

2. Calculate a Future Date
    - Prompts the user to enter a number of days
    - Uses timedelta(days=<value>) to add those days to today's date
    - Prints the future date

# Concepts covered
- **datetime module**
- **datetime.now()**
- **.strftime()** formatting
- **timedelta** for date calculations
- User input and function structurebn\