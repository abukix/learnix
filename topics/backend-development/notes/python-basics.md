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

# CH3: Functions

## 3.0 Functions

Functions allow us to reuse and organize code. For example, say we have some code that calculates the area of a circle:

```python
radius = 5
area = 3.14 * radius * radius
```

That works! The problem is when we want to calculate the area of other circles, each with its own radius. We could just copy the code and change the variable names like this:

```python
radius = 5
area1 = 3.14 * radius * radius

radius2 = 7
area2 = 3.14 * radius2 * radius2
```

But we want to reuse our code! Why would we want to redo our work? What if we wanted to calculate the area of thousands of circles? That's where functions help.

Instead, we can define a new function called `area_of_circle` using the `def` keyword.

```python
def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result
```

Let's break this `area_of_circle` function down:

- It takes one input (aka "parameter" or "argument") called `r`.
- After the `:`, the indented lines form the function body — this is the code block that will run each time we use (aka "call") the function.
- It returns a single value (the output of the function). In this case, it's the value stored in the `result` variable.

To "call" this function (fancy programmer speak for "use this function") we can pass in any number as the argument (in this case, `5`) for the parameter `r`, and capture the output into a new variable:

```python
area = area_of_circle(5)
print(area)
# 78.5
```

- `5` goes in as the input `r`.
- The body of the function runs, which stores `78.5` in the `result` variable within the function body.
- The function returns the `result` variable, which means the `area_of_circle(5)` expression evaluates to `78.5`.
- `78.5` is stored in the `area` variable and then printed.

Because we've already defined the function, now we can use it as many times as we want with different inputs!

## 3.1 Multiple parameters

Functions can have multiple parameters ("parameter" being a fancy word for "input"). For example, this `subtract` function accepts 2 parameters: `a` and `b`.

```python
def subtract(a, b):
    result = a - b
    return result
```

It's the argument's position that determines which parameter receives it (at least, for now). The first argument goes to the first parameter, the second to the second, and so on. In this example, the `subtract` function is called with `a = 5` and `b = 3`:

```python
result = subtract(5, 3)
print(result)
# 2
```

Here's an example with four parameters:

```python
def create_introduction(name, age, height, weight):
    first_part = "Your name is " + name + " and you are " + age + " years old."
    second_part = (
        "You are " + height + " meters tall and weigh " + weight + " kilograms."
    )
    full_intro = first_part + " " + second_part
    return full_intro
```

It can be called like this:

```python
my_name = "John"
my_age = "30"

intro = create_introduction(my_name, my_age, "1.8", "80")
print(intro)
# Your name is John and you are 30 years old. You are 1.8 meters tall and weigh 80 kilograms.
```

## 3.2 Printing vs. returning

Some new developers get hung up on the difference between `print()` and `return`.

It can be particularly confusing when a test suite simply prints the output of your functions to the console. It makes it seem like `print()` and `return` are interchangeable, but they are not!

**`print()`** is a function that:

- Prints a value to the console.
- Does not return a value.

```python
def print_alchemy():
    print("equivalent exchange")


printed_alchemy = print_alchemy()
# equivalent exchange

print(printed_alchemy)
# None
```

**`return`** is a keyword that:

- Ends the current function's execution.
- Provides a value (or values) back to the caller of the function.
- Does not print anything to the console (unless the return value is later `print()`ed).

```python
def return_transmutation():
    return "nothing is lost"


returned_transmutation = return_transmutation()

print(returned_transmutation)
# nothing is lost
```

**Printing to debug your code**

Printing values and running your code is a great way to debug your code. You can see what values are stored in various variables, find your mistakes, and fix them. Add print statements and run your code as you go! It's a great habit to get into to make sure that each line you write is doing what you expect it to do.

In the real world it's rare to leave `print()` statements in your code when you're done debugging. Similarly, you need to remember to remove any `print()` statements from your code before submitting your work here on Boot.dev because it will interfere with the tests!

## 3.3 Where to declare functions

You've probably noticed that a variable needs to be declared before it's used. For example, the following doesn't work:

