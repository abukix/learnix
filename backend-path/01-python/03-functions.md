# 03: Functions

Source: boot.dev Learn Python, Chapter 3, Lessons 1 to 17.

## What it is

### Defining and calling

A function is a named block of code that can be run whenever it is needed. Functions let a program reuse logic instead of copying it, and they give a piece of work a name so the code reads like a description of what it does.

A function is defined with the `def` keyword:

```python
def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result
```

- `area_of_circle` is the function's name. It follows the same `snake_case` convention as variables.
- `r` is a parameter: a name for the input the function will receive.
- The indented lines after the colon are the function body.
- `return` sends a value back to whoever called the function.

Defining a function does not run it. Python only records that the function exists. The body runs when the function is called, by writing its name followed by parentheses: `area_of_circle(5)`. A function can be called as many times as needed, each time with different inputs.

### How a call runs

When Python reaches a call such as `area = area_of_circle(5)`:

1. The argument `5` is evaluated and assigned to the parameter `r`.
2. Execution jumps into the function body and runs it from top to bottom.
3. `return result` ends the function and hands the value `78.5` back.
4. The call expression `area_of_circle(5)` evaluates to `78.5`, which is then stored in `area`.
5. Execution continues on the line after the call.

A function call is an expression. Anywhere a value can go, a call that returns that value can go too, such as `print(area_of_circle(5))`.

Variables created inside the body, such as `pi` and `result`, only exist while the function runs. They cannot be used outside the function. This is called scope and is covered in its own chapter.

### Parameters and arguments

- **Parameters** are the names listed in the function definition. `a` and `b` in `def subtract(a, b)`.
- **Arguments** are the actual values passed in when calling. `5` and `3` in `subtract(5, 3)`.

In conversation, developers use the two words interchangeably, but the distinction is useful when precision matters.

A function can take any number of parameters, separated by commas. By default, arguments are matched to parameters by position: the first argument goes to the first parameter, the second to the second, and so on. `subtract(5, 3)` is `2`, and `subtract(3, 5)` is `-2`. Arguments can also be passed by name, called keyword arguments: `subtract(b=3, a=5)` is `2`, regardless of order.

Calling a function with the wrong number of arguments raises a `TypeError`.

### Return versus print

`print()` and `return` can look interchangeable because both make a value appear when testing, but they do different things.

| | `print()` | `return` |
|---|---|---|
| What it is | A built-in function | A keyword |
| What it does | Writes a value to the console | Ends the function and hands a value back to the caller |
| Who sees the value | The person reading the console | The code that called the function |
| Can the value be reused | No | Yes. It can be stored, passed on, or printed later |

A function that prints its result instead of returning it is a common bug. The caller receives `None` and cannot do anything with the result.

`return` also ends the function immediately. Any code after a `return` that executes is never reached.

Printing is still the simplest way to debug, because it shows what a variable holds at a specific point. Debugging prints should be removed once the problem is found.

### Returning None

Every function returns a value. If a function has no `return` statement, or uses a bare `return`, it returns `None`. These three functions behave identically:

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

This is why `print(print("hi"))` prints `hi` and then `None`: the inner `print()` writes to the console and returns `None`.

### Multiple return values

A function can return several values by separating them with commas:

```python
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana
```

The caller can unpack them into separate variables: `damage, mana = cast_iceblast(5, 100)`. As with arguments, it is the position that matters, not the names. The variables in the caller do not need to match the names used inside the function.

Under the hood, Python packs the values into a single tuple, `(10, 90)`, and the caller unpacks it. This is the same multiple assignment from Chapter 2.

### Default values

A parameter can have a default value, which makes it optional:

```python
def get_greeting(email, name="there"):
    return f"Hello {name}, welcome! You've registered your email: {email}"
```

If the caller passes an argument, that value is used. If the caller leaves it out, the default is used. Parameters with defaults must come after all parameters without defaults, otherwise Python raises a `SyntaxError`.

### Define before calling

Code runs from top to bottom, and `def` is a statement like any other. A function does not exist until its `def` line has run, so calling it earlier raises a `NameError`, just like using a variable before assigning it.

The standard way to avoid ordering problems is to define every function first and call a single entry point at the bottom of the file. By convention, that entry point is named `main`:

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


