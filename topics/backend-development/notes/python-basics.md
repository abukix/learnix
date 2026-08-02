---
topic: Backend Development
source: boot.dev
date: 2026-08-02
status: seed   # seed | growing | evergreen
---

# CH1: Introduction

## 1.0 Python for beginners

**What is Python?**

Python is a popular, high-level, general-purpose programming language created by Guido van Rossum in 1991, known for its simple, English-like syntax and readability. It is widely used for artificial intelligence, web development, and task automation.

**Common uses**

- AI & Machine Learning: Building smart tools, deep learning models, and data agents.
- Automation: Writing quick scripts to do boring, repetitive computer tasks.
- Web Development: Powering the hidden back-end servers of websites using tools like Django and Flask. (Not popular for frontend use.)

**Key features**

- Easy to learn: Uses clear spacing and simple words instead of complex curly brackets.
- Interpreted: Runs code line by line, making it fast to test and find mistakes.
- Versatile: Handles small scripts as well as massive data systems.

## 1.1 What is code?

It's just a series of instructions for a computer to follow one after another. Programs can have a lot of instructions.

## 1.2 Syntax errors

A syntax error is a mistake in code that breaks the grammatical rules of a programming language, such as missing punctuation, misspelled words, or mismatched brackets. Because the computer cannot read or understand the broken structure, it stops the program from running at all.

**Common causes**

- Missing symbols: Leaving out a closing parenthesis `)`, bracket `]`, or semicolon `;`.
- Typo mistakes: Misspelling a command word or a variable name.
- Wrong quotes: Forgetting to close a text string with quotation marks `"`.
- Bad spacing: Using the wrong line indentation in languages like Python.

# CH2: Variables and Types

## 2.0 Variables

Variables are how we store data as our program runs. Up 'til now we've been printing data by passing it straight into `print()`. Now we're going to save the data in variables so we can reuse it and change it before printing it.

We have the freedom to choose any name for our variables, but they should be descriptive and consist of a single "token" — continuous text with underscores separating the words.

**Variables vary**

Variables are called "variables" because they can hold any value, and that value can change (it varies).

## 2.1 Mathematical operators

Common mathematical operators using Python syntax:

- Addition
- Subtraction
- Multiplication
- Division
- Order of operations

It can also use negative numbers directly.

## 2.2 Comments

Comments don't do... anything. They are ignored by the Python interpreter. That said, they're good for what the name implies: adding comments to your code in plain English (or whatever language you speak).

**Single-line comment** — a single `#` makes the rest of the line a comment:

```python
# speed describes how fast the player
# moves in meters per second
speed = 2
```

**Multi-line comment** — triple quotes can start and end a multi-line comment:

```python
"""
the code found below
will print 'Hello, World!' to the console
"""

print("Hello, World!")
```

## 2.3 Variable names

Variable names must not have spaces. They're continuous strings of characters.

The creator of the Python language himself, Guido van Rossum, implores us to use snake_case for variable names. What is snake case? It's just a style for writing variable names. Here are some examples of different casing styles:

| Name | Description | Code | Language(s) that recommend it |
| --- | --- | --- | --- |
| Snake Case | All words are lowercase and separated by underscores | `num_new_users` | Python, Ruby, Rust |
| Camel Case | Capitalize the first letter of each word except the first one | `numNewUsers` | JavaScript, Java |
| Pascal Case | Capitalize the first letter of each word | `NumNewUsers` | C#, C++ |
| No Casing | All lowercase with no separation | `numnewusers` | ...just don't do this |

To be clear, your Python code will still work with Camel Case or Pascal Case, but can we please just have nice things? We just want some consistency in our craft.

## 2.4 Multi-variable declaration

We can save space when creating many new variables by declaring them on the same line:

```python
sword_name, sword_damage, sword_length = "Excalibur", 10, 200
```

Which is the same as:

```python
sword_name = "Excalibur"
sword_damage = 10
sword_length = 200
```

Any number of variables can be declared on the same line, and variables declared on the same line should be related to one another in some way so that the code remains easy to understand.

We call code that's easy to understand "clean code."

## 2.5 Basic variable types

Python has several basic data types.

**Strings**

In programming, snippets of text are called "strings." They're lists of characters strung together. We create strings by wrapping the text in single quotes or double quotes. That said, double quotes are preferred.

