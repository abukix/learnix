---
topic: Python
source: boot.dev (compiled from python-basics.md)
date: 2026-08-21
status: growing
---

# Python cheat sheet — recall-ready

Every concept from `python-basics.md` (CH1: Introduction → CH13: Type Hints), rewritten in one consistent card format so it can be read out loud like an interview answer instead of re-derived from prose. Each card: **What it is** → **Use case** → **Syntax** → **Gotcha** (a common trip-up, worth calling out unprompted if asked). Cards drilled so far also carry a **One-liner** — a single sentence that compresses the whole card, meant to be memorized verbatim as the fastest possible answer.

How to drill this: cover the card, say the "What it is" line from memory, then check. Getting the words different from what's written is fine — getting the *idea* wrong is the thing to catch.

For the fuller narrative version of each lesson, see [python-basics.md](python-basics.md). For deep, project-specific gotchas (scope bugs, mutation semantics, etc.) traced line-by-line, see [python-glossary.md](python-glossary.md).

---

## CH1 — Introduction

### What is Python?

- **One-liner:** Python is a high-level, interpreted, dynamically-typed language created by Guido van Rossum in 1991 — known for readable, English-like syntax, and widely used for backend web dev, AI/ML, and automation.
- **What it is:** A high-level, general-purpose, interpreted programming language created by Guido van Rossum, first released in 1991. "High-level" means it reads close to English and hides low-level detail (memory management, etc.) from the programmer. "Interpreted" means code runs line-by-line via the Python interpreter rather than being compiled to machine code ahead of time.
- **Use case:** AI/ML and data science (most of the ecosystem — PyTorch, pandas, NumPy — is Python-first), backend web development (Django, Flask), and automation/scripting for repetitive tasks. Not commonly used for frontend web work.
- **Syntax:** No braces — blocks are defined by indentation (whitespace is *meaningful*, not cosmetic).
- **Gotcha:** "Interpreted" doesn't mean "slow by design" and doesn't mean "no compilation step" — CPython does compile source to bytecode internally (that's what `__pycache__/.pyc` files are), it just doesn't produce a standalone machine-code binary the way C does.

### Code and syntax errors

- **One-liner:** Code is ordered instructions for the computer to execute; a syntax error breaks the language's grammar and stops the program from running at all, before any bug inside it could even be reached.
- **What it is:** Code is a series of instructions the computer executes in order. A **syntax error** is a violation of the language's grammar (unclosed bracket/quote, bad indentation, typo'd keyword) that stops the program from running *at all* — the interpreter can't even start, let alone reach the bug.
- **Use case:** N/A — this is a failure mode, not a tool. Recognizing "syntax error" vs. "exception" (CH12) as two different categories is the useful distinction.
- **Syntax:** `SyntaxError: invalid syntax`, usually with a `^` pointing at where parsing broke down.
- **Gotcha:** The `^` points at where the interpreter *noticed* the problem, not necessarily where the actual mistake is — a missing closing quote on line 3 might not error until line 5.

---

## CH2 — Variables and Types

### Variable

- **One-liner:** A variable is a name bound to a value, created the instant you assign it, and it can be reassigned to a new value — or even a new type — later.
- **What it is:** A named reference to a value, created the moment you assign something to it. Called "variable" because the value it points to can change.
- **Use case:** Storing data so it can be reused or changed instead of hardcoding it repeatedly.
- **Syntax:** `speed = 2` · multi-assign on one line: `name, dmg, length = "Excalibur", 10, 200`
- **Gotcha:** A variable must be assigned before it's read — top-to-bottom execution means `print(x)` before `x = 5` raises `NameError`, and functions using a name must be *defined* before they're *called* (why `main()` conventionally goes at the bottom of the file, called last).

### Naming rules

- **One-liner:** Python variable names are one continuous token with words separated by underscores — snake_case — per Guido van Rossum's own convention.
- **What it is:** Variable names are a single continuous token (no spaces) — words are separated with underscores.
- **Use case:** Readable, self-documenting code.
- **Syntax:** `snake_case` — Python's official convention (per Guido himself), e.g. `num_new_users`. Contrast: `camelCase` (JS/Java), `PascalCase` (C#/C++).
- **Gotcha:** camelCase/PascalCase still *run* in Python — it's a style convention, not an enforced rule, but breaking it reads as "not idiomatic Python."

