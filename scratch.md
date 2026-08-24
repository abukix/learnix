# Scratch Notes — CH1-CH5

## CH1: Introduction

### What is Python

Python is a high-level, interpreted, dynamically-type programming language. It is created by Guido van Rossum and it's first release in 1991. It's known for its readable, English-like syntax and widely used for backend web development, AI/ML, and automations.

### What is Code and Syntax

Code is a set of instructions that the computer use to execute in order. Syntax is an error that violates the language's grammar and stops the program from running at all before it could reach any bugs inside.

## CH2: Variables and Types

### What is Variable

Variable is a named reference to a value which is created the moment to assign something to it and it can be re-assigned to a new value or type later.

- Python naming convention uses snake_case style, it's a one continuous token with words that is separated by underscore. Other naming conventions style such as PascalCase and camelCase still works with Python but not recommended, using it will read the program as not idiomatic.
- Python built-in types split into text, numeric, sequence, mapping, set, boolean, and None, each with its own rules for order, duplicates, and mutability.
- Python is dynamically-type, so variable's type is just whatever it currently holds and can change on reassignment. Unlike statically typed languages, which lock a variable's type at compile time.
  - Compile time is when a program's human-readable source code is translated into machine-readable binary or bytecode.
  - Run time is when that translated program is actively loaded into memory and executed by a computer's CPU.

### What is f-string

f-string(or formatted string) embeds variables and expressions directly into a string using leading f and {} placeholders. This is the modern, preferred way to format strings in Python.

### What is Mutability and Immutability

Mutable objects(list, dict, set) can be changed in place after creation. Immutable objects(int, float, str, tuple, frozenset, bool) cannot and any change actually creates a brand-new object.

### What is None type

None is Python's singleton value for no value at all. It's different from 0, False, or an empty string.

## CH3: Functions

### What is Functions

A function is a reusable, named block of code defined with def that takes inputs and can hand a value back to its caller with return.

- **Parameters and Arguments**: Parameters are the names in a function's definition. Arguments are the actual values supplied when it's called.
- **print vs. return**: print displays a value to the console and gives back None. return hands a value to the caller and prints nothing by itself.
- **Default parameter values**: A parameter can be declare a fallback value with equal(=) sign in the function signature, making it optional for the caller to supply.
- **Multiple return values**: A function can return several comma-separated values at once. Python packs them into a tuple that the caller unpacks into separate variables.
- **None return**: A function with no explicit return statement(or a bare return)   automatically returns None.

## CH4: Scope

### What is Scope

Scope is the region of code where a given variable/function name is visible and usable. There are two main levels, local which is created inside a function, alive only for that call and global which is created at the module/top level, visible everywhere including inside functions.

## CH5: Testing and Debugging

### What is Console-output and unit-test

Console-output checks compare printed text exactly. Unit tests is a separate test file calls the functions directly and checks their return values, ignoring anything printed.

### What is Debugging

Debugging means writing a small piece of code, printing to verify it does what you expect, and repeating in small steps. Never writing a large block blind an debugging it all at once.
