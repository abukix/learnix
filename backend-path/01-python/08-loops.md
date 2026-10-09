# 08: Loops

Source: boot.dev Learn Python, Chapter 8, Lessons 1 to 15.

## What it is

### Why loops

A loop runs the same block of code many times without writing it out each time. Printing the numbers 0 to 9 by hand takes ten `print` calls. A loop does it in two lines, and the same two lines work for a thousand or a million numbers.

Python has two kinds of loop:

- **`for`** goes through a sequence of values, one at a time. Use it when the number of iterations is known up front, such as "every number from 0 to 99."
- **`while`** keeps going as long as a condition is true. Use it when the loop should stop because something changed, such as "until the health is full."

### For loops and `range`

```python
for i in range(0, 10):
    print(i)
```

`i` is the loop variable. On each iteration it takes the next value from `range(0, 10)`, and the indented body runs once with that value. Step by step:

1. Start with `i` equal to `0`.
2. If `i` is `10` or more, exit the loop.
3. Run the body: print `i`.
4. Add 1 to `i`.
5. Go back to step 2.

The result is the numbers 0 to 9.

`range(start, stop)` includes `start` and excludes `stop`. `range(0, 10)` has ten numbers, 0 through 9, and `range(0, 1000)` stops at 999. This "inclusive start, exclusive stop" rule is common across programming, and it means `stop - start` is always the number of values.

`range` takes one, two, or three arguments:

| Call | Values |
|---|---|
| `range(5)` | `0, 1, 2, 3, 4`. Start defaults to `0` |
| `range(5, 10)` | `5, 6, 7, 8, 9` |
| `range(0, 10, 2)` | `0, 2, 4, 6, 8`. The third argument is the step |
| `range(3, 0, -1)` | `3, 2, 1`. A negative step counts down |
| `range(10, 0)` | Nothing. The start is already past the stop, so the loop body never runs |

To count down, the step must be negative and `start` must be greater than `stop`. The stop is still excluded: `range(5, 2, -1)` gives `5, 4, 3`.

All three arguments must be integers. `range(0, 1.5)` is a `TypeError`, and a step of `0` is a `ValueError`.

### Whitespace matters

The body of a loop works the same way as the body of an `if` or a function:

- The `for` or `while` line ends with a colon.
- Every line of the body is indented by the same amount. The convention is 4 spaces, and most editors insert 4 spaces when Tab is pressed.
- The first line back at the outer level is no longer part of the loop.

A missing colon is a `SyntaxError`, a missing indent is an `IndentationError`, and a body line with a different indent from the one above it is also an `IndentationError`.

### The accumulator pattern

A very common use of a loop is to build up a result. Create a variable before the loop, update it in the body, and use it after the loop:

```python
def sum_of_numbers(n):
    total = 0
    for i in range(0, n):
        total += i
    return total
```

The in-place operators from Chapter 6, `+=` and `-=`, do the updating. Three details are easy to get wrong:

- **Initialize before the loop.** Setting `total = 0` inside the body resets it on every iteration.
- **Add the loop variable, not a constant.** `total += 1` counts the iterations. `total += i` adds up the values.
- **Return after the loop.** A `return` inside the body exits the function on the first iteration.

Picking the right `range` often removes the need for an `if`. To add up the odd numbers below `end`, start at `1` and step by `2`: `range(1, end, 2)`. That only visits odd numbers, so there is nothing to filter.

The same pattern works for running totals that depend on the loop variable. Total experience at a given level, where reaching the next level costs `level * 5`, is the sum of `current_level * 5` for every level below it:

```python
def calculate_experience_points(level):
    xp = 0
    for current_level in range(1, level):
        xp += current_level * 5
    return xp
```

Level 1 gives `range(1, 1)`, which is empty, so the result is `0`.

### While loops

A `while` loop checks its condition before every iteration and stops as soon as the condition is false:

```python
num = 0
while num < 3:
    num += 1
    print(num)    # 1, 2, 3
```

If the condition is false from the start, the body never runs, not even once.

Something in the body has to move the condition toward false. If nothing does, the loop never ends. `while True:` and `while 1:` are infinite loops on purpose, since the condition is always truthy. They are useful only when the body has a `break` to get out. An infinite loop by accident hangs the program, and Ctrl+C stops it.

A `while` condition can combine comparisons with `and` and `or`, exactly like an `if`. The loop runs only while every part of an `and` is true, so it stops as soon as any one part fails:

