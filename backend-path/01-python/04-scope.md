# 04: Scope

Source: boot.dev Learn Python, Chapter 4, Lessons 1 to 2.

## What it is

### Local scope

Scope is the region of a program where a name, such as a variable or a function, can be used. A name is not available everywhere just because it exists somewhere in the file.

Every function has its own local scope. Parameters and any variables assigned inside the function body belong to that scope and only exist while the function runs:

```python
def subtract(x, y):
    return x - y


result = subtract(5, 3)
print(x)
# NameError: name 'x' is not defined
```

When `subtract(5, 3)` runs, `5` is assigned to `x` and `3` to `y`, but only inside `subtract`. Once the function returns, those names are gone. Only the returned value, stored in `result`, makes it back out. Trying to use `x` outside the function raises a `NameError`, the same error as using a variable that was never assigned.

Each call starts with a fresh local scope. Local variables do not remember their values from the previous call, and two functions can use the same variable name without affecting each other, because each name lives in a different scope.

### Global scope

Names defined at the top level of a file, outside any function, are in the global scope. Every variable and function from the earlier chapters was global. A global name can be used anywhere in the file, including inside functions:

```python
pi = 3.14


def get_area_of_circle(radius):
    return pi * radius * radius
```

`pi` is not defined inside `get_area_of_circle`, so Python looks for it in the global scope and finds it there. Functions themselves are global names too, which is why one function can call another.

Like the function calls in Chapter 3, the lookup happens when the function runs, not when it is defined. If a global changes between two calls, the function sees the new value on the second call.

Scope only goes one way. A function can read names from the global scope, but the global scope cannot read names from inside a function.

### How Python finds a name

When Python sees a name, it searches a fixed list of scopes in order and uses the first match. The order is known as LEGB:

1. **Local:** the current function's parameters and variables.
2. **Enclosing:** the scopes of any functions that this function is nested inside.
3. **Global:** the top level of the current file.
4. **Built-in:** names Python provides everywhere, such as `print`, `len`, and `int`.

If the name is in none of them, Python raises a `NameError`. The enclosing scope only matters for functions defined inside other functions, which is a later topic.

### Assigning inside a function

Reading a global from inside a function works, but assigning to the same name does not change the global. Assignment inside a function always creates or updates a local variable:

```python
health = 100


def take_damage():
    health = 50
    return health
```

Calling `take_damage()` returns `50`, but the global `health` is still `100`. The local `health` hides the global one inside the function. This is called shadowing.

Python decides which names are local before the function runs, by checking for assignments anywhere in its body. So a function that reads a name and then assigns to it fails, because the name is treated as local for the whole function:

```python
health = 100


def take_damage():
    health -= 10
    return health

take_damage()
# UnboundLocalError: cannot access local variable 'health' where it is not associated with a value
```

The `global` keyword tells Python that a name inside the function refers to the global variable, so assignments change it. It works, but functions that quietly change globals are hard to follow and test. The usual approach is to pass the value in as an argument and return the new value, which is what the course does by keeping only `player_level` global and letting the functions compute everything else.

### Blocks do not create scope

In Python, only functions (and classes and modules) create a new scope. `if` blocks and loops do not. A variable assigned inside an `if` or a `for` loop at the top level is still global, and is available after the block ends. This is different from many other languages.

## Analogy

Continuing the kitchen from Chapters 1 to 3: **scope is who can see which notes.**

- The global scope is the whiteboard on the kitchen wall. Anything written there, such as "today's special: salmon" or the recipe cards pinned beside it, can be read by every cook at every station.
- A function's local scope is the scratch paper a cook uses while following one recipe card. Notes like "3 tomatoes chopped" are on that paper only.
- When the cook finishes, they hand back the finished dish (the return value) and throw the scratch paper away. Nobody else ever sees it, and the next time that card is used, the cook starts with a clean sheet.
- Two cooks can both write "sauce" on their own scratch paper without confusing each other.
- When a cook needs something not on their scratch paper, they look up at the whiteboard. If it is not there either, they check the restaurant's standard rules (the built-ins). If it is nowhere, they stop and complain (`NameError`).
- Writing "special: tuna" on your own scratch paper does not change the whiteboard. It only means you stop looking at the whiteboard for that item (shadowing).
- `global` is walking over and rewriting the whiteboard yourself. It works, but everyone else is surprised by the change. It is better to hand your result back and let the head chef update the board.