```python
print(my_name)
my_name = "Lane Wagner"
# NameError: 'my_name' is not defined
```

It needs to be:

```python
my_name = "Lane Wagner"
print(my_name)
# Lane Wagner
```

Code executes in order from top to bottom, so a variable needs to be created before it can be used. That means that if you define a function, you can't call that function until after it has been defined.

## 3.4 Order of functions

All functions must be defined before they're used.

You might think this would make structuring Python code hard because the order of the functions needs to be just right. As it turns out, there's a simple trick that makes it super easy.

Most Python developers solve this problem by defining all the functions in their program first, then they call an "entry point" function at the end of the file. That way all of the functions have been read by the Python interpreter before the first one is called.

Conventionally this "entry point" function is usually called `main` to keep things simple and consistent.

```python
def main():
    health = 10
    armor = 5
    add_armor(health, armor)


def add_armor(h, a):
    new_health = h + a
    print_health(new_health)


def print_health(new_health):
    print(f"The player now has {new_health} health")


# call entrypoint at the end
main()
```

## 3.5 None return

When no return value is specified in a function, it will automatically return `None`. For example, maybe it's a function that prints some text to the console, but doesn't explicitly return a value. The following code snippets all return the same value, `None`:

```python
def my_func():
    print("I do nothing")
    return None

def my_func():
    print("I do nothing")
    return

def my_func():
    print("I do nothing")
```

If we print the returned value, we see it is `None`.

```python
result = my_func()
# I do nothing

print(result)
# None
```

## 3.6 Multiple return values

A function can return more than one value by separating them with commas.

```python
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana  # return two values
```

**Receiving multiple values**

When calling a function that returns multiple values, you can assign them to multiple variables.

```python
damage, mana = cast_iceblast(5, 100)
print(f"Damage: {damage}, Remaining Mana: {mana}")
# Damage: 10, Remaining Mana: 90
```

When `cast_iceblast` is called, it returns two values. The first value is assigned to `damage`, and the second value is assigned to `mana`. Just like function inputs, it's the order of the values that matters, not the variable names. We could just as easily have named the variables `one` and `two`:

```python
one, two = cast_iceblast(5, 100)
print(f"Damage: {one}, Remaining Mana: {two}")
# Damage: 10, Remaining Mana: 90
```

Descriptive variable names make your code easier to understand, so name them well!

**What happened to the variables?**

The `damage` and `new_mana` variables from `cast_iceblast`'s function body only exist inside of the function. They can't be used outside of the function. More on that later when we talk about scope.

## 3.7 Parameters vs. arguments

Parameters are the names used for inputs when defining a function. Arguments are the values of the inputs supplied when a function is called.

To reiterate, arguments are the actual values that go into the function, such as `42.0`, `"the dark knight"`, or `True`. Parameters are the names we use in the function definition to refer to those values, which at the time of writing the function, can be whatever we like.

That said, this is all semantics, and frankly developers are really lazy with these definitions. You'll often hear the words "arguments" and "parameters" used interchangeably.

```python
# a and b are parameters
def add(a, b):
    return a + b


# 5 and 6 are arguments
sum = add(5, 6)
```

## 3.8 Default values

In Python you can specify a default value for a function parameter. It's useful when a function has parameters that are "optional." You can specify a default value in case the caller doesn't provide one.

A default value is created by using the assignment (`=`) operator in the function signature.

```python
def get_greeting(email, name="there"):
    print("Hello", name + ", welcome! You've registered your email:", email)

get_greeting("lane@example.com", "Lane")
# Hello Lane, welcome! You've registered your email: lane@example.com

get_greeting("lane@example.com")
# Hello there, welcome! You've registered your email: lane@example.com
```

If the second parameter is omitted, the default `"there"` value will be used in its place. As you may have guessed, for this structure to work, optional parameters (the ones with defaults) must come after all required parameters.

# CH4: Scope

## 4.0 Scope

Scope refers to where a variable or function name is available to be used. For example, when we create variables in a function (such as by giving names to our parameters), that data is not available outside of that function.

**Example**

