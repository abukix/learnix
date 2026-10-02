# 02: Variables and Types

Source: boot.dev Learn Python, Chapter 2, Lessons 1 to 14.

## What it is

### Variables

A variable is a name that refers to a value. Assignment uses a single equals sign, with the name on the left and the value on the right:

```python
player_health = 1000
```

Once a name is assigned, using the name gives back its value. Variables let a program store a result, reuse it, and change it over time.

A variable can be reassigned at any point. The new value replaces the old one, and the old value is no longer reachable through that name. This is why they are called variables: their values can vary while the program runs.

### Arithmetic

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `7 + 2` | `9` |
| `-` | Subtraction | `7 - 2` | `5` |
| `*` | Multiplication | `7 * 2` | `14` |
| `/` | Division | `7 / 2` | `3.5` |
| `//` | Floor division | `7 // 2` | `3` |
| `%` | Remainder (modulo) | `7 % 2` | `1` |
| `**` | Exponent | `2 ** 10` | `1024` |

Operations follow the standard mathematical order: exponents first, then multiplication and division, then addition and subtraction. Parentheses override the order, so `(5 + 7 + 9) / 3` adds first and then divides. Negative numbers are written with a leading minus sign, such as `-10`.

One rule to remember: `/` always returns a float, even when the division is exact. `10 / 2` is `5.0`, not `5`. Use `//` when an integer result is needed.

### Basic types

Every value has a type. Python's basic types are:

| Type | Name | Examples | Notes |
|---|---|---|---|
| `str` | String | `"hello"`, `'hello'` | Text. Double quotes are the common convention. |
| `int` | Integer | `5`, `-5`, `0` | Whole numbers, with no size limit. |
| `float` | Floating-point number | `5.2`, `-0.5`, `5.0` | Numbers with a decimal part. |
| `bool` | Boolean | `True`, `False` | Exactly two values. Capitalized in Python. |
| `NoneType` | None | `None` | The absence of a value. |

`type(value)` returns the type of any value, which is useful when debugging.

### None

`None` represents "no value yet" or "no value at all." It is commonly used as a starting value for something that has not been determined, such as a username before the user has entered it.

`None` is its own type. It is not the same as `0`, `False`, an empty string `""`, or the string `"None"`. The correct way to check for it is `value is None`.

### Dynamic typing

Python is dynamically typed. A variable does not have a fixed type. The type belongs to the value, and the same name can be reassigned to a value of a different type:

```python
speed = 5
speed = "five"   # allowed, but avoid it
```

This is allowed but is usually a mistake. If a value changes meaning, give it a new name, such as `speed` and `speed_description`.

In a statically typed language such as Go or TypeScript, each variable has a fixed type that is checked before the program runs. Assigning a string to a number variable is a compile-time error, so the program never starts.

Python is also strongly typed: it does not silently convert between types. `"health: " + 100` raises a `TypeError` instead of guessing what was intended.

### Building strings

There are two common ways to combine values into text:

- **f-strings (preferred):** put `f` before the opening quote and place values inside curly braces. `f"You have {health} health"`. Any expression works inside the braces, and non-string values are converted automatically.
- **Concatenation with `+`:** joins strings together. `"Lane " + "Wagner"` gives `"Lane Wagner"`. Every part must already be a string, so numbers need `str()` first, and spacing has to be added by hand.

f-strings are easier to read and avoid both of those problems.

### Comments

Comments are notes for people and are ignored when the program runs.

- `#` turns the rest of the line into a comment.
- Triple-quoted strings (`"""..."""`) are sometimes used for longer notes. Strictly speaking they are strings, not comments. Python evaluates and discards them. When a triple-quoted string is the first line of a function, class, or module, it becomes a docstring, which documentation tools and `help()` can read.

Good comments explain why the code does something. The code itself should make clear what it does.

### Naming

Variable names cannot contain spaces and cannot start with a digit. Python's style guide, PEP 8, sets the conventions:

| Style | Example | Used in Python for |
|---|---|---|
| snake_case | `num_new_users` | Variables and functions |
| UPPER_SNAKE_CASE | `MAX_HEALTH` | Constants |
| PascalCase | `PlayerCharacter` | Classes |
| camelCase | `numNewUsers` | Not used in Python (common in JavaScript and Java) |

Code still runs with any style. The conventions exist so that code is consistent and other Python developers can read it easily. Descriptive names matter more than short ones: `player_health` is better than `ph`.