```python
def meditate(mana, max_mana, num_potions):
    while mana < max_mana and num_potions > 0:
        mana += 1
        num_potions -= 1
    return mana, num_potions
```

This stops when the mana is full or when the potions run out, whichever comes first.

### `continue`

`continue` skips the rest of the current iteration and goes straight to the next one:

```python
for number in range(-5, 5):
    if number < 0:
        continue
    print(f"The square root of {number} is {number**0.5}")
```

Negative numbers are skipped, and only 0 to 4 are printed. `continue` works like a guard clause from Chapter 7, but inside a loop: handle the case to skip, then get out of the way. It also saves work, because nothing below it runs for the skipped values.

A counter combined with `continue` acts on every Nth item. Add 1 to the counter each time. While it is below N, `continue`. When it reaches N, reset it to `0` and do the work.

### `break`

`break` exits the loop entirely. No more iterations run, and the program continues after the loop:

```python
for n in range(42):
    print(f"{n} * {n} = {n * n}")
    if n * n > 150:
        break
```

This would run 42 times, but stops after `13 * 13 = 169`. `break` is the usual way to stop searching once the answer is found, such as stopping at the first enchantment strong enough to block an attack.

The difference between the two:

- `continue` ends this iteration and moves to the next one.
- `break` ends the whole loop.
- `return` ends the whole function, and the loop with it.

`break` and `continue` only affect the innermost loop they are in. Using either one outside a loop is a `SyntaxError`.

### Printing inside a loop

`print` adds a newline at the end by default, so each call goes on its own line. To print a special last line, check for it inside the loop:

```python
for i in range(10, 0, -1):
    if i == 1:
        print(f"{i}...Fight!")
    else:
        print(f"{i}...")
```

To keep several values on the same line, pass `end`: `print(i, end=" ")` puts a space after each value instead of a newline.

## Analogy

Continuing the kitchen from Chapters 1 to 7: **loops are the repeated steps of a recipe.**

- A `for` loop is "crack 12 eggs." The cook knows the count before starting, and does the same motion once per egg. `range(0, 12)` is the egg carton, and the loop variable is which egg is in hand.
- `range` with a step is "fill every second tray." The step says how far to move each time, and a negative step is working back along the shelf.
- A `while` loop is "stir until the sauce thickens." Nobody knows the number of stirs ahead of time. The cook checks the sauce before each stir and stops when it is ready. Forgetting to actually stir is the infinite loop: the sauce never thickens, and the cook stands there forever.
- The accumulator is the measuring bowl. It starts empty before the first scoop, each scoop adds to it, and it gets used once the scooping is done. Emptying it before every scoop is the bug of initializing inside the loop.
- `continue` is setting aside a bruised apple and picking up the next one. The apple does not get peeled, but the peeling goes on.
- `break` is finding the one jar of saffron on the shelf and stopping the search. There is no reason to check the rest of the jars.

## Example