### Core built-in types

- **One-liner:** Python's built-ins split into text, numeric, sequence, mapping, set, boolean, and None types, each with its own rules for order, duplicates, and mutability.
- **What it is:** Python categorizes its built-in types into text, numeric, sequence, mapping, set, boolean, and `None`.
- **Use case:** Picking the right container/type for the shape of data you're modeling — ordered vs. not, unique vs. duplicates allowed, changeable vs. fixed.
- **Syntax / mutability table:**

| Category | Type(s) | Mutable? | Example |
|---|---|---|---|
| Text | `str` | No | `"hello"` |
| Numeric | `int`, `float`, `complex` | No | `42`, `3.14`, `2+3j` |
| Sequence | `list` | Yes | `[1, 2, 3]` |
| Sequence | `tuple`, `range` | No | `(1, 2, 3)`, `range(5)` |
| Mapping | `dict` | Yes | `{"key": "value"}` |
| Set | `set` | Yes | `{1, 2, 3}` |
| Set | `frozenset` | No | `frozenset({1, 2})` |
| Boolean | `bool` | No | `True`, `False` |
| None | `NoneType` | No | `None` |

- **Gotcha:** "Mutable" isn't about the *variable*, it's about the *object*. `x = 5; x = 6` isn't mutation — it's rebinding `x` to a new `int` object (ints are immutable, full stop). Mutation is only possible on mutable types, via methods like `.append()` or `dict[key] = ...` that edit the object in place.

### Dynamic typing

- **One-liner:** Python is dynamically typed, so a variable's type is just whatever it currently holds and can change on reassignment — unlike statically typed languages, which lock a variable's type at compile time.
- **What it is:** A variable's type is determined by whatever value it currently holds, and isn't locked in — the same name can be reassigned to a different type later. Contrast: statically typed languages (Go, TypeScript) reject assigning a mismatched type at compile time.
- **Use case:** Faster iteration, less ceremony — but the flexibility is a double-edged sword.
- **Syntax:** `speed = 5` then later `speed = "five"` — legal, runs fine.
- **Gotcha:** Legal isn't the same as good practice. Reassigning a variable to a new *type* is usually a code smell — prefer a new, differently-named variable (`speed_description = "five"`) over overloading one name for two purposes.

### f-strings

- **One-liner:** An f-string embeds variables and expressions directly into a string using a leading f and {} placeholders — the modern, preferred way to format strings in Python.
- **What it is:** The modern (3.6+) way to embed variables/expressions directly into a string literal, using a leading `f` and `{}` placeholders.
- **Use case:** String formatting — building messages, logs, and output without manual `+` concatenation.
- **Syntax:** `f"Hello, {name}. You are {age} years old."` · inline expressions: `f"{age + 1}"`, `f"{name.upper()}"` · number formatting: `f"{price:.2f}"` (2 decimals), `f"{price:,}"` (commas) · debug shorthand (3.8+): `f"{x=}"` prints `x=10`.
- **Gotcha:** Quote-scoping — an f-string delimited with `"` needs `'` for any inner string (like a dict key) unless you're on Python 3.12+ (PEP 701 lifted this restriction). And a comma-separated group inside one `{}` isn't several values, it's a single tuple: `f"{a, b}"` prints `(a, b)`, not `a, b`.

### Mutability vs. immutability

- **One-liner:** Mutable objects like lists and dicts can be changed in place; immutable ones like ints, strings, and tuples can't — any "change" to them actually builds a brand-new object.
- **What it is:** Mutable objects (`list`, `dict`, `set`) can be changed in place after creation. Immutable objects (`int`, `float`, `str`, `tuple`, `frozenset`, `bool`) cannot — any "change" actually creates a brand-new object.
- **Use case:** Predicting whether a function can silently alter data you passed into it, and whether two variables pointing at "the same" value will see each other's changes.
- **Syntax:** `a = [1, 2]; b = a; b.append(3)` → `a` is now `[1, 2, 3]` too (same list object, two labels). `a = "hi"; b = a; b += "!"` → `a` is still `"hi"` (strings are immutable, `b` now points at a *new* string).
- **Gotcha:** `variable = value` always rebinds the label to a (possibly new) object and never edits one in place. Mutating *methods* (`.append()`, `.sort()`, `d[k] = x`) reach into the object a variable currently points at and edit it directly. Two variables referencing the same mutable object both see mutations, but neither sees the other's reassignments.