main()
```

`main` calls `add_armor` even though `add_armor` is defined below it. That works because the name is looked up when `main` actually runs, and by the time `main()` is called on the last line, every function has been defined. Only the order of the calls matters, not the order of the definitions.

## Analogy

Continuing the kitchen from Chapters 1 and 2: **a function is a recipe card for a sub-task, such as "make the sauce."**

- Defining a function is writing the card and pinning it to the wall. Nothing gets cooked by writing it.
- Calling a function is a cook taking the card down and following it. The same card can be used for every order of the night.
- Parameters are the blanks on the card: "use ___ tomatoes." Arguments are what fills the blanks for this particular order.
- Positional arguments are filling the blanks in order. Keyword arguments are writing "tomatoes: 4" so the order does not matter.
- `return` is handing the finished sauce back to the cook who asked for it, who can then use it in the next step.
- `print` is shouting "the sauce is ready!" into the dining room. Everyone hears it, but nobody receives any sauce.
- Returning `None` is a card that only says "wipe the counter." The work happens, but nothing is handed back.
- Multiple return values are handing back a tray with the sauce and the leftover tomatoes on it. The receiving cook takes them off the tray in order.
- A default value is a blank that is already filled in: "salt: one pinch, unless told otherwise."
- `main` is the head chef reading every card on the wall before service starts, and then calling out the first order.

## Example

```python
# Define once, call many times
def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result

print(area_of_circle(5))                # 78.5
print(area_of_circle(7))                # 153.86

# Arguments are matched to parameters by position
def subtract(a, b):
    return a - b

print(subtract(5, 3))                   # 2
print(subtract(3, 5))                   # -2
print(subtract(b=3, a=5))               # 2, keyword arguments match by name

# print versus return
def print_title(name):
    print(f"{name} the warrior")

def get_title(name):
    return f"{name} the warrior"

printed = print_title("Aang")           # Aang the warrior
print(printed)                          # None
returned = get_title("Aang")            # (nothing printed)
print(returned)                         # Aang the warrior

# return ends the function immediately
def check_health(health):
    if health <= 0:
        return "dead"
    return "alive"
    print("never runs")

print(check_health(0))                  # dead

# Multiple return values are a tuple
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana

damage, mana = cast_iceblast(5, 100)
print(damage, mana)                     # 10 90
print(cast_iceblast(5, 100))            # (10, 90)

# Default values make a parameter optional
def get_punched(health, armor=0):
    damage = 50 - armor
    return health - damage

print(get_punched(100))                 # 50
print(get_punched(100, 20))             # 70

# Define everything first, then call the entry point
def main():
    health = 10
    armor = 5
    add_armor(health, armor)            # defined below, but main() runs after it exists

def add_armor(h, a):
    print(f"The player now has {h + a} health")

main()                                  # The player now has 15 health
```

Common errors:

```python
greet()                                 # NameError: name 'greet' is not defined
def greet():
    print("hi")

subtract(1)                             # TypeError: subtract() missing 1 required positional argument: 'b'

def get_punched(armor=0, health):       # SyntaxError: parameter without a default follows parameter with a default
    ...
