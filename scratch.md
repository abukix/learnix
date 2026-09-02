# Scratch Notes — CH1-CH6

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

## CH6: Computing

### What is Computing

Computing is the manipulation of data through arithmetic and logical operations. Under the hood, a computer only ever stores and moves data as binary(`0`s and `1`s), so every number, comparison, and boolean check a program runs eventually breaks down into bits being combined by circuits.

### What is Integer and Float

Integer is a whole number, positive or negative, with no decimal point(`3`, `-3`). Float is a number that carries a decimal point(`3.0`, `-3.5`). Dividing two integers with `/` always produces a float, even when the result is a whole number(`4 / 2` is `2.0`, not `2`).

### What is Floor Division and Exponents

Floor division(`//`) divides then rounds the result down to the nearest integer, not toward zero, so `-7 // 3` is `-3`, not `-2`. Exponents use `**`, Python's built-in stand-in for the math `^` notation(`3**2` is `9`).

### What is Changing in Place

Changing a variable based on its own current value(`score = score + 1`) works because the right-hand side is evaluated first using the old value, then the result is stored back into the same name. The `+=`, `-=`, `*=`, `/=` operators are shorthand for this exact pattern, e.g. `score += 1` instead of `score = score + 1`.

### What is Scientific Notation

Scientific notation writes very large or very small floats using `e`/`E` followed by an exponent, where the exponent tells how many places to shift the decimal point(right if positive, left if negative): `16e3` is `16000.0`, `7.1e-2` is `0.071`. Underscores can also be dropped into large number literals as a readability separator with no effect on the value(`16_000` is `16000`).

### What is Logical Operators (and, or, not)

`and` returns `True` only if both sides are `True`. `or` returns `True` if at least one side is `True`. `not` flips a boolean to its opposite. Nested expressions in parentheses evaluate innermost-first, same as in math.

### What is Binary Numbers and Bitwise Operators

Binary is base-2, using only `0` and `1`, where each digit's place value doubles moving left(ones, twos, fours, eights). Python writes a binary literal with a `0b` prefix(`0b0101` is `5`). Bitwise `&` and `|` apply `and`/`or` logic column-by-column across the bits of two numbers(`0b0101 & 0b0111` is `5`, `0b0101 | 0b0010` is `0b0111`), rather than treating the whole number as one boolean.
