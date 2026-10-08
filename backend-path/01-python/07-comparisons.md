# 07: Comparisons

Source: boot.dev Learn Python, Chapter 7, Lessons 1 to 13.

## What it is

### Comparison operators

A comparison checks how two values relate and always produces a boolean, `True` or `False`. Python has six comparison operators:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `<` | Less than | `5 < 6` | `True` |
| `>` | Greater than | `5 > 6` | `False` |
| `<=` | Less than or equal to | `5 <= 6` | `True` |
| `>=` | Greater than or equal to | `5 >= 6` | `False` |
| `==` | Equal to | `5 == 6` | `False` |
| `!=` | Not equal to | `5 != 6` | `True` |

`==` compares, and `=` assigns. Writing `if x = 5:` is a `SyntaxError`, and Python suggests `==` in the error message.

### Comparisons are values

The result of a comparison is an ordinary `bool` value, so it can be stored in a variable or returned like any other value:

```python
is_bigger = 5 > 4      # same as is_bigger = True
```

This means a function that answers a yes or no question does not need an `if` at all. `return armor >= damage` already returns `True` or `False`. Writing `if armor >= damage: return True` followed by `return False` does the same thing in four lines instead of one.

### Comparing different types

- **Numbers** compare by value across types: `1 == 1.0` is `True`.
- **Strings** compare character by character, using each character's Unicode code point. `"apple" < "banana"` is `True`. Uppercase letters come before lowercase, so `"Zebra" < "apple"` is also `True`. Numbers stored as strings compare as text, so `"10" < "9"` is `True`, because `"1"` comes before `"9"`.
- **Unrelated types** are never equal: `"5" == 5` is `False`. Ordering them with `<` or `>` raises a `TypeError`: `"5" < 5` and `None < 1` both fail.

### Chained comparisons

Python lets comparisons be chained, as in math:

```python
5 <= time <= 10        # same as 5 <= time and time <= 10
```

Each pair is checked, and the middle value is only evaluated once. This is the cleanest way to write a range check. Most other languages do not support this and need the two halves joined with `&&`.

### If statements

An `if` statement runs a block of code only when its condition is true:

```python
if CONDITION:
    # runs only when CONDITION is true

# code here runs either way
```

Two parts of the syntax are required:

- **The colon** at the end of the `if` line. Leaving it out is a `SyntaxError: expected ':'`.
- **Indentation** for the body. Python has no braces. The indented lines are the body, and the first line back at the outer level ends it. A missing indent is an `IndentationError`.

Code after the `if` block runs whether or not the condition was true. To stop a function inside the `if`, use `return`, which exits the function early:

```python
def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
        return
    print("Ganondorf is unalive!")
```

Without the `return`, a living boss would print both messages.

### If, elif, else

An `if` can be followed by any number of `elif` ("else if") branches, and then at most one `else`:

```python
if score > high_score:
    print("High score beat!")
elif score > second_highest_score:
    print("You got second place!")
else:
    print("Better luck next time")
```

Python checks the conditions from top to bottom and runs the body of the **first** one that is true. The rest are skipped, even if they are also true. The `else` body runs only when nothing above it was true.

The rules:

- `elif` and `else` cannot appear without an `if` before them.
- `else` does not need an `elif`.
- Order matters. Conditions that overlap should go from the most specific to the most general. If `health <= 5` is checked before `health <= 0`, a health of `-1` matches the first branch and the `dead` branch is never reached.

A branch can also set a variable instead of returning, with a single `return` at the end of the function. Setting every variable to a default before the `if` makes sure each one exists, whichever branch runs.

### Combining comparisons

Comparisons are booleans, so they combine with `and`, `or`, and `not` from Chapter 6:

```python
def does_attack_hit(attack_roll, armor_class):
    return (attack_roll != 1 and attack_roll >= armor_class) or attack_roll == 20
```

Comparison operators bind tighter than `and` and `or`, so the comparisons are always evaluated first. Parentheses are still worth adding around each group to show the intent, as in `(high_gpa and high_sat_score) or is_rich`.

### Guard clauses

When a function needs several conditions to all be true, it can check each one in a nested `if`:

```python
def check(condition_1, condition_2, condition_3):
    if condition_1:
        if not condition_2:
            if condition_3 > 1:
                return True
    return False
```

Each level pushes the real work further to the right and makes it harder to follow. The alternative is to invert each condition and return early as soon as one fails. These early checks are called guard clauses:

```python
def should_serve_drinks(age, on_break, time):
    if age < 21:
        return False
    if on_break:
        return False
    if time < 5 or time > 10:
        return False
    return True
```