### Multiple assignment

Several variables can be assigned on one line:

```python
sword_name, sword_damage, sword_length = "Excalibur", 10, 200
```

The number of names must match the number of values. This is best used for values that belong together. It also enables a clean swap without a temporary variable: `a, b = b, a`.

## Analogy

Continuing the kitchen from Chapter 1: **variables are labels, and values are the ingredients they are stuck to.**

- Assigning `sugar = jar_3` sticks the label "sugar" on a jar. When the recipe says "sugar," the cook looks for that label.
- Reassigning moves the label to a different jar. The old jar is still on the shelf, but nothing points to it anymore.
- Types are kinds of ingredients. Two liquids can be poured together, but pouring flour into a measuring cup of water labeled "milk" does not make milk.
- `None` is a label that has been written but not yet stuck to any jar. It says "this will be something later."
- **Dynamic typing:** in Python's kitchen, any label can go on any jar. The label "sugar" could end up on a jar of salt, and nothing stops you until the dish tastes wrong.
- **Static typing:** in Go's kitchen, each label is printed on a holder that only fits one kind of jar. Putting salt where sugar belongs is rejected before cooking starts.
- **Naming conventions** are the kitchen agreeing to write every label the same way, so anyone who walks in can find things.

## Example

```python
# Assignment and reassignment
player_health = 1000
player_health = player_health - 100
print(player_health)                    # 900

# Arithmetic and division
print((5 + 7 + 9) / 3)                  # 7.0, because / always returns a float
print(7 // 2, 7 % 2, 2 ** 10)           # 3 1 1024

# Basic types
name = "Yarl"                           # str
level = 37                              # int
magic_resistance = 0.5                  # float
account_active = True                   # bool
enemy = None                            # NoneType
print(type(level), type(magic_resistance), type(enemy))
# <class 'int'> <class 'float'> <class 'NoneType'>

# Building strings
print(f"{name} is level {level}")       # Yarl is level 37
print("Level " + str(level))            # Level 37
# print("Level " + level)               # TypeError: can only concatenate str (not "int") to str

# None is not zero, False, or empty
print(enemy is None)                    # True
print(enemy == 0, enemy == False)       # False False

# Multiple assignment and swapping
a, b = 1, 2
a, b = b, a
print(a, b)                             # 2 1
```

## In other languages

| | Python | JavaScript | Go | Bash |
|---|---|---|---|---|
| Create a variable | `x = 5` | `let x = 5` or `const x = 5` | `var x int = 5` or `x := 5` | `x=5` (no spaces around `=`) |
| Typing | Dynamic, strong | Dynamic, weak | Static, strong | Everything is a string |
| `"5" + 1` | `TypeError` | `"51"` | Compile error | `$(( "5" + 1 ))` is `6` |
| `7 / 2` | `3.5` | `3.5` | `3` for integers, `3.5` for floats | `$((7 / 2))` is `3` |
| Insert a value into text | `f"x is {x}"` | `` `x is ${x}` `` | `fmt.Sprintf("x is %d", x)` | `"x is $x"` |
| No value | `None` | `null` and `undefined` | Zero values (`0`, `""`, `false`); `nil` for pointers | Empty string |
| Naming style | `snake_case` | `camelCase` | `camelCase`; `PascalCase` to export | `lower_case` locally, `UPPER_CASE` for environment |
| Comment | `#` | `//` and `/* */` | `//` and `/* */` | `#` |

Two ideas carry over to every language:

1. **Where types are checked.** Static languages check types before running, dynamic languages check them while running. This is the same "how early are mistakes caught" idea from Chapter 1.
2. **Whether types convert silently.** JavaScript turns `"5" + 1` into `"51"`. Python refuses. Knowing which behavior a language has prevents a whole class of bugs.

## Interview framing

1. What does it mean that Python is dynamically typed? Is it strongly or weakly typed?
2. What are Python's basic data types?
3. What is `None`, and how is it different from `0`, `False`, or an empty string?
4. Why does `10 / 2` return `5.0`? What is the difference between `/`, `//`, and `%`?
5. What is the difference between f-strings and string concatenation?
6. What are Python's naming conventions, and why do they matter?
7. How does `a, b = b, a` work?

## My answer

**1. Dynamic and strong typing**