## Example

```python
# Parameters and local variables only exist inside the function
def subtract(x, y):
    return x - y

result = subtract(5, 3)
print(result)                           # 2
# print(x)                              # NameError: name 'x' is not defined

# Global names can be read inside functions
pi = 3.14

def get_area_of_circle(radius):
    return pi * radius * radius

print(get_area_of_circle(5))            # 78.5

# Globals are looked up when the function runs
player_level = 4

def get_max_health():
    return player_level * 100

print(get_max_health())                 # 400
player_level = 5
print(get_max_health())                 # 500

# Assigning inside a function creates a local and leaves the global alone
health = 100

def take_damage():
    health = 50
    return health

print(take_damage())                    # 50
print(health)                           # 100

# Each call starts with fresh locals
def count_calls():
    calls = 0
    calls += 1
    return calls

print(count_calls(), count_calls())     # 1 1

# The same name in different functions is a different variable
def first():
    name = "first"
    return name

def second():
    name = "second"
    return name

print(first(), second())                # first second

# global changes the global variable
score = 0

def add_point():
    global score
    score += 1

add_point()
add_point()
print(score)                            # 2

# The usual alternative: pass the value in and return the new one
def add_point_pure(score):
    return score + 1

score = add_point_pure(score)
print(score)                            # 3

# Shadowing a built-in only affects that scope
def shadow():
    len = 5
    return len

print(shadow(), len("abc"))             # 5 3

# if blocks and loops do not create a scope
if True:
    message = "hello"
print(message)                          # hello

for i in range(3):
    pass
print(i)                                # 2
```

Common errors:

```python
def f():
    y = 1

f()
print(y)                                # NameError: name 'y' is not defined

health = 100

def take_damage():
    health -= 10                        # UnboundLocalError: cannot access local variable 'health'
    return health                       # where it is not associated with a value

take_damage()
```

## In other languages

| | Python | JavaScript | Go | Bash |
|---|---|---|---|---|
| Function locals | Any name assigned in the body | Names declared with `let`, `const`, or `var` in the body | Names declared with `var` or `:=` in the body | Only names declared with `local`. Everything else is global |
| Global variables | Assigned at the top level of the file | Declared at the top level of the file or module | Declared with `var` at the package level | Any variable not marked `local` |
| Change a global from a function | Needs `global name` | Just assign it | Just assign it | Just assign it |
| Blocks (`if`, loops) create scope | No | Yes, for `let` and `const`. No, for `var` | Yes | No |
| Same name inside a block or function | Shadows the global inside the function | Shadows the outer variable inside the block | Shadows the outer variable inside the block | `local` shadows it inside the function |
| Using an undefined name | `NameError` when the line runs | `ReferenceError` when the line runs | Compile error | Empty string, no error (unless `set -u`) |

Two ideas carry over to every language:

1. **Keep names as local as possible.** The smaller the area where a variable can be read and changed, the easier the code is to reason about. Globals work best for values that never change, such as configuration or constants.
2. **Know what the default is.** Python makes assignments local by default and needs `global` to change a global. Bash does the opposite: variables are global unless marked `local`, which is a common source of bugs in shell scripts. JavaScript and Go let a function change an outer variable directly, but they add block scope, which Python does not have.

## Interview framing

1. What is scope?
2. What is the difference between local and global scope?
3. How does Python decide which variable a name refers to?
4. What happens when a function assigns to a variable that has the same name as a global?
5. What does the `global` keyword do, and when would you use it?
6. Why are global variables generally discouraged?

## My answer

**1. What is scope?**

