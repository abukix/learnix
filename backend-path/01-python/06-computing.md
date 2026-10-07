# 06: Computing

Source: boot.dev Learn Python, Chapter 6, Lessons 1 to 14.

## What it is

### Integers and floats

Python has two main number types:

- **`int`**: whole numbers, positive or negative, such as `3`, `-3`, and `0`.
- **`float`**: numbers with a fractional part, such as `5.5` or `-0.25`. Any number written with a decimal point is a float, even `5.0`.

The basic arithmetic operators work as expected:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `2 + 1` | `3` |
| `-` | Subtraction | `2 - 1` | `1` |
| `*` | Multiplication | `2 * 2` | `4` |
| `/` | Division | `3 / 2` | `1.5` |
| `//` | Floor division | `8 // 3` | `2` |
| `%` | Modulo (remainder) | `8 % 3` | `2` |
| `**` | Exponent | `3 ** 2` | `9` |

Two rules decide the type of the result:

1. `/` always returns a float, even when the division is exact. `4 / 2` is `2.0`, not `2`.
2. Mixing an `int` and a `float` gives a `float`. `2 + 1.0` is `3.0`.

Python integers have no size limit. `2 ** 100` gives the exact 31 digit answer instead of overflowing, which most languages cannot do without a special type.

### Floor division and modulo

Floor division, `//`, divides and then rounds down to the nearest whole number. "Down" means towards negative infinity, not towards zero:

- `8 // 3` is `2`, rounded down from 2.666.
- `-7 // 3` is `-3`, rounded down from -2.333. It is not `-2`.

When both operands are integers, the result is an integer. If either is a float, the result is a float with nothing after the decimal point: `8.0 // 3` is `2.0`.

Modulo, `%`, gives the remainder that floor division leaves behind. The two always fit together: `(a // b) * b + (a % b)` equals `a`. They are commonly used together to split a quantity into units, such as turning 125 seconds into 2 minutes (`125 // 60`) and 5 seconds (`125 % 60`). The built-in `divmod(a, b)` returns both at once as a tuple.

### Exponents

`**` raises a number to a power: `3 ** 2` is "three squared," which is `9`. Many languages need a math library for this, but Python has it built in.

Outside of code, exponents are often written with a caret, as in `5^3`. In Python, `^` is not an exponent. It is the bitwise XOR operator, covered below, so `5 ^ 3` is `6`, not `125`. This is a common bug for people coming from math or spreadsheets.

`**` binds tighter than a leading minus sign, so `-2 ** 2` is `-(2 ** 2)`, which is `-4`. Use parentheses for `(-2) ** 2`.

### Changing a variable in place

A common pattern is to update a variable based on its current value:

```python
player_score = 4
player_score = player_score + 1
```

As a math equation, this makes no sense. As code, it reads: "calculate `player_score + 1` using the current value, then assign the result to `player_score`." The right-hand side is always evaluated first, before the assignment happens.

Because this pattern is so common, Python has shorter in-place operators, also called augmented assignment:

| Operator | Same as |
|---|---|
| `x += 1` | `x = x + 1` |
| `x -= 1` | `x = x - 1` |
| `x *= 2` | `x = x * 2` |
| `x /= 2` | `x = x / 2`, which makes `x` a float |
| `x //= 2` | `x = x // 2` |
| `x %= 2` | `x = x % 2` |
| `x **= 2` | `x = x ** 2` |

Python does not have the `++` and `--` operators from JavaScript and Go. `x++` is a `SyntaxError`, and `x += 1` is used instead.

In-place operators are statements, not expressions, so they do not produce a value. `return health -= damage` is a `SyntaxError`. Update the variable on one line and return it on the next.

### Writing large and small numbers

**Scientific notation** writes a number as a value times a power of 10, using `e` or `E`. The number after the `e` says how many places to move the decimal point: right if positive, left if negative.

- `16e3` is `16000.0`
- `7.1e-2` is `0.071`
- `1.024e18` is `1024000000000000000.0`