"Dynamically typed means a variable does not have a fixed type. The type belongs to the value, and it is checked while the program runs rather than before. So the same name can hold an integer and later a string, although doing that on purpose is usually a bad idea. Python is also strongly typed, which means it does not silently convert between types. Adding a string and an integer raises a `TypeError`. JavaScript, by comparison, is dynamic but weak, so `"5" + 1` becomes `"51"`. Go is static and strong, so the same mistake fails at compile time."

**2. Basic data types**

"The basic types are `str` for text, `int` for whole numbers, `float` for decimal numbers, `bool` for `True` and `False`, and `None` for the absence of a value. Python integers have no fixed size limit, which is different from most languages. Floats follow the standard binary floating-point format, so they can have small rounding errors."

**3. None**

"`None` is Python's way of saying there is no value. It is used for things that have not been set yet, optional values, and functions that do not return anything. It is its own type, `NoneType`, and it is not equal to `0`, `False`, or an empty string, even though all of them count as false in an `if` statement. The correct check is `is None` rather than `== None`, because there is only one `None` object and `is` checks identity directly."

**4. Division**

"`/` is true division and always returns a float, even when the result is a whole number, so `10 / 2` is `5.0`. `//` is floor division, which rounds down to the nearest whole number, and `%` gives the remainder. One detail is that floor division rounds toward negative infinity, so `-7 // 2` is `-4`, not `-3`."

**5. f-strings versus concatenation**

"f-strings let me write the text once and place values inside curly braces, and Python converts each value to a string automatically. Concatenation with `+` requires every part to already be a string, so numbers need `str()`, and I have to manage spaces by hand. f-strings are more readable and are the standard choice in modern Python. They also support formatting, such as `{price:.2f}` for two decimal places."

**6. Naming conventions**

"Python follows PEP 8: `snake_case` for variables and functions, `UPPER_SNAKE_CASE` for constants, and `PascalCase` for classes. The interpreter does not enforce any of it, but consistent naming makes code easier to read and review, and linters such as `ruff` flag violations. More important than the style is using descriptive names, because code is read far more often than it is written."

**7. Swapping with `a, b = b, a`**

"The right-hand side is evaluated first and packed into a tuple, `(b, a)`, using the current values. Then the tuple is unpacked into the names on the left. Because the right side is fully evaluated before anything is assigned, the swap works without a temporary variable. The same unpacking works for any number of values, as long as the counts match on both sides."

**Points to recall**

- A variable is a name that refers to a value. Reassignment points the name at a new value.
- Python is dynamically typed (types are checked at runtime) and strongly typed (no silent conversion).
- The basic types are `str`, `int`, `float`, `bool`, and `None`.
- `None` is not `0`, `False`, or `""`. Check it with `is None`.
- `/` always returns a float. `//` floors, `%` gives the remainder.
- Prefer f-strings over `+` concatenation.
- PEP 8: `snake_case` for variables, `UPPER_SNAKE_CASE` for constants, `PascalCase` for classes.
- Multiple assignment evaluates the right side first, which is why `a, b = b, a` swaps.

## Follow-up gotchas

**Why does `0.1 + 0.2 == 0.3` return `False`?**
Floats are stored in binary, and most decimal fractions cannot be represented exactly in binary. `0.1 + 0.2` is actually `0.30000000000000004`. Compare floats with a tolerance, such as `math.isclose()`, and use the `decimal` module for money.

**Is a triple-quoted string a comment?**
Not technically. It is a string expression that Python evaluates and discards. That is why it can become a docstring when placed at the start of a function or class. For ordinary comments, `#` is the correct tool.

**What does `True + True` return?**
`2`. In Python, `bool` is a subclass of `int`, so `True` behaves like `1` and `False` like `0` in arithmetic. This is occasionally useful, such as counting matches with `sum()`, but it can also hide bugs.

**Does assigning one variable to another copy the value?**
No. `b = a` makes both names refer to the same object. For immutable types such as numbers and strings this makes no practical difference, because they cannot be changed in place. For mutable types such as lists, changing the object through one name is visible through the other. This is covered in more depth with lists.

**What happens if the counts do not match in multiple assignment?**
Python raises a `ValueError`, such as `too many values to unpack (expected 2, got 3)`.

**Why is `x = 5` fine in Python but `x = 5` an error in Bash?**
In Bash, spaces separate a command from its arguments, so `x = 5` is read as running a command named `x` with the arguments `=` and `5`. Bash assignments must be written without spaces: `x=5`.
