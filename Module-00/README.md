# Python Module 00

An introductory Python project focused on learning the language's basic syntax through a series of small garden-themed exercises. The module covers functions, user input, variables, arithmetic operations, conditionals, loops, recursion, string methods, and type hints.

## Exercises

### Exercise 0 — Hello, Garden!
Create a simple function that prints a welcome message to the garden community. This exercise introduces function definition, indentation, and basic output with `print()`.

### Exercise 1 — Garden Name
Ask the user for the name of a garden and display it together with its current status. This exercise introduces user input, variables, and formatted output.

### Exercise 2 — Plot Area
Read the length and width of a garden plot, calculate its area, and display the result. This exercise practices integer conversion and basic arithmetic operations.

### Exercise 3 — Harvest Total
Request the harvest amount for three different days, add the values, and print the total harvest. This exercise reinforces input handling, variables, and addition.

### Exercise 4 — Plant Age
Ask for a plant's age in days and determine whether it is ready to harvest. A plant is ready only when it is strictly more than 60 days old. This exercise introduces conditional statements with `if` and `else`.

### Exercise 5 — Watering Reminder
Ask how many days have passed since the plants were last watered. Display a watering reminder when more than two days have passed; otherwise, report that the plants are fine. This exercise provides further practice with conditional logic.

### Exercise 6 — Harvest Countdown
Implement the same harvest countdown in two different ways:

- **Iterative version:** use a `for` loop and `range()` to print each day until harvest.
- **Recursive version:** use a function that calls itself until the countdown is complete.

Both versions finish by printing `Harvest time!`.

### Exercise 7 — Seed Inventory
Create a typed function that displays seed inventory information according to the supplied unit: packets, grams, or planting area. This exercise introduces function parameters, type hints, `elif`, f-strings, and the `capitalize()` string method.

## Project Structure

```text
.
├── ex0/ft_hello_garden.py
├── ex1/ft_garden_name.py
├── ex2/ft_plot_area.py
├── ex3/ft_harvest_total.py
├── ex4/ft_plant_age.py
├── ex5/ft_water_reminder.py
├── ex6/ft_count_harvest_iterative.py
├── ex6/ft_count_harvest_recursive.py
└── ex7/ft_seed_inventory.py
```

## Concepts Practised

- Python functions and indentation
- Variables and dynamic typing
- `input()`, `print()`, and integer conversion
- Arithmetic operations
- Conditional statements
- `for` loops and `range()`
- Recursion and base cases
- String methods and f-strings
- Type hints and static type checking

## Validation

From the project root, the code can be checked with:

```bash
python3 -m flake8 .
python3 -m mypy .
```