A number written in scientific notation is always a float, even when it is a whole number.

**Underscores** can be placed between digits to make long numbers easier to read. Python ignores them: `16_000_000` is exactly `16000000`. Commas cannot be used for this, because a comma in Python separates values. `calculate_dps(8,000,000, 45)` passes four arguments, not two, and raises a `TypeError`.

### Float precision

Floats are stored in binary, and most decimal fractions, such as `0.1`, cannot be represented exactly in binary, just as 1/3 cannot be written exactly in decimal. The small errors can show up in results:

```python
0.1 + 0.2           # 0.30000000000000004
0.1 + 0.2 == 0.3    # False
```

This is not a Python bug. Every language that uses standard floats behaves the same way. Compare floats with `math.isclose(a, b)` instead of `==`. For money, use whole numbers of the smallest unit, such as cents, or the `decimal` module.

### Logical operators

Logical operators combine boolean values, `True` and `False`:

- **`and`** is `True` only if both sides are `True`.
- **`or`** is `True` if at least one side is `True`.
- **`not`** reverses a value: `not True` is `False`.

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

Parentheses group expressions, and the innermost group is evaluated first. `(True or False) and False` becomes `True and False`, which is `False`.

Without parentheses, `not` is applied first, then `and`, then `or`. So `True or True and False` is `True or (True and False)`, which is `True`. When an expression mixes `and` and `or`, parentheses make the intent clear.

Python spells these operators as words. `&&`, `||`, and `!` from other languages are syntax errors in Python.

### Short-circuit evaluation

`and` and `or` stop as soon as the answer is known:

- `False and anything` is `False`, so the right side is never evaluated.
- `True or anything` is `True`, so the right side is never evaluated.

This matters when the right side calls a function or could fail. `count > 0 and total / count > 10` never divides by zero, because the division only runs if `count > 0` is true.

Strictly, `and` and `or` do not return `True` or `False`. They return one of the two operands: `or` returns the first truthy value (or the last value), and `and` returns the first falsy value (or the last value). So `0 or "default"` is `"default"`, and `5 and 7` is `7`. With actual booleans, this is the same as the truth table above.

### Binary numbers

Binary is base 2. It works like the everyday base 10 system, but with two digits, `0` and `1`, instead of ten. In base 10, each place is worth ten times the place to its right (ones, tens, hundreds). In binary, each place is worth twice the place to its right:

| Eights | Fours | Twos | Ones | Value |
|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 4 + 1 = 5 |
| 0 | 1 | 1 | 1 | 4 + 2 + 1 = 7 |
| 1 | 0 | 0 | 1 | 8 + 1 = 9 |

Each binary digit is called a bit. Leading zeros do not change the value. They are only added to line numbers up.

Python can work with binary in several ways:

- **Binary literals** use the `0b` prefix: `0b0101` is the integer `5`. Without the prefix, `101` is one hundred and one.
- **`bin(n)`** turns an integer into a binary string: `bin(5)` is `"0b101"`.
- **`int(s, 2)`** turns a binary string into an integer. The second argument is the base: `int("10010", 2)` is `18`.
- **`f"{n:04b}"`** formats an integer as binary padded to 4 digits: `"0101"`.

The same works for other bases: `0x` for hexadecimal (base 16) and `0o` for octal (base 8), with `int(s, 16)` and `int(s, 8)` to convert strings.

A binary literal is not a different type. `0b0101` and `5` are the same `int`, just written differently.

### Bitwise operators

Bitwise operators apply logic to each bit of two integers, column by column. A `1` acts like `True` and a `0` like `False`.

**`&` (AND)** gives `1` only where both numbers have a `1`:

```
  0101   (5)
& 0111   (7)
= 0101   (5)
```

**`|` (OR)** gives `1` wherever either number has a `1`:

```
  0101   (5)
| 0010   (2)
= 0111   (7)
```

Python has a few more, beyond what the lessons cover:

| Operator | Name | Example | Result |
|---|---|---|---|
| `&` | AND | `5 & 7` | `5` |
| `\|` | OR | `5 \| 2` | `7` |
| `^` | XOR: `1` where exactly one has a `1` | `5 ^ 7` | `2` |
| `~` | NOT: flips every bit | `~5` | `-6` |
| `<<` | Shift left: moves bits left, multiplying by 2 per place | `1 << 3` | `8` |
| `>>` | Shift right: moves bits right, floor dividing by 2 per place | `0b1000 >> 2` | `2` |

`and` and `&` are different operators. `and` works on whole values and returns one of them, so `5 and 2` is `2`. `&` compares bit by bit, so `5 & 2` is `0`.

### Bit flags

A common use for bitwise operators is storing several yes or no settings in one integer, called bit flags. Each permission gets its own bit:

```python
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001
```

A user with the review and edit permissions has `0b0101`. The common operations are:

- **Check** a permission with `&`: `user & can_review_guild` keeps only that bit. If the result equals `can_review_guild`, the user has it.
- **Combine** permissions with `|`: `a | b | c` has every bit that any of them has. This is how a guild gets the union of all its members' permissions.
- **Grant** a permission with `|=`: `user |= can_delete_guild`.
- **Remove** a permission with `&= ~`: `user &= ~can_delete_guild` turns that bit off and leaves the rest.
- **Toggle** a permission with `^=`.

One integer is smaller and faster to compare than a list of permission names. Unix file permissions (`chmod 755`) and many network protocols use the same idea. In application code, Python's `enum.Flag` gives each bit a readable name.

## Analogy

Continuing the kitchen from Chapters 1 to 5: **computing is the kitchen's measuring and bookkeeping.**

- Integers are whole items: 3 eggs, 12 plates. Floats are measured amounts: 1.5 cups of flour.
- `/` is splitting a batch evenly. Even when it divides cleanly, the answer is written as an amount on the scale, so 4 cups split 2 ways is 2.0 cups.
- `//` and `%` are filling boxes of 6: 14 cookies make 2 full boxes (`14 // 6`) with 2 cookies left over (`14 % 6`).
- `**` is scaling a recipe that doubles at every step. `2 ** 3` is doubling three times.
- `+=` is updating the stock count on the whiteboard: read the current number, add the delivery, write the new number over the old one.
- Scientific notation and underscores are the way the supplier writes big orders, so nobody miscounts the zeros.
- Float precision is the kitchen scale that is off by a hair. Two weights that should match can differ in the last digit, so you check that they are close enough, not identical.
- `and`, `or`, and `not` are the rules on the order ticket: "gluten free and vegetarian," "rice or noodles," "not spicy." Once a ticket fails the first `and` condition, nobody checks the rest.
- Bit flags are the row of switches by the door: lights, fans, oven hood, music. One look at the panel shows every setting at once. `&` checks one switch, `|` flips switches on, and `&= ~` turns one off.

## Example