"Scope is the part of a program where a name can be used. In Python, every function has its own local scope, the top level of a file is the global scope, and built-in names like `print` are available everywhere. A variable created inside a function, including its parameters, only exists inside that function while it runs. Using it outside raises a `NameError`."

**2. Local versus global**

"A global variable is defined at the top level of a file and can be read from anywhere in that file, including inside functions. A local variable is defined inside a function and only exists for that call. Each call gets a fresh set of locals, so they do not carry over between calls, and two functions can use the same variable name without interfering with each other."

**3. How Python resolves a name**

"Python follows the LEGB rule. It checks the local scope first, then any enclosing functions, then the global scope of the module, and finally the built-ins. It uses the first match it finds. If the name is in none of them, it raises a `NameError`. The lookup happens when the code runs, so a function sees the current value of a global, not the value it had when the function was defined."

**4. Assigning to a global's name inside a function**

"It creates a new local variable that shadows the global inside that function. The global is not changed. Python decides which names are local by looking for assignments anywhere in the function body, before running it. So if a function reads a global and then assigns to it, for example `health -= 10`, the name is treated as local from the start and the read fails with an `UnboundLocalError`."

**5. The `global` keyword**

"`global name` inside a function tells Python that assignments to `name` should change the module-level variable instead of creating a local. I would only use it for something like a small script's module-level state. In most code, it is cleaner to pass the value in as an argument and return the new value, so the function's effect is visible at the call site."

**6. Why avoid globals?**

"Any function can read or change a global, so when its value is wrong, the cause could be anywhere in the program. Functions that depend on globals are also harder to test, because their result depends on state that is not in their arguments, and they are not safe to run concurrently without care. Global constants are fine, by convention written in `UPPER_SNAKE_CASE`. Global state that changes is what causes problems."

**Points to recall**

- Scope is where a name can be used.
- Parameters and variables assigned in a function are local and disappear when the call ends.
- Each call gets fresh locals.
- Globals can be read inside functions and are looked up at call time.
- Name lookup order is LEGB: Local, Enclosing, Global, Built-in.
- Assigning inside a function creates a local that shadows the global.
- Reading and then assigning the same name in a function raises `UnboundLocalError`.
- `global` lets a function change a global, but passing and returning values is usually better.
- `if` blocks and loops do not create a new scope in Python.

## Follow-up gotchas

**Why does `health -= 10` fail inside a function when `print(health)` works?**
Because `health -= 10` is an assignment. Python sees the assignment when it compiles the function and marks `health` as local for the entire body. When the line runs, it tries to read the local `health` before it has a value, which raises `UnboundLocalError`. A function that only reads `health` has no assignment, so the name is found in the global scope.

**Does a function need `global` to change a global list?**
No. `global` is only needed to rebind the name, meaning to make it point to a new value. Calling a method that changes the object itself, such as `inventory.append("sword")`, only reads the name `inventory` and then modifies the list it points to, so it works without `global`. The difference between rebinding a name and mutating an object comes up again with lists and dictionaries.

**Is a variable defined inside an `if` block available after the block?**
Yes. Python has no block scope, so a variable assigned in an `if` or a loop belongs to the surrounding function or module. The catch is that if the block never runs, the variable is never assigned, and using it later raises an error. A loop variable also keeps its last value after the loop ends.

**What is `nonlocal`?**
It is the equivalent of `global` for nested functions. When a function is defined inside another function, `nonlocal name` lets the inner function rebind a variable from the outer function's scope. This is the "Enclosing" part of LEGB and is mainly used with closures.

**What happens if you name a variable `list` or `len`?**
It shadows the built-in in that scope. Python finds your variable first, so `len("abc")` in that scope would try to call your variable instead and fail. It is legal, but it causes confusing bugs. Avoid built-in names such as `list`, `dict`, `str`, `id`, `input`, and `sum` for your own variables.

**Are global variables shared between files?**
No. Each Python file, or module, has its own global scope. To use a name from another file, it has to be imported. In that sense "global" in Python really means "module level."