```

## In other languages

| | Python | JavaScript | Go | Bash |
|---|---|---|---|---|
| Define | `def add(a, b):` | `function add(a, b) {}` or `const add = (a, b) => {}` | `func add(a int, b int) int {}` | `add() { ... }` |
| Call | `add(2, 3)` | `add(2, 3)` | `add(2, 3)` | `add 2 3` |
| Read parameters | By name | By name | By name | Positionally, as `$1`, `$2`, and so on |
| Return a value | `return x` | `return x` | `return x`, with the type declared in the signature | `echo x`, captured with `$(add 2 3)`. `return` only sets an exit status from 0 to 255 |
| No return statement | Returns `None` | Returns `undefined` | Not allowed if the signature declares a return type | Exit status of the last command |
| Multiple return values | `return a, b` (a tuple) | Return an array or object and destructure it | Built in: `func f() (int, error)` | Print several values and split the output |
| Default values | `def f(a, b=0)` | `function f(a, b = 0)` | Not supported | `${2:-0}` |
| Wrong number of arguments | `TypeError` | Missing ones are `undefined`, extras are ignored | Compile error | Missing ones are empty strings |
| Call before definition | `NameError` | Works for `function` declarations (hoisting) | Works. Top-level order does not matter | Error: `command not found` |
| Entry point | `main()` by convention, usually under `if __name__ == "__main__":` | None. The file runs top to bottom | `func main()` in `package main` is required | None. The file runs top to bottom |

Two ideas carry over to every language:

1. **Return values and side effects are different things.** A function can hand data back to its caller, or it can affect the outside world, such as printing, writing a file, or sending a request. Bash makes this distinction obvious because "returning" data actually means printing it.
2. **Multiple returns are a design choice.** Go builds them into the language and uses them for errors, as in `value, err := f()`. Python returns a tuple, and JavaScript returns an array or object. The idea is the same: return everything the caller needs in one call.

## Interview framing

1. What is a function, and why are functions useful?
2. What is the difference between a parameter and an argument? Between positional and keyword arguments?
3. What is the difference between `print` and `return`?
4. What does a function return if it has no `return` statement?
5. How does Python return multiple values?
6. How do default parameter values work, and what are the rules for using them?
7. Why do Python programs often define a `main` function and call it at the bottom of the file?

## My answer

**1. What is a function?**

"A function is a named, reusable block of code that takes inputs, does some work, and optionally returns an output. Functions remove duplication, because the logic lives in one place and a fix applies everywhere it is used. They also make code easier to read, because a well-named function call describes what happens without the reader needing every detail. And they make code easier to test, because a small function with clear inputs and outputs can be tested on its own."

**2. Parameters versus arguments**

"Parameters are the names in the function definition, and arguments are the values passed in when the function is called. In `def add(a, b)`, `a` and `b` are parameters. In `add(5, 6)`, `5` and `6` are arguments. By default arguments are matched by position, so the first argument goes to the first parameter. Keyword arguments, such as `add(b=6, a=5)`, are matched by name instead, which makes calls with many parameters easier to read and harder to get wrong."

**3. `print` versus `return`**

"`print` writes a value to the console for a person to read. It is a side effect, and it gives nothing back to the code. `return` ends the function and hands a value back to the caller, which can store it, pass it to another function, or print it later. A function that prints when it should return looks correct in the console, but the caller actually receives `None`. As a rule, functions that compute something should return it, and printing should happen at the edges of the program."

**4. No `return` statement**

"It returns `None`. Every Python function returns something, so a function without a `return`, or with a bare `return`, gives back `None`. That is why assigning the result of a function like `print()` to a variable gives `None`."

**5. Multiple return values**

"Writing `return a, b` packs the values into a single tuple, and the caller usually unpacks it with `x, y = f()`. The unpacking is by position, so the names on the caller's side do not need to match the names inside the function. If the caller assigns the result to a single variable, it gets the whole tuple. For more than two or three values, I would return something with named fields, such as a dataclass or a named tuple, so callers do not depend on the order."

**6. Default values**

"A default makes a parameter optional: `def greet(email, name="there")`. If the caller leaves out `name`, the default is used. Parameters with defaults must come after parameters without them, otherwise it is a `SyntaxError`. The important detail is that the default is evaluated once, when the function is defined, not on every call. That is fine for numbers, strings, and `None`, but a mutable default like an empty list is shared between calls. The standard pattern is to default to `None` and create the list inside the function."

**7. Why `main`?**

"Python runs a file from top to bottom, and a function only exists after its `def` line has run. Defining every function first and calling one entry point at the end means all functions exist before any of them is used, so the order of the definitions stops mattering. In practice the call is usually wrapped in `if __name__ == "__main__": main()`. That way `main()` runs when the file is executed directly, but not when another file imports it, which keeps the file safe to reuse as a module."

**Points to recall**

- Defining a function does not run it. Calling it does.
- A call is an expression that evaluates to the returned value.
- Parameters are names in the definition. Arguments are values in the call. Positional arguments match by order, keyword arguments by name.
- `print` shows a value. `return` hands it back and ends the function.
- No `return` means the function returns `None`.
- `return a, b` returns a tuple that the caller unpacks by position.
- Defaults must come after required parameters and are evaluated once at definition time.
- Define functions first, then call `main()` at the bottom, usually under `if __name__ == "__main__":`.

## Follow-up gotchas

**What is wrong with `def add_item(item, items=[])`?**
The default list is created once, when the function is defined, and the same list is reused on every call. Calling `add_item("a")` and then `add_item("b")` returns `['a', 'b']` the second time, not `['b']`. Use `items=None` and write `if items is None: items = []` inside the function.

**Why can `main` call a function defined below it?**
Names inside a function body are looked up when the function runs, not when it is defined. As long as every function is defined before `main()` is called, the order of the definitions does not matter. Calling `main()` at the top of the file would still fail.

**What is the difference between `f` and `f()`?**
`f()` calls the function and evaluates to its return value. `f` without parentheses is the function itself, which is a value like any other. It can be stored in a variable or passed to another function. Forgetting the parentheses is a common bug: `if is_ready:` is always true, because a function object is truthy.

**What happens if you assign a multiple-return call to a single variable?**
The variable holds the whole tuple. `result = cast_iceblast(5, 100)` makes `result` equal to `(10, 90)`, and individual values are accessed as `result[0]` and `result[1]`. Unpacking into the wrong number of variables raises a `ValueError`.

**Does code after `return` ever run?**
Not in the same path. `return` exits the function immediately. A function can have several `return` statements in different branches, and whichever one runs first ends the call. Linters flag code placed directly after a `return` as unreachable.

**Is a function that returns `None` useless?**
No. Many functions exist for their side effects, such as printing, writing to a file, or updating a database. The useful habit is to separate them: functions that compute values should return them without side effects, and functions with side effects should make that obvious from their name, such as `save_user` or `print_report`.