```python
# Division always gives a float
print(3 / 2)                            # 1.5
print(4 / 2)                            # 2.0
print(2 + 1.0)                          # 3.0

def calculate_damage(sword, arrow, fireball, lightning):
    total_damage = sword + arrow + fireball + lightning
    average_damage = total_damage / 4
    return total_damage, average_damage

print(calculate_damage(10, 4, 20, 6))   # (40, 10.0)

# Floor division rounds down, towards negative infinity
print(8 // 3, 8 % 3)                    # 2 2
print(-7 // 3, -7 % 3)                  # -3 2
print(int(-7 / 3))                      # -2, int() rounds towards zero instead
print(divmod(125, 60))                  # (2, 5): 2 minutes, 5 seconds

# Exponents
print(3 ** 2)                           # 9
print(2 ** -1)                          # 0.5
print(-2 ** 2, (-2) ** 2)               # -4 4
print(5 ^ 3)                            # 6, XOR, not an exponent
print(2 ** 100)                         # 1267650600228229401496703205376

# Changing in place
star_rating = 4
star_rating += 1
print(star_rating)                      # 5
star_rating -= 1
print(star_rating)                      # 4
star_rating *= 2
print(star_rating)                      # 8
star_rating /= 2
print(star_rating)                      # 4.0

def get_hurt(current_health, damage):
    current_health -= damage
    return current_health

print(get_hurt(100, 30))                # 70

# Scientific notation and underscores
print(16e3)                             # 16000.0
print(7.1e-2)                           # 0.071
print(1.024e18)                         # 1.024e+18
print(16_000_000)                       # 16000000
print(f"{16000000:,}")                  # 16,000,000

def calculate_dps(damage, time):
    return damage / time

print(calculate_dps(8_000_000, 45))     # 177777.77777777778

# Float precision
import math

print(0.1 + 0.2)                        # 0.30000000000000004
print(0.1 + 0.2 == 0.3)                 # False
print(math.isclose(0.1 + 0.2, 0.3))     # True

# Logical operators
print(True and False, True or False)    # False True
print((True or False) and False)        # False
print(not True, not False)              # False True
print(True or True and False)           # True, because and runs before or

# Short circuit: the right side is skipped when the answer is already known
def loud():
    print("called")
    return True

print(False and loud())                 # False, and loud() never runs
print(0 or "default")                   # default
print(5 and 7)                          # 7

# Binary
print(0b0101)                           # 5
print(bin(18))                          # 0b10010
print(f"{5:04b}")                       # 0101
print(int("10010", 2))                  # 18
print(int("ff", 16), 0xff)              # 255 255

def binary_string_to_int(a, b, c):
    return int(a, 2), int(b, 2), int(c, 2)

print(binary_string_to_int("100", "101", "110"))   # (4, 5, 6)

# Bitwise operators
print(5 & 7, 5 & 2)                     # 5 0
print(5 | 7, 5 | 2)                     # 7 7
print(5 ^ 7, ~5)                        # 2 -6
print(1 << 3, 0b1000 >> 2)              # 8 2
print(5 and 2, 5 & 2)                   # 2 0

# Bit flags
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

user_permissions = 0b0101
print(user_permissions & can_review_guild == can_review_guild)   # True
print(user_permissions & can_create_guild == can_create_guild)   # False

def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    return glorfindel | galadriel | elendil | elrond

print(bin(calculate_guild_perms(0b1000, 0b0100, 0b0000, 0b0001)))   # 0b1101

perms = 0b0000
perms |= can_edit_guild                 # grant
perms |= can_delete_guild
print(f"{perms:04b}")                   # 0011
perms &= ~can_delete_guild              # remove
print(f"{perms:04b}")                   # 0001
perms ^= can_create_guild               # toggle
print(f"{perms:04b}")                   # 1001
```

Common errors:

```python
x = 5
x++                                     # SyntaxError: invalid syntax

def get_hurt(current_health, damage):
    return current_health -= damage     # SyntaxError: invalid syntax

calculate_dps(8,000,000, 45)            # TypeError: calculate_dps() takes 2 positional arguments but 4 were given
print(1,000,000)                        # prints 1 0 0, three separate values

print(1 / 0)                            # ZeroDivisionError: division by zero
int("102", 2)                           # ValueError: invalid literal for int() with base 2: '102'
print(010)                              # SyntaxError: leading zeros in decimal integer literals are not permitted
```

## In other languages