```python
# for loops with range
for i in range(0, 3):
    print(i)                            # 0, 1, 2

for i in range(3):
    print(i)                            # 0, 1, 2, start defaults to 0

print(list(range(5, 10)))               # [5, 6, 7, 8, 9]
print(list(range(0, 10, 2)))            # [0, 2, 4, 6, 8]
print(list(range(3, 0, -1)))            # [3, 2, 1]
print(list(range(10, 0)))               # [], start is already past stop
print(len(range(0, 1000)))              # 1000

def count_down(start, end):
    for i in range(start, end, -1):
        print(i)

count_down(5, 2)                        # 5, 4, 3

# Accumulator pattern
def sum_of_numbers(n):
    total = 0
    for i in range(0, n):
        total += i
    return total

print(sum_of_numbers(5))                # 10, 0 + 1 + 2 + 3 + 4

def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total

print(sum_of_odd_numbers(10))           # 25, 1 + 3 + 5 + 7 + 9

def calculate_experience_points(level):
    xp = 0
    for current_level in range(1, level):
        xp += current_level * 5
    return xp

print([calculate_experience_points(n) for n in range(1, 5)])   # [0, 5, 15, 30]

# while loops
num = 0
while num < 3:
    num += 1
    print(num)                          # 1, 2, 3

def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:
        current_health += 1
        enemy_distance -= 2
    return current_health

print(regenerate(1, 10, 10))            # 5
print(regenerate(10, 10, 10))           # 10, the body never runs

def meditate(mana, max_mana, num_potions):
    while mana < max_mana and num_potions > 0:
        mana += 1
        num_potions -= 1
    return mana, num_potions

print(meditate(5, 10, 3))               # (8, 0)
print(meditate(5, 10, 9))               # (10, 4)

# Infinite loop with a way out
attempts = 0
while True:
    attempts += 1
    if attempts == 3:
        break
print(attempts)                         # 3

# continue
for number in range(-3, 3):
    if number < 0:
        continue
    print(f"The square root of {number} is {number**0.5}")   # 0, 1, 2 only

def award_enchantments(start, end, step):
    counter = 0
    for quests in range(start, end, step):
        counter += 1
        if counter < 3:
            continue
        counter = 0
        print(f"Enchantment of strength {quests * 5} awarded for completing {quests} quests!")

award_enchantments(2, 8, 1)             # strength 20 for 4 quests, strength 35 for 7 quests

# break
for n in range(42):
    if n * n > 150:
        print(f"stopped at {n}")        # stopped at 13
        break

def check_defense(attack, enchantments):
    for strength in enchantments:
        if strength >= attack:
            print(f"Blocked by enchantment of strength {strength}")
            break

check_defense(5, [2, 6, 9])             # Blocked by enchantment of strength 6, 9 is never checked

# Printing on the same line
for i in range(10, 0, -1):
    if i == 1:
        print(f"{i}...Fight!")          # 1...Fight!
    else:
        print(f"{i}...")                # 10... down to 2...

for i in range(3):
    print(i, end=" ")                   # 0 1 2 on one line
print()

# for, else
for n in [1, 3, 5]:
    if n % 2 == 0:
        print("found an even number")
        break
else:
    print("no even number")             # no even number

# The loop variable survives the loop
for i in range(3):
    pass
print(i)                                # 2

# Reassigning i inside the loop does not change the next value
for i in range(3):
    print(i)                            # 0, 1, 2
    i += 10
```

Common errors:

```python
for i in range(3)                       # SyntaxError: expected ':'
    print(i)

for i in range(3):
print(i)                                # IndentationError: expected an indented block after 'for' statement on line 1

for i in range(3):
    print(i)
      print(i)                          # IndentationError: unexpected indent

range(0, 10, 0)                         # ValueError: range() arg 3 must not be zero
range(0, 1.5)                           # TypeError: 'float' object cannot be interpreted as an integer

i = 0
i++                                     # SyntaxError: invalid syntax, use i += 1

break                                   # SyntaxError: 'break' outside loop
```

## In other languages

| | Python | JavaScript | Go | Bash |
|---|---|---|---|---|
| Counting loop | `for i in range(0, 10):` | `for (let i = 0; i < 10; i++) { }` | `for i := 0; i < 10; i++ { }`, or `for i := range 10 { }` since Go 1.22 | `for ((i=0; i<10; i++)); do ... done` or `for i in {0..9}` |
| Step | `range(0, 10, 2)` | `i += 2` in the loop header | `i += 2` in the loop header | `for i in $(seq 0 2 9)` or `((i+=2))` |
| Count down | `range(3, 0, -1)` | `for (let i = 3; i > 0; i--)` | `for i := 3; i > 0; i-- { }` | `for ((i=3; i>0; i--))` |
| While loop | `while cond:` | `while (cond) { }` | `for cond { }`. Go has no `while` keyword | `while (( cond )); do ... done` |
| Infinite loop | `while True:` | `while (true) { }` or `for (;;) { }` | `for { }` | `while true; do ... done` |
| Runs at least once | No do-while, use `while True` with `break` | `do { } while (cond);` | No do-while | No do-while |
| Skip and exit | `continue`, `break` | `continue`, `break` | `continue`, `break`, and labels to break an outer loop | `continue`, `break`, and `break 2` for an outer loop |
| Increment | `i += 1` | `i++` or `i += 1` | `i++`, a statement only | `((i++))` |
| Body marked by | Indentation | Braces | Braces, required | `do` and `done` |

Two ideas carry over to every language:

1. **Every loop needs a reason to stop.** In a counting loop, it is reaching the end of the range. In a condition loop, the body must change something the condition checks. Off by one errors come from the stop condition too, so check whether the last value should be included.
2. **Prefer the loop that matches the question.** "For each of these" is a `for` loop over the values. "Until this is true" is a `while` loop. Python's `for` over `range` hides the counter update, which removes a whole class of bugs that the C-style `for (i = 0; i < n; i++)` allows, such as updating the wrong variable.

## Interview framing