Each guard handles one failure and gets out of the way. If the function gets past all of them, every condition passed. When inverting a condition, the boundary flips too: "between 5 and 10, inclusive" becomes "less than 5 or greater than 10." The same logic as a single expression is `return age >= 21 and not on_break and 5 <= time <= 10`.

Guard clauses also remove the need for `else` after a `return`. Once a branch returns, the code below it only runs when that branch did not:

```python
def check_mount_rental(time_used, time_purchased):
    if time_used >= time_purchased:
        return "overtime charged"
    return "no charges yet"
```

### Truthiness

An `if` does not need a comparison. A boolean variable works on its own, and `if is_big:` is preferred over `if is_big == True:`, which is redundant.

More generally, `if` accepts any value and checks whether it is truthy or falsy. These values are falsy:

- `False` and `None`
- Zero of any number type: `0`, `0.0`
- Empty collections: `""`, `[]`, `{}`, `()`, `set()`

Everything else is truthy, including `"0"`, `[0]`, and `-1`. `bool(value)` shows how a value would be treated. This is why `if not name:` is a common way to check for an empty string.

### Conditional expressions

For choosing between two values, Python has a one-line form, often called a ternary:

```python
status = "dead" if hp <= 0 else "alive"
```

It reads as "this value if the condition is true, otherwise that value." It is an expression, so it can be returned or passed as an argument. It is best kept for short, simple choices. Anything with more than two outcomes reads better as a full `if` statement.

### `==` versus `is`

`==` checks whether two values are equal. `is` checks whether two names point to the exact same object in memory:

```python
a = [1, 2]
b = [1, 2]
a == b       # True, same contents
a is b       # False, two separate lists
```

Use `==` for comparing values. Use `is` only for singletons, mainly `None`: `if item is None:` is the standard style.

## Analogy

Continuing the kitchen from Chapters 1 to 6: **comparisons and conditionals are the decisions the cooks make at every station.**

- A comparison is reading the thermometer. "Is the oil at 180 degrees or more?" has a yes or no answer, and the cook can write that answer down for later.
- An `if` is a line in the recipe that only applies sometimes: "if the dough is sticky, add flour." Every cook moves on to the next step either way, unless the line says to stop.
- `return` inside an `if` is sending the plate out early. Once it has left the kitchen, the remaining steps do not happen.
- `if`, `elif`, `else` is checking doneness with a probe. Above 70 degrees is well done, otherwise above 60 is medium, otherwise it is rare. The cook stops at the first match, so the order of the checks matters.
- Guard clauses are the head chef screening an order before it starts. Ingredient out of stock? Send it back. Kitchen closed? Send it back. Only an order that passes every check gets cooked, and nobody has to keep the whole checklist in mind at once.
- Truthiness is a glance at the shelf. An empty jar counts as "no," without anyone counting what is inside.
- `==` versus `is` is two pots of the same soup versus the same pot. They taste equal, but stirring one does not stir the other.

## Example

```python
# Comparisons produce booleans
print(5 < 6, 5 > 6, 5 >= 6, 5 <= 6, 5 == 6, 5 != 6)   # True False False True False True

is_bigger = 5 > 4
print(is_bigger, type(is_bigger))       # True <class 'bool'>

def player_1_wins(player_1_score, player_2_score):
    return player_1_score > player_2_score

print(player_1_wins(10, 7))             # True

def can_withstand_blow(armor, damage):
    return armor >= damage

print(can_withstand_blow(5, 5))         # True

# Comparing different types
print(1 == 1.0)                         # True
print("5" == 5)                         # False
print("apple" < "banana")               # True
print("Zebra" < "apple")                # True, uppercase sorts first
print("10" < "9")                       # True, compared character by character

# Chained comparisons
time = 7
print(5 <= time <= 10)                  # True
print(1 < 3 > 2)                        # True, same as 1 < 3 and 3 > 2

# If statements and early return
def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
        return
    print("Ganondorf is unalive!")

show_status(10)                         # Ganondorf is alive!
show_status(0)                          # Ganondorf is unalive!

def print_status(player_health):
    if player_health <= 0:
        print("dead")
    print("status check complete")

print_status(0)                         # dead, then status check complete
print_status(5)                         # status check complete

# if, elif, else
def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"

print(player_status(-1), player_status(5), player_status(6))   # dead injured healthy

# elif order matters: the first true branch wins
def player_status_wrong(health):
    if health <= 5:
        return "injured"
    elif health <= 0:
        return "dead"                   # never reached
    return "healthy"

print(player_status_wrong(-1))          # injured

# Combining comparisons
def does_attack_hit(attack_roll, armor_class):
    return (attack_roll != 1 and attack_roll >= armor_class) or attack_roll == 20

print(does_attack_hit(1, 1), does_attack_hit(15, 12), does_attack_hit(20, 25))   # False True True

is_tall, is_bulky, is_lean, is_short = True, True, False, False
print((is_tall and is_bulky) or (is_lean and is_short))   # True

# Guard clauses
def should_serve_drinks(age, on_break, time):
    if age < 21:
        return False
    if on_break:
        return False
    if time < 5 or time > 10:
        return False
    return True

print(should_serve_drinks(21, False, 5), should_serve_drinks(30, False, 11))   # True False

def should_serve_drinks_short(age, on_break, time):
    return age >= 21 and not on_break and 5 <= time <= 10

print(should_serve_drinks_short(21, False, 10))   # True

def check_mount_rental(time_used, time_purchased):
    if time_used >= time_purchased:
        return "overtime charged"
    return "no charges yet"

print(check_mount_rental(60, 60))       # overtime charged

# Setting a variable in each branch
def get_advantage(player_power, enemy_defense):
    advantage = False
    disadvantage = False
    evenly_matched = False
    if player_power > enemy_defense:
        advantage = True
    elif player_power == enemy_defense:
        evenly_matched = True
    else:
        disadvantage = True
    return advantage, disadvantage, evenly_matched

print(get_advantage(5, 5))              # (False, False, True)

# Truthiness
for value in [0, 0.0, "", [], {}, None, False]:
    if not value:
        print(repr(value), "is falsy")  # prints a line for every value
print(bool("0"), bool([0]), bool(-1))   # True True True

is_big = True
if is_big:
    print("big")                        # big

# Conditional expression
hp = 0
print("dead" if hp <= 0 else "alive")   # dead

# == versus is
a = [1, 2]
b = [1, 2]
print(a == b, a is b)                   # True False
item = None
print(item is None)                     # True
```

