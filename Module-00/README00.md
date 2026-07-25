# Python Module 00

This module introduces the fundamentals of **Python programming** through a collection of garden-themed functions. The exercises progress from basic output and user input to arithmetic operations, conditional logic, loops, recursion, string methods, and type annotations.

## Project Structure

```text
.
├── ex0/
│   └── ft_hello_garden.py
├── ex1/
│   └── ft_garden_name.py
├── ex2/
│   └── ft_plot_area.py
├── ex3/
│   └── ft_harvest_total.py
├── ex4/
│   └── ft_plant_age.py
├── ex5/
│   └── ft_water_reminder.py
├── ex6/
│   ├── ft_count_harvest_iterative.py
│   └── ft_count_harvest_recursive.py
└── ex7/
    └── ft_seed_inventory.py
```

## Exercises

### Exercise 0 — Hello Garden

Defines a simple function that displays a welcome message for the garden community.

**Main concepts:** function definition, `def`, `print()`, indentation, and basic program structure.

### Exercise 1 — Garden Name

Asks the user for a garden name and displays it together with a fixed status message.

**Main concepts:** `input()`, variables, strings, `print()`, and user interaction.

### Exercise 2 — Garden Plot Area

Requests the length and width of a rectangular garden plot, converts both inputs to integers, and displays the calculated area.

**Main concepts:** type conversion with `int()`, arithmetic operations, variables, input, and output.

### Exercise 3 — Harvest Total

Requests harvest quantities from three different days and calculates their total.

**Main concepts:** multiple inputs, integer conversion, variable assignment, addition, and accumulation of values.

### Exercise 4 — Plant Age Check

Checks whether a plant is ready to harvest based on its age. A plant is considered ready only when it is strictly more than 60 days old.

**Main concepts:** `if`, `else`, comparison operators, boolean conditions, and decision-making.

### Exercise 5 — Water Reminder

Checks how many days have passed since the plants were last watered and displays the appropriate reminder.

**Main concepts:** conditional logic, comparison operators, input conversion, and alternative execution paths.

### Exercise 6 — Count to Harvest

Implements the same harvest countdown in two different ways: an iterative version using a loop and a recursive version using a helper function.

**Main concepts:** `for`, `range()`, iteration, recursion, nested helper functions, recursive calls, and the base case.

### Exercise 7 — Seed Inventory with Type Annotations

Defines a function that receives a seed type, quantity, and unit as parameters. It formats the seed name, supports different inventory units, and uses type annotations.

**Main concepts:** function parameters, type hints, `-> None`, `if`/`elif`/`else`, f-strings, string methods, and `capitalize()`.

## Requirements

- Python 3.10 or later
- `flake8` for style checking
- `mypy` for static type checking

No external Python libraries are required to run the exercises.

## Testing the Exercises

The subject requires each file to contain only the requested function, without function calls or a main program outside it. The functions can be tested by importing and calling them from the terminal.

Basic example:

```bash
python3 -c "from ex0.ft_hello_garden import ft_hello_garden; ft_hello_garden()"
```

Example with user input:

```bash
python3 -c "from ex2.ft_plot_area import ft_plot_area; ft_plot_area()"
```

Example with function arguments:

```bash
python3 -c "from ex7.ft_seed_inventory import ft_seed_inventory; ft_seed_inventory('tomato', 15, 'packets')"
```

## Code Checks

```bash
python3 -m flake8 .
python3 -m mypy .
```

`flake8` checks code style and formatting. `mypy` checks type annotations, which are specifically required in Exercise 7.

## What This Module Teaches

By completing this module, you practice the fundamental building blocks of Python:

- Defining functions and organizing blocks through indentation.
- Working with variables and basic data types.
- Receiving and converting user input.
- Performing arithmetic operations.
- Making decisions with conditional statements.
- Repeating actions with loops.
- Understanding recursion and base cases.
- Passing arguments through function parameters.
- Formatting strings with f-strings and string methods.
- Documenting and checking types with type hints and `mypy`.