1. When would you use a `for` loop and when a `while` loop?
2. What is the difference between `break`, `continue`, and `return` inside a loop?
3. What does `range` return, and why is `range(10**12)` not a problem?
4. What does `else` do on a `for` loop?
5. How do you avoid an infinite loop, and how would you debug one?

## My answer

**1. `for` versus `while`**

"I use `for` when I am going through a known collection or a known number of steps, like every item in a list or every number in a range. The loop handles moving to the next value for me, so it cannot forget to advance. I use `while` when the stopping point depends on something that changes during the loop, like reading input until the user types quit, or retrying until a request succeeds. Any `for` loop can be written as a `while` with a manual counter, but the `for` version is shorter and harder to get wrong."

**2. `break`, `continue`, `return`**

"`continue` skips the rest of the current iteration and moves on to the next one. `break` leaves the loop entirely, and the code after the loop runs. `return` leaves the whole function, which ends the loop as a side effect. `break` and `continue` only apply to the innermost loop. To exit nested loops in Python, I usually move them into a function and `return`, since Python has no labeled break."

**3. `range`**

"`range` returns a range object, not a list. It only stores the start, stop, and step, and calculates each value when it is needed. So `range(10**12)` uses the same tiny amount of memory as `range(10)`, and checking `len`, indexing, or `in` on it is computed directly, without looping. Calling `list(range(...))` is what actually builds all the values in memory."

**4. `for`, `else`**

"The `else` block on a loop runs when the loop finishes without hitting a `break`. It fits the search pattern: loop through the items, `break` when found, and put the 'not found' handling in the `else`. The name is confusing, since it reads like 'if the loop did not run,' so I add a short comment or use a flag variable when the team is not used to it."

**5. Infinite loops**

"In a `while` loop, I make sure the body always changes something that the condition depends on, and that every path through the body does so, including paths with `continue`. When a loop is meant to be infinite, like a server's main loop, I make the exit explicit with `break` or `return`. To debug one, I interrupt it with Ctrl+C and look at the traceback to see which line it was stuck on, or print the variables in the condition each iteration to see which one is not changing."

**Points to recall**

- `range(start, stop, step)` includes `start` and excludes `stop`.
- `range(n)` starts at `0`. The step defaults to `1` and cannot be `0`.
- Counting down needs a negative step and `start` greater than `stop`.
- A range with no values runs the body zero times, with no error.
- Loop bodies need a colon and consistent indentation, 4 spaces by convention.
- Accumulator: initialize before the loop, update in the body, return after the loop.
- `while` checks the condition before each iteration, so the body may never run.
- The body of a `while` must move the condition toward false.
- `continue` skips to the next iteration, `break` exits the loop, `return` exits the function.
- `break` and `continue` only affect the innermost loop.
- Python has no `i++`. Use `i += 1`.
- `print(x, end=" ")` keeps output on the same line.

## Follow-up gotchas

**Does changing `i` inside a `for` loop change the next value?**
No. On each iteration, `for` assigns the next value from the range to `i`, overwriting whatever the body did. `i += 10` in the body only lasts until the end of that iteration. This is different from a C-style loop in JavaScript or Go, where changing `i` in the body does affect the next iteration. To skip ahead in Python, use `continue`, a different step, or a `while` loop with a manual counter.

**What is `i` after the loop ends?**
The last value it took. A `for` loop does not create a new scope, so `i` is still defined after the loop, and after `for i in range(3)` it is `2`. If the range was empty, `i` is never assigned, and using it after the loop raises a `NameError` unless it existed before. In JavaScript, `let i` in the header is scoped to the loop, and in Go, `i :=` is too.

**Why does `range(0, 10, -1)` produce nothing?**
A negative step counts down, and `0` is already below `10`, so there are no values before the stop. The loop body silently never runs, with no error. When a countdown loop does nothing, check that `start` is greater than `stop`.

**Is there a do-while loop in Python?**
No. The usual replacement is `while True:` with the body first and an `if ...: break` at the end, which guarantees at least one run. JavaScript has `do { } while (cond);`, and Go and Bash do not.

**Why add up floats with care in a loop?**
Each `+=` with a float can add a tiny rounding error, and the errors build up over many iterations. Adding `0.1` three times gives `0.30000000000000004`, not `0.3`. This is the float behavior from Chapter 6, and it affects every language. For money, use integer cents or `decimal.Decimal`. For a `while` condition, compare with `<` or `>=` rather than `==` on a float, or the exact value may be stepped over and the loop never ends.