| | Python | JavaScript | Go | Bash |
|---|---|---|---|---|
| Number types | `int` (unlimited size) and `float` | One `number` type (a float), plus `BigInt` | Sized types: `int`, `int64`, `float64`, and others | Integers only in `$(( ))`. Decimals need a tool like `bc` |
| `3 / 2` | `1.5` | `1.5` | `1` for integers, `1.5` for floats | `$((3 / 2))` is `1` |
| Integer division | `//`, rounds down: `-7 // 3` is `-3` | `Math.floor(-7 / 3)` is `-3`, `Math.trunc` is `-2` | `/` on ints, rounds towards zero: `-7 / 3` is `-2` | `/`, rounds towards zero: `-2` |
| `-7 % 3` | `2` | `-1` | `-1` | `-1` |
| Exponent | `3 ** 2` | `3 ** 2` | `math.Pow(3, 2)`, floats only | `$((3 ** 2))` |
| `^` means | XOR | XOR | XOR, and bitwise NOT as `^x` | XOR |
| Increment | `x += 1` | `x++` or `x += 1` | `x++` (a statement only) or `x += 1` | `((x++))` or `((x += 1))` |
| Digit separators | `1_000_000` | `1_000_000` | `1_000_000` | Not supported |
| Binary literal | `0b0101` | `0b0101` | `0b0101` | `$((2#0101))` |
| Parse a binary string | `int("101", 2)` | `parseInt("101", 2)` | `strconv.ParseInt("101", 2, 64)` | `$((2#101))` |
| Logical operators | `and`, `or`, `not` | `&&`, `\|\|`, `!` | `&&`, `\|\|`, `!` | `&&`, `\|\|`, `!` between commands |
| Bitwise operators | `& \| ^ ~ << >>` | Same, but on 32 bit integers only | Same, plus `&^` (AND NOT). `^x` is NOT | Same, inside `$(( ))` |
| `0.1 + 0.2` | `0.30000000000000004` | `0.30000000000000004` | `0.3` for constants, `0.30000000000000004` for variables | Not possible without `bc` |

Two ideas carry over to every language:

1. **Integer division and remainders differ with negative numbers.** Python rounds down and gives the remainder the sign of the divisor. JavaScript, Go, and Bash round towards zero and give the remainder the sign of the dividend. Code that only ever sees positive numbers behaves the same everywhere. Code that handles negatives, such as wrapping around a circular index, needs checking in each language.
2. **Floats are approximate everywhere.** Every mainstream language uses the same binary floating point standard (IEEE 754), so `0.1 + 0.2` is slightly off in all of them. Never compare floats with `==`, and never use them for money.

## Interview framing

1. What is the difference between `/` and `//` in Python?
2. Why is `0.1 + 0.2 == 0.3` false?
3. What is the difference between `and` and `&`?
4. What is short-circuit evaluation, and how can it be useful?
5. How would you store and check a set of permissions using bits?
6. How do you convert between binary strings and integers in Python?

## My answer

**1. `/` versus `//`**

"`/` is true division and always returns a float, so `4 / 2` is `2.0`. `//` is floor division: it divides and rounds down towards negative infinity, so `7 // 2` is `3` and `-7 // 2` is `-4`. With two integers, `//` returns an integer. Its partner is `%`, which returns the remainder, and they always satisfy `(a // b) * b + a % b == a`. Rounding down is different from Go, JavaScript, and C, which round towards zero for integer division, so negative numbers give different results."

**2. Why `0.1 + 0.2 != 0.3`**

"Floats are stored in binary, and `0.1` and `0.2` cannot be represented exactly in binary, just as one third cannot be written exactly in decimal. The tiny rounding errors add up to `0.30000000000000004`. Every language that follows the IEEE 754 standard does this. To compare floats, I use `math.isclose` or check that the difference is smaller than a tolerance. For money, I store whole cents as integers or use the `decimal` module."

**3. `and` versus `&`**

"`and` is a logical operator. It looks at whether whole values are truthy, short-circuits, and returns one of the operands, so `5 and 2` is `2`. `&` is a bitwise operator. It compares two integers bit by bit and returns a new integer, so `5 & 2` is `0`, because `0101` and `0010` share no bits. `&` is used for bit masks and flags. It is also used for element-wise operations in libraries like NumPy and pandas, where `and` does not work."

**4. Short-circuit evaluation**