```python
def subtract(x, y):
    return x - y


result = subtract(5, 3)
print(x)
# ERROR! "name 'x' is not defined"
```

When the `subtract` function is called, we assign `5` to the variable `x`, but `x` only exists in the code within the `subtract` function. If we try to print `x` outside of that function, then we won't get a result. In fact, we'll get a big fat error.

## 4.1 Global scope

So far we've been working in the global scope. That means that when we define a variable or a function, that name is accessible in every other place in our program, even within other functions.

For example:

```python
pi = 3.14


def get_area_of_circle(radius):
    return pi * radius * radius
```

Because `pi` was declared in the parent "global" scope, it is usable within the `get_area_of_circle()` function.

# CH5: Testing and Debugging

## 5.0 Unit tests

Up until this point, all the coding lessons you've completed have been testing you based on your code's console output (what's printed). For example, a lesson might expect your code (in conjunction with the code we provide) to print something like:

```
Armor: 2
Health: 18
```

If your code prints that exact output, you pass. If it doesn't, you fail.

**A new type of lesson**

Going forward, you'll encounter a new type of lesson: unit tests. A unit test is just an automated program that tests a small "unit" of code. Usually just a function or two.

The editor will have tabs:

- The `main.py` file containing your code.
- The `main_test.py` file containing the unit tests.

These new unit-test-style lessons will test your code's functionality rather than its output. Our tests will call functions in your code with different arguments, and expect certain return values. If your code returns the correct values, you pass. If it doesn't, you fail.

There are two reasons for this change:

- It's more realistic. In the real world, you'll be writing unit tests and running them against your code to make sure it works as expected.
- You can run and debug your code with print statements, and leave those print statements in when you submit. Unlike the output-based lessons, you won't have to remove your print statements to pass.

Also, ▶ Run and ▶ Submit work a little differently than before. When you run your code, it only runs some of the tests, but when you submit your code, it runs all of the tests. This is to simulate a production environment with unexpected edge cases and to teach you to think them through. Luckily for you, all of the tests are visible in the `main_test.py` file tab, so be sure to always check them before submitting.

## 5.1 Two lesson types

As we talked about, there are 2 types of coding lessons on Boot.dev:

- Console output lessons
- Unit-test lessons

**Console output lessons**

- Only 1 file of code, usually with a comment explaining where to write your code.
- When you "submit" your code, its console output must match the expected output exactly to pass.
- Debug print statements will cause your code to fail submission, so remove them before submitting.

**Unit-test lessons**

- 2 files of code: `main` and `main_test`. You can read the tests but you can't edit them.
- When you "submit" your code, the return values of your functions must match the expected values exactly to pass.
- Console output is ignored, you can leave debug print statements in your code.

**Which is more common?**

Going forward, you'll encounter far more unit-test lessons than console output lessons, but you'll still see both from time to time. Different concepts are better suited to different types of lessons.

## 5.2 Debugging

When you're working as a professional developer, you'll typically write code on your computer and test it by yourself before it's deployed to users.

That first part of the process is called debugging. You write some code, run it, and if it doesn't work, you fix the bugs. You repeat this process until you're confident that your code works as expected.

**Run vs. Submit**

At Boot.dev, the Run button is for debugging. The Submit button mimics the idea of publishing your code for production use.

You should be debugging your code using the Run button. You should be adding `print()` statements to your code to make sure it's doing what you think it's doing at different points in the code.

1. Write a line to calculate a value.
2. `print()` the value you calculated.
3. Run the code.
4. Did it print what you expected? If not, fix it.
5. Repeat.

You will never lose XP or be penalized on Boot.dev for using the run button. However, there are consequences for submitting broken code, just like there are career consequences for pushing broken code to your users!

**The Submit button will run additional tests**

When you use the Run button, a few tests will run against your code. However, the Submit button will run additional tests that you're not able to debug against. That's what keeps it fun and realistic (it's so hard to know what your users will do with your code!).

## 5.3 Learning effectively

This course is about to get a bit harder. There's no way around it, if programming were a walk in the park everyone would be earning 6 figures as a software engineer. But it's not, and to succeed without getting stuck and frustrated, you need to learn how to learn.

**Process for solving hard coding problems**

1. Read the lesson first! Figure out the examples before writing your own code.
2. Read the assignment. Understand the goal of the assignment before you start writing code.
3. Start writing code.
4. Add `print()` statements. Don't wait until you've written a lot of code to start testing. Add `print()` statements and use the Run button to see if your code is doing what you expect at each step. It's easier to find issues in small bits of code than in large blocks of code.
   - Keep running, printing, and fixing until you're confident your code is working.
5. Submit your code. If the assignment you're working on has unit tests, no need to remove your debugging `print()` statements. If the assignment you're working on is testing console output, be sure to remove your `print()` statements before submitting.
6. Compare your code to the instructor's. You will not be penalized for looking at the solution after you have successfully completed the assignment.

**Additional tidbits**

- Try to use Boots before peeking at the solution. Boots is quite good at giving you pointed hints to help you solve the problem on your own.
- It's okay to peek at the solution when you're completely stuck every once in a while, but don't make it a habit. If you find that you're always stuck, you should restart the chapter or course to make sure you understand the material.
- You can reset your code for an assignment with the "reset" ↶ button. For example, maybe you forgot which modifications you made vs which code was left by the instructor.
- You can reset all your cached code from the settings page. This is useful if you want to restart a course or chapter.

## 5.4 Debugging practice

This walks through how to approach writing code, complete with all the debugging steps taken along the way.

The goal is to write small amounts of code, and then test each bit of code to make sure it's doing what we expect before moving on. Trying to write entire programs at once is a recipe for pain and suffering. The goal is to write a few lines, test them, and then write a few more lines, and repeat until you're done.

This isn't a technique that's unique to beginners. Even senior engineers write code this way.

## 5.5 Stack trace

A stack trace (or "traceback") is a scary-looking error message that the Python interpreter prints to the console when it encounters certain problems. Stack traces are most common (at least for you right now) when you're trying to run invalid Python code.

You need to get used to figuring out scary error messages as a programmer. We might as well start now.

# CH6: Computing

## 6.0 Python numbers

In Python, numbers without a decimal point are called Integers – just like they are in mathematics.

Integers are simply whole numbers, positive or negative. For example, `3` and `-3` are both examples of integers.

Arithmetic can be performed as you might expect:

**Addition**

```python
2 + 1
# 3
```

**Subtraction**

```python
2 - 1
# 1
```

**Multiplication**

```python
2 * 2
# 4
```

**Division**

```python
3 / 2
# 1.5 (a float)
```

This one is actually a bit different – division on two integers will actually produce a float. A float is, as you may have guessed, the number type that allows for decimal values.

## 6.1 Numbers review

**Integers**

In Python, numbers without a decimal point are called Integers.

Integers are simply whole numbers, positive or negative. For example, `3` and `-3` are both examples of integers.

**Floats**

A float is, as you may have guessed, the number type that allows for decimal values.

```python
my_int = 5
my_float = 5.5
```

## 6.2 Floor division

Python has great out-of-the-box support for mathematical operations. This, among other reasons, is why it has had such success in artificial intelligence, machine learning, and data science applications.

Floor division is like normal division except the result is floored afterward, which means the result is rounded down to the nearest integer. The `//` operator is used for floor division.

```python
8 // 3
# 2 (an integer, rounded down from 2.666)
-7 // 3
# -3 (an integer, rounded down from -2.333)
```

## 6.3 Exponents

Python has built-in support for exponents – something most languages require a math library for.

```python
# reads as "three squared" or
# "three raised to the second power"
3**2
# 9
```

Sometimes exponents are also shown in text using the caret symbol (`^`):

`5^3 = 5³`

## 6.4 Changing in place

It's fairly common to want to change the value of a variable based on its current value.

```python
player_score = 4
player_score = player_score + 1
# player_score now equals 5

player_score = 4
player_score = player_score - 1
# player_score now equals 3
```

Don't let the fact that the expression `player_score = player_score - 1` is not a valid mathematical expression confuse you. It doesn't matter, it is valid code. It's valid because the way the expression should be read in English is:

> Assign to `player_score` the current value of `player_score` minus 1

In this operation, the right-hand side (`player_score - 1`) is calculated first. Once we have the result, we update `player_score` with this new value.

## 6.5 Plus equals

Python makes reassignment easy when doing math. In JavaScript or Go, you might be familiar with the `++` syntax for incrementing a number variable by 1. In Python, we use the `+=` in-place operator instead.

```python
star_rating = 4
star_rating += 1
# star_rating is now 5
```

**Other operators**

The other in-place operators work similarly:

```python
star_rating = 4
star_rating -= 1
# star_rating is now 3

star_rating = 4
star_rating *= 2
# star_rating is now 8

star_rating = 4
star_rating /= 2
# star_rating is now 2.0
```

## 6.6 Scientific notation

As we covered earlier, a float is a positive or negative number with a fractional part.

You can add the letter `e` or `E` followed by a positive or negative integer to specify that you're using scientific notation.

```python
print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071
```

If you're not familiar with scientific notation, it's a way of expressing numbers that are too large or too small to conveniently write normally.

In a nutshell, the exponent following the `e` specifies how many places to move the decimal: right when the exponent is positive, left when it's negative.

**Underscores for readability**

Python also allows you to represent large numbers in the decimal format using underscores as the delimiter instead of commas to make it easier to read.

```python
num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000
```

## 6.7 Logical operators

You're probably familiar with the logical operators `and` and `or`.

Logical operators deal with boolean values, `True` and `False`.

The logical `and` operator requires that both inputs are `True` to return `True`. The logical `or` operator only requires that at least one input is `True` to return `True`.

For example:

```python
True and True == True
True and False == False
False and False == False

True or True == True
True or False == True
False or False == False
```

**Python syntax**

```python
print(True and True)
# prints True

print(True or False)
# prints True
```

**Nesting with parentheses**

We can nest logical expressions using parentheses.

```python
print((True or False) and False)
```

First, we evaluate the expression in the parentheses, `(True or False)`. It evaluates to `True`:

```python
print(True and False)
```

`True and False` evaluates to `False`:

```python
print(False)
```

So, `print((True or False) and False)` prints `"False"` to the console.

## 6.8 Not

We skipped a very important logical operator – `not`. The `not` operator reverses the result. It returns `False` if the input was `True` and vice-versa.

```python
print(not True)
# Prints: False

print(not False)
# Prints: True
```

## 6.9 Binary numbers

Binary numbers are just "base 2" numbers. They work the same way as "normal" base 10 numbers, but with two symbols instead of ten.

- Base-2 (binary) symbols: `0` and `1`
- Base-10 (decimal) symbols: `0, 1, 2, 3, 4, 5, 6, 7, 8, 9`

Each digit's place value is double the place to its right. In a 4-digit binary number, the place values are:

- Eights
- Fours
- Twos
- Ones

For example, `0101` means:

- 0 eights
- 1 four
- 0 twos
- 1 one

So `0101` is `5` in decimal.

## 6.10 Binary in Python

You can write an integer in Python using binary syntax using the `0b` prefix:

```python
print(0b0001)
# Prints 1

print(0b0101)
# Prints 5
```

Leading 0s are often added for visual consistency but do not change the value of a binary number.

## 6.11 Bitwise "&" operator

Bitwise operators are similar to logical operators, but instead of operating on boolean values, they apply the same logic to all the bits in a value by column. For example, say you had the numbers 5 and 7 represented in binary. You could perform a bitwise AND operation and the result would be 5.

- `0101` is 5
- `0111` is 7

```
  0101
& 0111
------
  0101   ->  5
```

A `1` in binary is the same as `True`, while `0` is `False`. So really a bitwise operation is just a bunch of logical operations that are completed in tandem by column.

```
0 & 0 = 0
1 & 1 = 1
1 & 0 = 0
```

Ampersand `&` is the bitwise AND operator in Python. "AND" is the name of the bitwise operation, while ampersand `&` is the symbol for that operation. For example, `5 & 7 = 5`, while `5 & 2 = 0`.

- `0101` is 5
- `0010` is 2

```
  0101
& 0010
------
  0000
```

**Binary notation**

When writing a number in binary, the prefix `0b` is used to indicate that what follows is a binary number. `0b10` is two in binary, but `10` without the `0b` prefix is simply ten.

- `0b0101` is 5
- `0b0111` is 7

**Putting it together**

```python
0b0101 & 0b0111
# equals 5

binary_five = 0b0101
binary_seven = 0b0111
binary_five & binary_seven
# equals 5
```

## 6.12 Bitwise "|" operator

As you may have guessed, the bitwise "or" operator is similar to the bitwise "and" operator in that it works on binary rather than boolean values. However, the bitwise "or" operator "or"s the bits together. Here's an example:

- `0101` is 5
- `0111` is 7

```
  0101
| 0111
------
  0111   ->  7
```

A `1` in binary is the same as `True`, while `0` is `False`. So a bitwise operation is just a bunch of logical operations that are completed in tandem. When two binary numbers are "or"ed together, the result has a `1` in any place where either of the input numbers has a `1` in that place.

`|` is the bitwise "or" operator in Python. `5 | 7 = 7` and `5 | 2 = 7` as well!

- `0101` is 5
- `0010` is 2

```
  0101
| 0010
------
  0111
```

# CH7: Comparisons

## 7.0 Comparison operators

When coding it's necessary to be able to compare two values. Boolean logic is the name for these kinds of comparison operations that always result in `True` or `False`.

The operators:

- `<` "less than"
- `>` "greater than"
- `<=` "less than or equal to"
- `>=` "greater than or equal to"
- `==` "equal to"
- `!=` "not equal to"

For example:

```python
5 < 6   # evaluates to True
5 > 6   # evaluates to False
5 >= 6  # evaluates to False
5 <= 6  # evaluates to True
5 == 6  # evaluates to False
5 != 6  # evaluates to True
```

## 7.1 Comparison operator evaluations

When a comparison happens, the result of the comparison is just a boolean value, it's either `True` or `False`.

Take the following two examples:

```python
is_bigger = 5 > 4

is_bigger = True
```

In both of the above cases, we're creating a Boolean variable called `is_bigger` with a value of `True`.

Because 5 is greater than 4, `is_bigger` is assigned the value of `True`.

## 7.2 Comparison practice

```python
car_size = 4
truck_size = 5
is_smaller = car_size < truck_size
# is_smaller is True
```

## 7.3 If statements

It's often useful to only execute code if a certain condition is met:

```python
if CONDITION:
    # do some stuff here

# code after the if block may still run regardless
```

For example, in this code:

```python
def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
        return
    print("Ganondorf is unalive!")
```

If `boss_health` is greater than 0, then this will be printed:

```
Ganondorf is alive!
```

Otherwise, this will be printed:

```
Ganondorf is unalive!
```

Without a `return` in the `if` block, "Ganondorf is unalive" would always be printed:

```python
def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
    print("Ganondorf is unalive!")
```

This code could print both messages:

```
Ganondorf is alive!
Ganondorf is unalive!
```

When you only want code within an `if` block to run, use `return` to exit the function early.

Indentation is what tells Python whether the body of a function or the `if` statement has ended. Don't forget the colon after your `if` statement `:`; it is a required part of the syntax!

## 7.4 If practice

Remember, you can use the `==` operator to check if two values are equal. For example:

```python
is_equal = 5 == 5
# is_equal is True
```

## 7.5 If-else

An `if` statement can be followed by zero or more `elif` (which stands for "else if") statements, which can be followed by zero or one `else` statements.

For example:

```python
if score > high_score:
    print("High score beat!")
elif score > second_highest_score:
    print("You got second place!")
elif score > third_highest_score:
    print("You got third place!")
else:
    print("Better luck next time")
```

First the `if` statement is evaluated. If it is `True` then the `if` statement's body is executed and all the other `elif`s and the `else` are ignored.

If the first `if` is false then the next `elif` is evaluated. Likewise, if it is `True` then its body is executed and the rest are ignored.

If none of the `if` or `elif` statements evaluate to `True` then the final `else` statement will be the only body executed.

## 7.6 If-else practice

Here are some basic rules with if/else blocks.

- You can't have an `elif` or an `else` without an `if`.
- You can have an `else` without an `elif`.

Remember, to check if two values are the same use the `==` operator.

```python
are_equal = 5 == 6
# are_equal is False

are_equal = 6 == 6
# are_equal is True
```

**Assignment**

Complete the `check_high_score` function. If the `player_name` matches the high score name, return the string `"high"`. Otherwise, if it's the low scorer, return the string `"low"`. Otherwise, return the string `"neither"`.

## 7.7 Boolean logic

Boolean logic refers to logic dealing with boolean (`True` or `False`) values. For example:

- Dogs must have four legs and weigh less than 100 kilograms. (Both conditions must be true.)
- Cars are cool if they go faster than 200 MPH, or if they are electric. (At least one condition must be true.)

**Logical operators review**

As we discussed earlier, the logical operators `and` and `or` can be used to perform boolean logic.

**`and` review**

The `and` operator returns `True` if both of the conditions on either side evaluate to `True`:

```python
def is_dog(num_legs, weight):
    return num_legs == 4 and weight < 100
```

Let's go over how this function evaluates the parameters `num_legs=4` and `weight=99`:

```python
return 4 == 4 and 99 < 100

return True and True

return True
```

Let's see what would happen with `3` and `98` instead:

```python
return 3 == 4 and 98 < 100

return False and True

return False
```

**`or` review**

The `or` operator returns `True` if at least one of the conditions on either side evaluates to `True`:

```python
def is_car_cool(speed, is_electric):
    return speed > 200 or is_electric
```

Let's use a non-electric car that can do 250:

```python
return 250 > 200 or False

return True or False

return True
```

## 7.8 Should serve drinks

**Assignment**

In Fantasy Quest, players can go to a town's local pub. Drinking virtual beer refills their stamina!

Complete the function that determines if a bartender should serve drinks to a customer. Only return `True` if all of these conditions apply. If any of these conditions are `False`, return `False`:

- The customer's age is 21 or older.
- The bartender is working.
- The time is between 5 and 10 o'clock (inclusive of both 5 and 10).

**Tips: understand the problem**

This assignment tests your ability to think critically by challenging your expectations up to this point. First, understand the problem before rushing to conclusions about the requirements. Then, convert these positive conditions into negatives. Finally, convert them into code.

- If the customer's age is less than 21, return `False`.
- If the bartender is on break, return `False`.
- If the time is before 5 or after 10, return `False`. This means 5 and 10 would return `True`.
- Return `True`.

Why go through the hassle of inverting the logic? These early returns are the whole solution. The alternative is to write a function that is deeply nested and therefore less readable and more confusing than the solution.

```python
def check_conditions(condition_1, condition_2, condition_3):
    if condition_1:
        if not condition_2:
            if condition_3 > 1:
                return True
    return False
```

## 7.9 If statements don't need a comparison

Where `is_big` is a boolean value, the following statements are identical:

```python
if is_big:
    # ...

if is_big == True:
    # ...
```

The first option should be preferred due to length; however, the second is more readable. The `== True` is redundant.

# CH8: Loops

## 8.0 Loops

Loops are a programmer's best friend. Loops allow us to do the same operation multiple times without having to write it explicitly each time.

For example, let's pretend I want to print the numbers 0-9. I could do this:

```python
print(0)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
```

Even so, it would save me a lot of time typing to use a loop. Especially if I wanted to do the same thing one thousand or one million times.

A "for loop" in Python is written like this:

```python
for i in range(0, 10):
    print(i)
```

`i` is a variable that takes on each value from 0 to 9, one at a time. In English, the code says:

1. Start with `i` equals 0. (`i in range(0)`)
2. If `i` is greater than or equal to 10 (`range(0, 10)`), exit the loop. Else:
   - Print `i` to the console. (`print(i)`)
   - Add 1 to `i`. (`range` defaults to incrementing by 1)
   - Go back to step 2.

The result is that the numbers 0-9 are logged to the console in order.

The numbers `a` and `b` in `range(a, b)` are inclusive of `a` and exclusive of `b`. So `range(0, 10)` includes 0 but not 10.

**Whitespace matters in Python!**

The body of a for-loop must be indented, otherwise you'll get a syntax error.

## 8.1 Range continued

The `range()` function we've been using in our for loops actually has an optional 3rd parameter: the "step."

```python
for i in range(0, 10, 2):
    print(i)
# prints:
# 0
# 2
# 4
# 6
# 8
```

The "step" parameter determines how much to add to `i` in each iteration of the loop. You can even go backwards:

```python
for i in range(3, 0, -1):
    print(i)
# prints:
# 3
# 2
# 1
```

## 8.2 Sum game

Remember you can use in-place operators to increase or decrease a variable by any amount.

```python
number_of_enemies = 10
number_of_enemies += 2
# number_of_enemies is 12

number_of_enemies = 10
number_of_enemies -= 2
# number_of_enemies is 8
```

## 8.3 While

Python has another type of loop, the while loop. It's a loop that continues while a condition remains `True`. The syntax is simple:

```python
while 1:
    print("1 evaluates to True")

# prints:
# 1 evaluates to True
# 1 evaluates to True
# (...continuing)
```

The example above is hardcoded to continue forever, creating an infinite loop. Typically, a while loop condition is a comparison or variable, and it determines when the loop ends:

```python
num = 0
while num < 3:
    num += 1
    print(num)

# prints:
# 1
# 2
# 3
# (the loop stops when num >= 3)
```

## 8.4 Continue statement

Sometimes, while looping through a sequence, you may find items that you want to skip. Python (like many programming languages) provides a way to do this: the `continue` statement.

`continue` means "go directly to the next iteration of this loop." Whatever else was supposed to happen in the current iteration is skipped.

Let's say we want to print all the numbers from 1 to 50, but skip every 7th number. We can use `continue` to do this, by keeping track of a counter:

```python
# Remember, `range` is inclusive of the start, but exclusive of the end
counter = 0
for number in range(1, 51):
    counter = counter + 1

    if counter == 7:
        counter = 0  # Reset the counter
        continue  # Skip this number

    print(number)
```

What we'll see printed are all the numbers from 1 to 50, except for 7, 14, 21, 28, 35, 42, and 49.

**Avoiding work**

A `continue` statement immediately halts the current iteration and jumps to the next one, which saves the program from doing unnecessary work.

For example, if we're calculating square roots, we might want to skip negative numbers. `continue` lets us move on to the next number without wasting any time:

```python
for number in range(-5, 5):
    if number < 0:
        continue  # Skip negatives

    print(f"The square root of {number} is {number**0.5}")
```

This would print:

```
The square root of 0 is 0.0
The square root of 1 is 1.0
The square root of 2 is 1.4142135623730951
The square root of 3 is 1.7320508075688772
The square root of 4 is 2.0
```

Using `continue` to avoid pointless work can make your code run faster, which is especially helpful if the loop includes time-consuming computations.

## 8.5 Break statement

We can use `continue` to skip to the next iteration in a loop, but what if we want to exit the loop entirely? That's where the `break` statement comes in.

```python
for n in range(42):
    print(f"{n} * {n} = {n * n}")
    if n * n > 150:
        break

# 0 * 0 = 0
# 1 * 1 = 1
# 2 * 2 = 4
# 3 * 3 = 9
# 4 * 4 = 16
# 5 * 5 = 25
# 6 * 6 = 36
# 7 * 7 = 49
# 8 * 8 = 64
# 9 * 9 = 81
# 10 * 10 = 100
# 11 * 11 = 121
# 12 * 12 = 144
# 13 * 13 = 169
```

This code would loop from 0 all the way to 41, but it actually exits early. Once `n * n` is greater than 150, the `break` statement executes, stopping the loop.