### `None`

- **One-liner:** None is Python's singleton value for "no value at all" — distinct from 0, False, or an empty string.
- **What it is:** A special singleton value representing "no value" / absence of data. Its own type is `NoneType`.
- **Use case:** Default/placeholder state before a variable has a real value; a function's implicit return when it has no explicit `return`.
- **Syntax:** `my_var = None`
- **Gotcha:** `None` is not `0`, not `False`, and not `""` — and definitely not the string `"None"` (`x = "None"` is a str with 4 characters, not a null value).

---

## CH3 — Functions

### Function

- **One-liner:** A function is a reusable, named block of code defined with def that takes inputs and can hand a value back to its caller with return.
- **What it is:** A reusable, named block of code, defined with `def`, that can accept inputs (parameters) and produce an output (via `return`).
- **Use case:** Avoiding copy-pasted logic — write the calculation once, call it with different inputs as many times as needed.
- **Syntax:**
  ```python
  def area_of_circle(r):
      pi = 3.14
      return pi * r * r

  area = area_of_circle(5)  # 78.5
  ```
- **Gotcha:** Functions must be *defined* before they're *called* — Python reads top to bottom. The standard fix: define all functions first, then call an entry-point function (conventionally `main()`) at the very bottom of the file.

### Parameters vs. arguments

- **One-liner:** Parameters are the names in a function's definition; arguments are the actual values supplied when it's called.
- **What it is:** Parameters are the names in the function *definition*; arguments are the actual values passed in at *call time*.
- **Use case:** Precise vocabulary for describing function signatures — though in practice the terms get used interchangeably.
- **Syntax:** `def add(a, b): ...` — `a`/`b` are parameters. `add(5, 6)` — `5`/`6` are arguments.
- **Gotcha:** By default, argument-to-parameter matching is purely positional — first argument fills the first parameter, regardless of names.

### `print()` vs. `return`

- **One-liner:** print() displays a value to the console and gives back None; return hands a value to the caller and prints nothing by itself.
- **What it is:** `print()` writes text to the console and gives back `None`. `return` ends the function and hands a value back to the *caller* — it prints nothing by itself.
- **Use case:** `return` when the value needs to be used elsewhere in the program (stored, passed on, computed with). `print()` only when a human needs to see it right now.
- **Syntax:** `def f(): print("hi")` → calling `x = f()` prints `"hi"` and sets `x = None`. `def g(): return "hi"` → calling `x = g()` prints nothing and sets `x = "hi"`.
- **Gotcha:** This is the single most common beginner confusion. If a function is supposed to *return* a value, printing it inside the function instead is a bug even though the console output can look identical.

### Default parameter values

- **One-liner:** A parameter can declare a fallback value with = in the function signature, making it optional for the caller to supply.
- **What it is:** A parameter can have a fallback value used when the caller omits that argument.
- **Use case:** Making a parameter "optional" without needing a separate overload.
- **Syntax:** `def get_greeting(email, name="there"): ...` → `get_greeting("a@b.com")` uses `name="there"`.
- **Gotcha:** Parameters with defaults must come *after* all required (no-default) parameters in the signature.

### Multiple return values

- **One-liner:** A function can return several comma-separated values at once — Python packs them into a tuple that the caller unpacks into separate variables.
- **What it is:** A function can return more than one value, comma-separated — Python packs them into a tuple under the hood.
- **Use case:** Returning two related results from one computation (e.g. damage dealt and mana remaining) without building a whole dict/class for it.
- **Syntax:** `return damage, new_mana` then unpack at the call site: `damage, mana = cast_iceblast(5, 100)`
- **Gotcha:** It's the *order* of the returned values that maps to the unpacking variables, not their names — you can name the receiving variables anything.

### `None` return

- **One-liner:** A function with no explicit return statement (or a bare return) automatically returns None.
- **What it is:** A function with no explicit `return` (or a bare `return`) automatically returns `None`.
- **Syntax:** `def f(): print("hi")` — calling `f()` and capturing it gives `None`.
- **Gotcha:** Easy to forget when refactoring — deleting a `return` statement silently turns a value-producing function into a `None`-returning one; nothing warns you.

---

## CH4 — Scope

### Scope