"`and` and `or` evaluate from left to right and stop once the result is decided. If the left side of `and` is falsy, the right side never runs. If the left side of `or` is truthy, the right side never runs. This works as a guard: `user is not None and user.is_admin` never touches `user.is_admin` when `user` is `None`. It also allows defaults, such as `name = input_name or "Guest"`, but that pattern treats every falsy value, including `0` and an empty string, as missing, which is not always what you want."

**5. Permissions as bits**

"Give each permission its own bit, such as `CREATE = 0b1000` and `EDIT = 0b0001`, and store a user's permissions as one integer. To check a permission, I use `perms & EDIT == EDIT`. To grant one, `perms |= EDIT`. To remove one, `perms &= ~EDIT`. To combine several users' permissions, I OR them together. It is compact, fast, and easy to store in a single database column. In Python application code, I would use `enum.Flag`, which gives the same behavior with readable names."

**6. Binary conversion**

"`int(s, 2)` parses a binary string into an integer, and it accepts any base from 2 to 36, so `int("ff", 16)` is `255`. In the other direction, `bin(n)` gives a string with a `0b` prefix, and `format(n, "b")` or `f"{n:08b}"` gives just the digits, optionally padded. In source code, the literal `0b101` is just another way to write the integer `5`."

**Points to recall**

- `/` always returns a float. `//` rounds down. `%` is the remainder.
- Mixing `int` and `float` gives a `float`.
- Python integers have no size limit.
- `**` is the exponent operator. `^` is XOR.
- Python has `+=` and similar operators, but no `++`. They are statements, so they cannot be returned.
- Scientific notation such as `1e3` always makes a float. Underscores in numbers are ignored.
- Floats are approximate: compare with `math.isclose`, not `==`.
- `not` runs before `and`, which runs before `or`. Use parentheses when mixing them.
- `and` and `or` short-circuit and return one of their operands.
- `0b` writes binary, `bin()` and `int(s, 2)` convert to and from strings.
- `&` checks bits, `|` combines them, `&= ~` clears one.

## Follow-up gotchas

**Why is `-7 // 3` equal to `-3` and not `-2`?**
Floor division rounds towards negative infinity, and -2.333 rounded down is -3. Python does this so that `%` always has the same sign as the divisor, which makes `n % 7` always land between 0 and 6, even for negative `n`. That is convenient for wrapping around indexes or days of the week. To round towards zero instead, use `int(-7 / 3)` or `math.trunc`.

**Why is `~5` equal to `-6`?**
Python integers behave as if they used two's complement with an unlimited number of bits, and in two's complement, flipping every bit of `n` gives `-n - 1`. That is why `~` is mainly used together with `&` to clear bits, as in `perms & ~FLAG`, rather than on its own.

**Does `user & FLAG == FLAG` need parentheses?**
Not in Python. Bitwise operators bind tighter than comparisons, so it is read as `(user & FLAG) == FLAG`. In JavaScript and C, `==` binds tighter than `&`, so the same expression means `user & (FLAG == FLAG)` and gives the wrong answer: in JavaScript, `5 & 4 == 4` is `1`. Adding the parentheses is a good habit in any language.

**What does `round(2.5)` return?**
`2`. Python rounds exact halves to the nearest even number, which is called banker's rounding, so `round(2.5)` is `2` and `round(3.5)` is `4`. This avoids a bias towards rounding up when rounding many values. Rounding half up needs the `decimal` module.

**Is `1e3` the same as `1000`?**
Equal, but not the same type. `1e3 == 1000` is `True`, but `1e3` is the float `1000.0`. That matters where an integer is required, such as `range(1e3)` or indexing a list, which raise a `TypeError`. Use `1_000` or `10 ** 3` when an integer is needed.

**Why can't `-=` be used in a `return` statement?**
In-place operators are statements: they update a variable but do not produce a value, so there is nothing to return. Python 3.8 added the walrus operator, `:=`, which assigns and returns a value inside an expression, but it does not support `+=` style operators. Updating on one line and returning on the next is the clear way to write it.