```python
name_with_single_quotes = 'boot.dev'  # not so good
name_with_double_quotes = "boot.dev"  # so good
```

**Numbers**

Numbers are not surrounded by quotes when they're declared.

An integer (or "int") is a number without a decimal part:

```python
x = 5   # positive integer
y = -5  # negative integer
```

A float is a number with a decimal part:

```python
x = 5.2
y = -5.2
```

**Booleans**

A "Boolean" (or "bool") is a type that can only have one of two values: `True` or `False`. As you may have heard, computers really only use 1's and 0's. These 1's and 0's are just True/False boolean values.

```python
is_tall = True
is_short = False
```

## 2.6 Data types

Python has built-in data types categorized into text, numeric, sequence, mapping, set, and boolean types. Because Python is dynamically typed, you do not need to declare a variable's type explicitly before using it.

You can check any variable's data type by passing it into the built-in `type()` function.

### Quick overview

| Category | Type name | Mutable? | Example syntax |
| --- | --- | --- | --- |
| Text | `str` | No | `"Hello World"` |
| Numeric | `int`, `float`, `complex` | No | `42`, `3.14`, `2+3j` |
| Sequence | `list`, `tuple`, `range` | Varies — `list` yes, `tuple`/`range` no | `[1, 2, 3]`, `(1, 2, 3)`, `range(5)` |
| Mapping | `dict` | Yes | `{"key": "value"}` |
| Set | `set`, `frozenset` | Varies — `set` yes, `frozenset` no | `{1, 2, 3}`, `frozenset({1, 2})` |
| Boolean | `bool` | No | `True`, `False` |
| None | `NoneType` | No | `None` |

### Core Python data types

**1. Text type**

- `str`: Represents text or a sequence of characters. Strings must be enclosed in single, double, or triple quotes.

**2. Numeric types**

- `int`: Holds whole numbers of unlimited length, both positive and negative.
- `float`: Holds real numbers containing one or more decimals.
- `complex`: Holds complex numbers written with a `j` as the imaginary part (e.g., `3+5j`).

**3. Sequence types**

- `list`: An ordered, changeable (mutable) collection that allows duplicate items. Defined using square brackets `[]`.
- `tuple`: An ordered, unchangeable (immutable) collection that allows duplicate items. Defined using parentheses `()`.
- `range`: Represents an immutable sequence of numbers, commonly used for looping a specific number of times in `for` loops.

**4. Mapping type**

- `dict`: An ordered (as of Python 3.7) and changeable collection of key-value pairs. No duplicate keys are allowed. Defined using curly braces with colons, e.g. `{"name": "Alice"}`.

**5. Set types**

- `set`: An unordered, changeable, and unindexed collection of unique items. Defined using curly braces, e.g. `{1, 2, 3}`.
- `frozenset`: An immutable version of a set. Its elements cannot be changed after creation.

**6. Boolean type**

- `bool`: Represents one of two truth values: `True` or `False`. Note that the "T" and "F" must always be capitalized.

**7. None type**

- `NoneType`: Represented by the `None` keyword. It signifies the absence of a value or a null value.

### Mutability vs. immutability

Understanding mutability is crucial for memory management and avoiding bugs in Python:

- **Mutable** types can be changed after they are created (e.g., `list`, `dict`, `set`).
- **Immutable** types cannot be changed once created (e.g., `int`, `float`, `str`, `tuple`, `frozenset`). If you alter an immutable variable, Python actually creates a brand-new object in memory.

## 2.7 Dynamic typing

Python is dynamically typed, which means a variable can store any type, and that type can change.

For example, if I make a number variable, I can later change that variable to a string:

```python
speed = 5
speed = "five"
```

**But like, maybe don't**

In almost all circumstances, it's a bad idea to change the type of a variable. The "proper" thing to do is to just create a new one. For example:

```python
speed = 5
speed_description = "five"
```

**What is non-dynamic typing?**

Languages that aren't dynamically typed are statically typed, such as Go and TypeScript (one of which you'll learn in a later course depending on your chosen track). In a statically typed language, if you try to assign a value to a variable of the wrong type, you'll get a compile-time error and the program won't run.