- **One-liner:** Scope is where a name is visible — local names live only inside the function that created them, while global names live at module level and are readable everywhere, but writable from inside a function only with extra syntax.
- **What it is:** The region of code where a given variable/function name is visible and usable. Two main levels: **local** (created inside a function, alive only for that call) and **global** (created at module/top level, visible everywhere including inside functions).
- **Use case:** Understanding why a variable created inside a function "disappears" once the function returns, and why functions can freely *read* module-level constants without extra syntax.
- **Syntax:**
  ```python
  pi = 3.14  # global

  def get_area(radius):
      return pi * radius * radius  # reads the global `pi` fine
  ```
- **Gotcha:** Reading a global from inside a function needs nothing special — but *writing* to one does (see `global` keyword, [python-glossary.md](python-glossary.md) for the full `UnboundLocalError` trace). A parameter (`x` in `def f(x): ...`) is local to that function; trying to read `x` outside it raises `NameError`.

---

## CH5 — Testing and Debugging

### Console-output vs. unit-test lessons

- **One-liner:** Console-output checks compare printed text exactly; unit tests call your functions directly and check their return values, ignoring anything printed.
- **What it is:** Two ways to check code correctness. Console-output: your program's *printed text* must match exactly. Unit tests: a separate test file calls your *functions* directly and checks their *return values*, ignoring anything printed.
- **Use case:** Unit tests are the realistic, professional pattern — they check behavior (return values), not incidental output, and you don't have to strip debug `print()`s before submitting.
- **Gotcha:** In console-output lessons, leftover debug `print()` statements make the actual output not match the expected output and fail the check — remove them before submitting. Not an issue in unit-test lessons.

### Debugging process

- **One-liner:** Debugging means writing a small piece of code, printing to verify it does what you expect, and repeating in small steps — never writing a large block blind and debugging it all at once.
- **What it is:** Write a small piece of code → add a `print()` to inspect a value → run it → confirm it matches expectations → fix if not → repeat. Even senior engineers work this way; the goal is small, verifiable steps instead of writing a large block blind and debugging it all at once.
- **Use case:** Isolating exactly which line broke, instead of guessing across a whole function.
- **Gotcha:** A stack trace ("traceback") looks intimidating but is just the interpreter reporting *where* and *why* execution failed — reading it top to bottom (or bottom to top, since Python prints the deepest frame last) is a learnable skill, not something to skip past.

---

## CH6 — Computing

### Integers vs. floats

- **One-liner:** An int is a whole number with no decimal part, a float has one, and regular division between two ints in Python 3 always produces a float.
- **What it is:** `int` = whole number, no decimal part. `float` = number with a decimal part.
- **Syntax:** `x = 5` (int) · `x = 5.2` (float)
- **Gotcha:** Regular division `/` between two ints *always* produces a float in Python 3, even when the result is a whole number: `4 / 2` → `2.0`, not `2`.

### Floor division `//`

- **One-liner:** Floor division divides and rounds the result down to the nearest integer, toward negative infinity.
- **What it is:** Division that rounds the result *down* to the nearest integer.
- **Use case:** Getting a whole-number quotient (e.g. "how many full groups of N fit").
- **Syntax:** `8 // 3` → `2` · `-7 // 3` → `-3` (rounds toward negative infinity, not toward zero — watch this with negatives).

### Exponents `**`

- **One-liner:** The ** operator raises a number to a power, built into Python with no math import required.
- **What it is:** Python's built-in power operator — no math library import needed.
- **Syntax:** `3**2` → `9` ("three squared")

### Modulo `%`

- **One-liner:** The modulo operator % returns the remainder of a division — commonly used to test evenness or wrap a value within a fixed range.
- **What it is:** Returns the *remainder* of a division.
- **Use case:** Checking evenness/oddness (`n % 2 == 0`), cycling an index within a fixed range, extracting "leftover" amounts.
- **Syntax:** `8 % 3` → `2`
- **Gotcha:** It's not a percentage despite the `%` symbol — pure "what's left over" arithmetic.

### Compound assignment (`+=`, `-=`, `*=`, `/=`)

