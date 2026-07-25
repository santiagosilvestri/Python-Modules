# Python Module 01

This module introduces the fundamentals of **Object-Oriented Programming in Python** through a digital garden management system. The exercises progress from a basic Python program to a class hierarchy with inheritance, encapsulation, special methods, and internal statistics.

## Project Structure

```text
.
├── ex0/
│   └── ft_garden_intro.py
├── ex1/
│   └── ft_garden_data.py
├── ex2/
│   └── ft_plant_growth.py
├── ex3/
│   └── ft_plant_factory.py
├── ex4/
│   └── ft_garden_security.py
├── ex5/
│   └── ft_plant_types.py
└── ex6/
    └── ft_garden_analytics.py
```

## Exercises

### Exercise 0 — Planting Your First Seed

Creates a basic Python program that stores and displays plant information using variables, type hints, `print()`, and the `if __name__ == "__main__":` entry point.

**Main concepts:** variables, basic types, f-strings, program structure, and the shebang.

### Exercise 1 — Garden Data Organizer

Defines a `Plant` class and creates several plant instances with a name, height, and age. Each plant provides a `show()` method to display its information.

**Main concepts:** classes, objects, attributes, methods, and `self`.

### Exercise 2 — Plant Growth Simulator

Extends the `Plant` class with methods that increase its height and age. The program simulates one week of growth and calculates the total height increase.

**Main concepts:** object state, instance methods, loops, `range()`, `round()`, and floating-point values.

### Exercise 3 — Plant Factory

Introduces the `__init__()` constructor so plants can be created directly with their initial values. Multiple plant objects are stored in a list and displayed in an organized way.

**Main concepts:** constructors, object initialization, lists of objects, and iteration.

### Exercise 4 — Garden Security System

Protects plant data using attributes that follow the protected naming convention. Getters provide controlled access, while setters validate changes and prevent negative height or age values.

**Main concepts:** encapsulation, protected attributes, getters, setters, validation, and boolean return values.

### Exercise 5 — Specialized Plant Types

Creates specialized plant classes derived from `Plant`: `Flower`, `Tree`, and `Vegetable`. Each subclass reuses common behavior and adds its own attributes and methods.

**Main concepts:** inheritance, `super()`, method overriding, specialization, code reuse, and polymorphism.

### Exercise 6 — Garden Analytics

Adds an internal statistics system that records calls to plant methods. It also introduces static methods, class methods, nested classes, tree-specific statistics, and a `Seed` class derived from `Flower`.

**Main concepts:** `@staticmethod`, `@classmethod`, nested classes, composition, multilevel inheritance, encapsulation, and polymorphism.

## Running the Exercises

Each exercise can be executed independently:

```bash
python3 ex0/ft_garden_intro.py
python3 ex1/ft_garden_data.py
python3 ex2/ft_plant_growth.py
python3 ex3/ft_plant_factory.py
python3 ex4/ft_garden_security.py
python3 ex5/ft_plant_types.py
python3 ex6/ft_garden_analytics.py
```

The files can also be executed directly because they include a shebang:

```bash
chmod +x ex0/ft_garden_intro.py
./ex0/ft_garden_intro.py
```

## Code Checks

```bash
python3 -m flake8 .
python3 -m mypy .
```

## What This Module Teaches

By completing this module, you practice the main foundations of Object-Oriented Programming in Python:

- Creating classes and objects.
- Using attributes and instance methods.
- Initializing objects with `__init__()`.
- Protecting and validating internal state.
- Reusing code through inheritance.
- Overriding methods and applying polymorphism.
- Understanding instance, static, and class methods.
- Organizing responsibilities with composition and nested classes.