Common errors:

```python
if 5 > 4                                # SyntaxError: expected ':'
    print("yes")

else:                                   # SyntaxError: invalid syntax, no if before it
    pass

if True:
print("yes")                            # IndentationError: expected an indented block after 'if' statement on line 1

if x = 5:                               # SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
    pass

if x > 3 && x < 9:                      # SyntaxError: invalid syntax, use and
    pass

"5" < 5                                 # TypeError: '<' not supported between instances of 'str' and 'int'
None < 1                                # TypeError: '<' not supported between instances of 'NoneType' and 'int'
```

## In other languages

| | Python | JavaScript | Go | Bash |
|---|---|---|---|---|
| Equality | `==` | `===`. `==` converts types first, so `"5" == 5` is `true` | `==`, only between the same type | `-eq` for numbers, `==` for strings in `[[ ]]` |
| Ordering | `< > <= >=` | `< > <= >=` | `< > <= >=` | `-lt -gt -le -ge` in `[ ]`, or `< >` in `(( ))` |
| `if` syntax | `if x > 5:` with an indented body | `if (x > 5) { }` | `if x > 5 { }`, braces required | `if [ "$x" -gt 5 ]; then ... fi` |
| Else if | `elif` | `else if` | `else if` | `elif ...; then` |
| Range check | `5 <= t <= 10` | `5 <= t && t <= 10`. `5 <= t <= 10` runs but is wrong | `5 <= t && t <= 10`. Chaining does not compile | `(( 5 <= t && t <= 10 ))` |
| Comparing `int` with `float` | `1 == 1.0` is `True` | One number type, so `1 === 1.0` is `true` | Compile error: mismatched types | Integers only |
| Condition must be a boolean | No, any value is truthy or falsy | No, any value is truthy or falsy | Yes, `if x {}` with an `int` does not compile | The condition is a command, and exit status `0` means true |
| Empty list is | Falsy | Truthy: `Boolean([])` is `true` | Not allowed as a condition | Not applicable |
| Ternary | `a if cond else b` | `cond ? a : b` | None, use `if` | `[[ cond ]] && a \|\| b`, with caveats |
| Identity | `is` | `===` on objects | `==` on pointers | Not applicable |

Two ideas carry over to every language:

1. **Know what your language does with mixed types.** Python refuses to order unrelated types, JavaScript silently converts them, and Go refuses to even compile. When values come from user input or a file, they are usually strings, and comparing them as strings gives the wrong order for numbers. Convert first, then compare.
2. **Prefer guard clauses to deep nesting.** Returning early on each failure case keeps the main path of a function flat and readable. This is standard style in Go in particular, where errors are checked and returned immediately after each call.

## Interview framing

1. What is the difference between `==` and `is`?
2. What values are falsy in Python, and when is `if x:` the wrong check?
3. What is a guard clause, and why use one instead of nested `if` statements?
4. How does Python evaluate an `if`, `elif`, `else` chain?
5. What does `1 < x < 10` do in Python, and would it work in JavaScript?

## My answer

**1. `==` versus `is`**