- **One-liner:** Compound operators like += read a variable's current value, apply an operation, and reassign the result — all in one step.
- **What it is:** Shorthand that reads a variable's current value, applies an operation, and reassigns the result — in place of writing it out longhand.
- **Syntax:** `score += 1` is shorthand for `score = score + 1`
- **Gotcha:** It still counts as a full assignment for scope purposes — inside a function, `x -= 1` makes `x` local for the *entire function body*, even lines above it (see [python-glossary.md](python-glossary.md) `UnboundLocalError` note).

### Logical operators: `and`, `or`, `not`

- **One-liner:** and requires both sides to be True, or requires at least one side to be True, and not flips a boolean — all operating on booleans, unlike the bitwise & and | which operate on individual bits.
- **What it is:** Boolean-combining operators. `and` → `True` only if both sides are `True`. `or` → `True` if at least one side is `True`. `not` → flips a boolean.
- **Syntax:** `True and False` → `False` · `True or False` → `True` · `not True` → `False`
- **Gotcha:** Don't confuse these (operate on booleans) with the bitwise operators `&`/`|` (operate on the individual bits of integers) — they look similar but work at different levels.

### Scientific notation & underscores

- **One-liner:** Scientific notation (16e3) writes very large or small floats compactly, and underscores (16_000) are a purely visual separator in number literals.
- **What it is:** `e`/`E` notation for very large/small floats; `_` as a readability separator in number literals (not a comma).
- **Syntax:** `16e3` → `16000.0` · `7.1e-2` → `0.071` · `16_000` → `16000`

---

## CH7 — Comparisons

### Comparison operators

- **One-liner:** Comparison operators (<, >, <=, >=, ==, !=) compare two values and always evaluate to a boolean.
- **What it is:** Operators that compare two values and always evaluate to a `bool`.
- **Syntax:**

| Operator | Meaning |
|---|---|
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |
| `==` | equal to |
| `!=` | not equal to |

- **Gotcha:** `==` (comparison) vs. `=` (assignment) is the classic typo — `if x = 5` is a syntax error in Python (unlike some languages where it silently assigns).

### `if` / `elif` / `else`

- **One-liner:** if/elif/else runs the first matching block top to bottom and skips the rest, falling through to else only if nothing else matched.
- **What it is:** Conditional branching. `if` is evaluated first; if `True`, its body runs and everything else (`elif`s, `else`) is skipped. Otherwise the next `elif` is checked, and so on; `else` catches everything unmatched.
- **Syntax:**
  ```python
  if score > high_score:
      print("New high score!")
  elif score > second_highest:
      print("Second place!")
  else:
      print("Try again")
  ```
- **Gotcha:** Without an early `return` inside an `if` block in a function, execution falls through to whatever code comes *after* the block too — it doesn't automatically exit the function.

### Boolean logic combining conditions

- **One-liner:** Chaining comparisons with and/or expresses compound rules — and for "all must hold," or for "at least one must hold."
- **What it is:** Chaining comparisons with `and`/`or` to express compound rules.
- **Use case:** "All of these must be true" (`and`) vs. "at least one must be true" (`or`) — e.g. serving a drink requires age ≥ 21 **and** bartender working **and** time in range.
- **Gotcha:** `if is_big == True:` works but is redundant — prefer `if is_big:` directly, since `is_big` already *is* the boolean value being tested.

---

## CH8 — Loops

### `for` loop with `range()`

- **One-liner:** A for loop with range(start, stop, step) iterates a variable over a sequence of numbers, including start but excluding stop.
- **What it is:** Iterates a variable over a sequence of numbers.
- **Syntax:** `range(start, stop, step)` — inclusive of `start`, exclusive of `stop`. `for i in range(0, 10): print(i)` prints 0–9. `range(0, 10, 2)` steps by 2. `range(3, 0, -1)` counts down.
- **Gotcha:** `stop` is never included — `range(0, 10)` never produces `10`. This is the single most common off-by-one source for beginners.

### `while` loop

- **One-liner:** A while loop repeats as long as its condition stays True, checked fresh before every iteration.
- **What it is:** Repeats as long as a condition stays `True`, checked before each iteration.
- **Use case:** When the number of iterations isn't known ahead of time (unlike `for`/`range`, which is for a known count).
- **Syntax:**
  ```python
  num = 0
  while num < 3:
      num += 1
  ```
- **Gotcha:** Forgetting to update the loop's condition variable inside the body creates an infinite loop.

### `continue` vs. `break`