If Python were statically typed, the first example from before wouldn't allow the second line, `speed = "five"`. The computer would give an error along the lines of "you can't assign a string value (`"five"`) to a number variable (`speed`)."

## 2.8 String formatting (f-strings)

An f-string (formatted string literal) is the most modern, efficient, and readable way to format strings in Python (introduced in Python 3.6). To create one, simply prefix the string with the letter `f` or `F` and place variables or expressions inside curly braces `{}`.

### Basic usage

Instead of using messy concatenation or older `.format()` methods, you can insert variables directly:

```python
name = "Alice"
age = 30

# Basic f-string
message = f"Hello, {name}. You are {age} years old."
print(message)
# Output: Hello, Alice. You are 30 years old.
```

### Key capabilities and tricks

**1. Inline expressions and math**

You can run calculations, call methods, or evaluate logic directly inside the braces.

```python
print(f"Next year you will be {age + 1}.")         # Output: Next year you will be 31.
print(f"Uppercase name: {name.upper()}")            # Output: Uppercase name: ALICE
print(f"Is adult? {'Yes' if age >= 18 else 'No'}")   # Output: Is adult? Yes
```

**2. Number formatting**

Use a colon `:` inside the braces followed by a format specifier to control decimals, commas, or alignments.

```python
price = 1250.456

# Round to 2 decimal places
print(f"Price: ${price:.2f}")       # Output: Price: $1250.46

# Add thousands separators
print(f"Price: ${price:,}")         # Output: Price: $1,250.456

# Combine both (comma and 2 decimals)
print(f"Price: ${price:,.2f}")      # Output: Price: $1,250.46
```

**3. Easy debugging (Python 3.8+)**

Adding an equal sign `=` after the variable prints both the variable name and its value automatically. This is perfect for quick `print()` debugging.

```python
x = 10
y = 25
print(f"{x=}, {y=}, {x+y=}")
# Output: x=10, y=25, x+y=35
```

**4. Formatting dates**

You can easily structure `datetime` objects without calling `.strftime()` explicitly.

```python
import datetime
today = datetime.datetime.now()

print(f"Today is {today:%B %d, %Y}")
# Output: Today is August 02, 2026
```

**5. Text alignment and padding**

Use `<`, `>`, or `^` to align text and set a specific character width.

```python
text = "test"
print(f"{text:>10}")  # Right-align (width 10):  '      test'
print(f"{text:<10}")  # Left-align (width 10):   'test      '
print(f"{text:^10}")  # Center-align (width 10):  '   test   '
print(f"{text:*^10}") # Center-align with '*' padding: '***test***'
```

### Important rules to remember

**Quote scoping** — if your f-string uses double quotes on the outside, use single quotes on the inside (like for dictionary keys), and vice versa.

```python
user = {"name": "Bob"}
print(f"User is {user['name']}")  # Correct
```

**Escaping braces** — if you need to print literal `{}` brackets in your text, double them up.

```python
print(f"Use {{x}} to print brackets.")  # Output: Use {x} to print brackets.
```

**Combining prefixes** — you can combine f-strings with raw strings using `fr"..."` or `rf"..."` if you need to use backslashes (like in file paths or regexes) alongside dynamic variables.

## 2.9 Math with strings

When working with strings, the `+` operator performs a "concatenation," which is a fancy word that means "joining two strings." Generally speaking, it's better to use string interpolation with f-strings over `+` concatenation.

```python
first_name = "Lane "
last_name = "Wagner"
full_name = first_name + last_name
print(full_name)
# prints "Lane Wagner"
```

`full_name` now holds the value `"Lane Wagner"`.

Notice the extra space at the end of `"Lane "` in the `first_name` variable. That extra space is there to separate the words in the final result: `"Lane Wagner"`.

## 2.10 NoneType variables

Not all variables have a value. We can make an "empty" variable by setting it to `None`. `None` is a special value in Python that represents the absence of a value. It is not the same as zero, `False`, or an empty string.

```python
my_mental_acuity = None
```

The value of `my_mental_acuity` in this case is `None` until we use the assignment operator, `=`, to give it a value.

**None is not a string**

`NoneType` is not the same as a string with a value of `"None"`:

```python
my_none = None    # this is a None-type
my_none = "None"  # this is a string with the value "None"
```