"`==` checks equality of value. It calls the object's `__eq__` method, so two separate lists with the same contents are equal. `is` checks identity: whether both names refer to the very same object. I use `is` for singletons, almost always `None`, as in `if result is None`. Using `is` to compare numbers or strings is a bug, because whether two equal values share one object is an implementation detail. It can appear to work for small integers and then fail for larger ones."

**2. Falsy values**

"`False`, `None`, zero of any numeric type, and empty collections such as `""`, `[]`, `{}`, and `set()` are falsy. Everything else is truthy, including the string `"0"`. `if x:` is the idiomatic check for an empty collection or a missing value. It is the wrong check when zero or an empty string is a valid value. For example, `if not quantity:` treats a quantity of `0` the same as a missing one. In that case I check `if quantity is None:` explicitly."

**3. Guard clauses**

"A guard clause checks a failure condition at the top of a function and returns or raises immediately. Instead of nesting the happy path inside several `if` blocks, each guard handles one case and exits, so the main logic sits at the lowest indentation level. It is easier to read, because each condition can be understood on its own, and easier to change, because adding a new rule is one more guard rather than another level of nesting. It also removes the need for `else` after a `return`."

**4. `if`, `elif`, `else`**

"The conditions are evaluated from top to bottom, and only the body of the first true one runs. The remaining conditions are not even evaluated. If none are true, the `else` runs, if there is one. Because the first match wins, overlapping conditions have to be ordered from most specific to most general. Checking `health <= 5` before `health <= 0` would make the `dead` branch unreachable."

**5. Chained comparisons**

"In Python, `1 < x < 10` means `1 < x and x < 10`, with `x` evaluated only once, so it is a clean range check. JavaScript does not chain. It evaluates `1 < x` first, gets a boolean, and then compares that boolean to `10`, converting it to `0` or `1`. So `1 < x < 10` is always `true` in JavaScript, and `3 > 2 > 1` is `false`. Go rejects it at compile time. Outside Python, I write the two comparisons joined with `&&`."

**Points to recall**

- Comparisons return a `bool`. Return it directly instead of wrapping it in `if ... return True`.
- `=` assigns, `==` compares, `is` checks identity. Use `is` only for `None`.
- Strings compare character by character: `"10" < "9"` is `True`.
- Ordering unrelated types, such as `"5" < 5`, raises a `TypeError`.
- `5 <= t <= 10` is a chained comparison and is the preferred range check.
- `if` needs a colon and an indented body.
- Only the first true branch of an `if`, `elif`, `else` chain runs. Order specific checks first.
- `return` inside an `if` exits the function early, and makes a following `else` unnecessary.
- Guard clauses invert the conditions and return early, which avoids nesting.
- Falsy values: `False`, `None`, `0`, `0.0`, and empty collections.
- `if is_big:` is preferred over `if is_big == True:`.
- `a if cond else b` chooses between two values in one expression.

## Follow-up gotchas

**What does `x == 1 or 2` do?**
It does not check whether `x` is 1 or 2. It is read as `(x == 1) or 2`, and because `2` is truthy, the whole expression is always truthy: when `x` is `3`, it returns `2`. Write `x == 1 or x == 2`, or better, `x in (1, 2)`.

**Is `True == 1`?**
Yes. `bool` is a subclass of `int`, with `True` equal to `1` and `False` equal to `0`. So `True + True` is `2`, and `sum()` over a list of booleans counts the true ones. This is also why `if x == True:` behaves differently from `if x:` for values like `2`: `2 == True` is `False`, but `2` is truthy.

**Why is `float("nan") == float("nan")` false?**
NaN, "not a number," is defined by the IEEE 754 standard as unequal to everything, including itself. This is the same in every language that uses standard floats. Check for it with `math.isnan(x)` instead of `==`.

**Can `1 < 3 > 2` be written in Python?**
Yes, and it is `True`, because it means `1 < 3 and 3 > 2`. A chain does not have to go in one direction, and it does not compare the two ends to each other. It is legal but confusing, so chains are best kept to the range form `low <= x <= high`.

**Is a full `else` ever better than a guard clause?**
Yes, when both branches are equally important outcomes rather than one main path and one exceptional case. Setting a different value in each branch, as with advantage, disadvantage, and evenly matched, reads naturally as `if`, `elif`, `else`. Guard clauses are for filtering out failures before the real work starts.

**Why does `[ 10 > 9 ]` in Bash not compare numbers?**
Inside single brackets, `>` is output redirection, not a comparison. The command runs `[ 10 ]`, which is true because the string is not empty, and creates a file named `9`. Use `-gt` in `[ ]`, or `(( 10 > 9 ))` for arithmetic. Each language has its own comparison syntax, and Bash is the one where getting it wrong fails silently.