- **One-liner:** continue skips to the next iteration of a loop; break exits the loop entirely, right away.
- **What it is:** `continue` skips the rest of the *current* iteration and jumps to the next one. `break` exits the loop *entirely*, immediately.
- **Use case:** `continue` to skip items that don't apply (e.g. skip negative numbers before computing a square root). `break` to stop early once a condition is met (e.g. stop once a threshold is exceeded), avoiding wasted iterations.
- **Syntax:**
  ```python
  for n in range(42):
      if n * n > 150:
          break
      print(n)
  ```

---

## CH9 — Lists

### List

- **One-liner:** A list is an ordered, mutable, duplicate-allowing collection — Python's version of an array — indexed from 0.
- **What it is:** An ordered, mutable collection that allows duplicates. Python's equivalent of what other languages call an "array."
- **Use case:** Any sequence of items where order matters and the collection may grow/shrink/change — an inventory, a roster, a feed of posts.
- **Syntax:** `inventory = ["Sword", "Potion", "Scraps"]`
- **Gotcha:** Indexing starts at `0`, not `1` — `names[0]` is the *first* item. `len(names)` is always one greater than the last valid index.

### Indexing, updating, appending, popping

- **One-liner:** .append() adds to the end of a list and .pop() removes and returns the last item — both mutate the list in place, with no reassignment needed.
- **What it is:** Core list operations — read/write by position, add to the end, remove from the end.
- **Syntax:** `names[1]` (read) · `inv[0] = "New Item"` (update in place) · `cards.append("nvidia")` (add to end) · `vegetables.pop()` (remove & return last item)
- **Gotcha:** `.append()` and `.pop()` mutate the list *in place* and don't need reassignment — `cards = cards.append(...)` is a bug, since `.append()` itself returns `None`.

### Iterating

- **One-liner:** Loop over a list by index (range(len(list))) when you need the position, or directly (for item in list) when you only need the value.
- **What it is:** Looping over a list's items either by index (`range(len(...))`) or directly (no-index `for item in list`).
- **Use case:** No-index form when you only need the value; index form when you also need the position (or need to mutate by position).
- **Syntax:** `for tree in trees: print(tree)`

### Slicing

- **One-liner:** Slicing (list[start:stop:step]) pulls out a new sub-list, with any section omittable and negative indices counting from the end.
- **What it is:** Extracting a sub-list using `[start:stop:step]`; any section can be omitted. Returns a *new* list.
- **Syntax:** `nums[1:5:2]` · `nums[:3]` (start to index 3, exclusive) · `nums[3:]` (index 3 to end) · `nums[::2]` (every other item) · `nums[-3:]` (last 3 items, negative index counts from the end)

### Concatenation & membership

- **One-liner:** + joins two lists into a new one, and in/not in checks whether a value exists inside a list.
- **What it is:** `+` joins two lists into a new one. `in`/`not in` checks whether a value exists in a list.
- **Syntax:** `[1,2,3] + [4,5,6]` → `[1,2,3,4,5,6]` · `"banana" in fruits` → `True`/`False`

### Tuple

- **One-liner:** A tuple is an ordered, immutable, fixed-size grouping used for small, distinctly-shaped data like a coordinate or a name-age pair, and a single-item tuple needs a trailing comma to not be read as a plain parenthesized value.
- **What it is:** An ordered, *immutable* collection — like a list with a fixed size, created with `()` instead of `[]`.
- **Use case:** Small, fixed-shape groupings where each position has a distinct meaning (e.g. a coordinate, a name+age pair) — as opposed to a list, which is normally a variable-length collection of *similar* things.
- **Syntax:** `dog = ("Fido", 4)` · unpacking: `name, age = dog` · list of tuples: `my_tuples[0][1]` (tuple index, then value index)
- **Gotcha:** A single-item tuple *needs* a trailing comma — `("Fido")` is just a parenthesized string, not a tuple; it must be `("Fido",)`.

### `.split()` / `.join()`

- **One-liner:** .split() breaks a string into a list of substrings, and sep.join(list) glues a list of strings back together with a delimiter.
- **What it is:** `.split()` breaks a string into a list of substrings (default: split on whitespace). `.join()` does the reverse — glues a list of strings together with a given delimiter.
- **Syntax:** `"hello there".split()` → `["hello", "there"]` · `" ".join(["hello", "there"])` → `"hello there"`
- **Gotcha:** `.join()` is called *on the delimiter*, not on the list — `" ".join(list_of_words)`, not `list_of_words.join(" ")`.

---

## CH10 — Dictionaries

### Dictionary

- **One-liner:** A dictionary is a mutable, ordered (3.7+) collection of unique key-to-value pairs, used to model labeled, structured data.
- **What it is:** A mutable collection of key → value pairs; ordered as of Python 3.7+. No duplicate keys allowed.
- **Use case:** Modeling structured, labeled data — a record with named fields — rather than a flat sequence.
- **Syntax:** `car = {"brand": "Toyota", "year": 2019}`
- **Gotcha:** Writing a key twice in a literal doesn't error — the *last* value silently wins: `{"brand": "Toyota", "brand": "Honda"}` → `{'brand': 'Honda'}`.

### Access, set, update, delete

- **One-liner:** Square brackets read and write dict values by key (d["key"]), and del d["key"] removes an entry — reading or deleting a missing key raises KeyError.
- **What it is:** Square-bracket syntax for reading and writing by key.
- **Syntax:** `car["make"]` (read) · `planets["Earth"] = True` (set/update — same syntax either way) · `del names_dict["joe"]` (delete)
- **Gotcha:** Deleting a key that doesn't exist raises `KeyError`. Reading a missing key also raises `KeyError` (unlike `list` out-of-range, this is the same exception type but a different cause).

### Checking existence & iterating

- **One-liner:** in checks for a key's presence in a dict, and looping directly over a dict (for k in d) walks its keys.
- **What it is:** `in` checks for a *key's* presence (not a value's). Iterating a dict directly (`for k in d`) walks its keys.
- **Syntax:** `"ford" in cars` → `True`/`False` · `for name in fruit_sizes: size = fruit_sizes[name]`

### Nested dicts

- **One-liner:** Dict values can themselves be dicts or lists, letting you model arbitrarily hierarchical data.
- **What it is:** Dict values can themselves be dicts (or lists), letting you model arbitrarily structured/hierarchical data.
- **Syntax:** `{"quests": {"bridge_run": {"status": "In Progress"}}}`

---

## CH11 — Sets

### Set

- **One-liner:** A set is an unordered, mutable collection that automatically discards duplicates, created with {} (non-empty) or set() (empty, since bare {} means an empty dict).
- **What it is:** An unordered, mutable collection that guarantees uniqueness — no duplicates possible.
- **Use case:** Tracking "have I seen this before" (visited locations, unique tags) where order doesn't matter and duplicates should be automatically discarded.
- **Syntax:** `fruits = {"apple", "banana"}` · add: `fruits.add("pear")` · empty set: `set()` (not `{}` — that's an empty dict!)
- **Gotcha:** Adding a value already in the set is a silent no-op, not an error. Because sets are unordered, printing/iterating one can show items in any order, and that order isn't guaranteed to be stable.

### Set subtraction

- **One-liner:** Subtracting one set from another (set1 - set2) removes every element of the second set from the first.
- **What it is:** `-` between two sets removes all elements of the second set from the first.
- **Syntax:** `{"apple","banana","grape"} - {"apple","banana"}` → `{"grape"}`

---

## CH12 — Errors

### Syntax errors vs. exceptions

- **One-liner:** A syntax error means the code isn't valid Python and can't run at all; an exception is a runtime error in otherwise-valid code that can be anticipated and handled gracefully.
- **What it is:** A syntax error means the code isn't even valid Python and can't run. An exception is a runtime error — the code *is* valid, but something went wrong while it executed (division by zero, missing key, etc.).
- **Use case:** Exceptions can be anticipated and handled gracefully; syntax errors just need to be fixed before anything runs.

### `try` / `except`

- **One-liner:** try/except wraps risky code so that if it raises an exception, control jumps to a matching handler instead of crashing the program.
- **What it is:** Wraps risky code so that if it raises an exception, execution jumps to a handler instead of crashing the whole program.
- **Syntax:**
  ```python
  try:
      10 / 0
  except Exception as e:
      print(e)  # "division by zero"
  ```
- **Gotcha:** Multiple `except` clauses are checked top to bottom, and only the *first type match* runs — order matters, and a broad `except Exception` placed first will swallow everything below it.

### `raise`

- **One-liner:** raise manually triggers an exception, used to signal an error condition your own code has detected.
- **What it is:** Manually triggers an exception.
- **Use case:** Signaling an error condition your own code detects (bad input, invalid state) instead of letting the program continue in a broken state.
- **Syntax:** `raise Exception("something bad happened")`

### Exception hierarchy

- **One-liner:** Nearly every built-in exception is a subclass of the base Exception type, which is why except Exception catches virtually anything — but matching is always based on the exception's type, never its message string.
- **What it is:** Built-in exceptions form a type hierarchy — nearly all of them (`ZeroDivisionError`, `IndexError`, `KeyError`, ...) are subclasses of the base `Exception` type.
- **Use case:** Explains why `except Exception` catches *everything* — it matches any exception type because they all IS-A `Exception`.
- **Gotcha:** What matters for matching an `except` clause is the exception's *type*, not its message string. `raise Exception("zero division")` is still just a plain `Exception` — it will **not** be caught by `except ZeroDivisionError`, only by `except Exception`, regardless of what the message says.

---

## CH13 — Type Hints

### Type hints

- **One-liner:** Type hints are optional, unenforced annotations that document a variable, parameter, or return value's intended type, mainly to help humans and tooling catch mistakes before running the code.
- **What it is:** Optional annotations that document the *intended* type of a variable, parameter, or return value. Purely advisory — Python remains dynamically typed and does **not** enforce hints at runtime.
- **Use case:** Readability for humans, and better autocomplete/error-catching in editors and tools like mypy — catching a type mistake *before* running the code, not after.
- **Syntax:** variable: `character_level: int = 7` · parameter: `def greet(name: str): ...` · return: `def add(a: int, b: int) -> int: ...`
- **Gotcha:** Hints on simple variable declarations are often redundant (the type is inferable from the literal), but hints on function *parameters* are genuinely useful — without them, the tooling has no way to infer what a parameter's type is meant to be.

### Container type hints

- **One-liner:** Container type hints like list[str] or dict[str, int] specify not just the container but what type(s) live inside it, read outside-in when nested.
- **What it is:** Hints for `list`, `set`, `dict`, `tuple` specify not just the container but what's inside it.
- **Syntax:** `list[str]` · `set[str]` · `dict[str, int]` (key type, then value type) · `tuple[str, int]` (position-by-position, can mix types) · nested: `dict[str, list[str]]` (read outside-in: a dict of str → list of str)
- **Gotcha:** A bare `list` (no `[...]`) is legal but tells you nothing about what's inside — prefer being specific whenever the contents are known.

### Optional values (`X | None`)

- **One-liner:** The | operator marks a value as possibly being one of several types, most often "this type, or None" for something that might not exist.
- **What it is:** The `|` operator marks a value as possibly being one of several types — most commonly "this type, or `None`."
- **Use case:** A function that might not have anything to return (e.g. "no spell prepared") should say so in its signature.
- **Syntax:** `damage_bonus: int | None` · `def get_prepared_spell(has_spell: bool) -> str | None: ...`

---

## Quick-reference tables

### Built-in type mutability (all in one place)

| Mutable | Immutable |
|---|---|
| `list`, `dict`, `set` | `int`, `float`, `str`, `tuple`, `frozenset`, `bool`, `NoneType` |

### Container syntax at a glance

| Type | Literal | Ordered? | Duplicates? | Mutable? |
|---|---|---|---|---|
| `list` | `[1, 2, 3]` | Yes | Yes | Yes |
| `tuple` | `(1, 2, 3)` | Yes | Yes | No |
| `dict` | `{"k": "v"}` | Yes (3.7+) | No dup keys | Yes |
| `set` | `{1, 2, 3}` | No | No | Yes |

### Common built-ins used throughout the course

| Function/method | Does |
|---|---|
| `len(x)` | Number of items in a list/dict/set, or characters in a string |
| `type(x)` | The runtime type of `x` |
| `range(start, stop, step)` | Lazy sequence of numbers, `stop` exclusive |
| `float("inf")` / `float("-inf")` | Positive/negative infinity — handy as a starting "worst possible" value when searching for a max/min |
| `sum(iterable)` | Adds up all the numbers in an iterable |
| `.append(x)` | Add `x` to the end of a list (mutates in place) |
| `.pop()` | Remove & return the last item of a list (mutates in place) |
| `.split()` / `sep.join(list)` | String ↔ list of strings |
