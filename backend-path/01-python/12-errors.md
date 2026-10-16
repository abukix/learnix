# 12: Errors

Source: boot.dev Learn Python, Chapter 12, Lessons 1 to 9.

## What it is

### Two kinds of errors

Python has two kinds of errors that can be told apart:

- **Syntax errors.** The code is not valid Python, so the interpreter refuses to run any of the file. Chapter 5 covers how they are reported.
- **Exceptions.** The code is valid, but something goes wrong while it runs, such as dividing by zero or reading an index that does not exist.

```python
this is not valid code, so it will error
#                  ^^^^
# SyntaxError: invalid syntax
```

A syntax error cannot be handled by the program itself, because the program never starts. An exception can be, and that is what this chapter is about.

### What an uncaught exception does

When an exception is raised and nothing handles it, the program stops at that line and Python prints a traceback (see Chapter 5). The lines after it never run:

```python
def craft(metal_bar):
    raise Exception("invalid metal bar")

print("start")
craft("gold")
print("end")
```

```
start
Traceback (most recent call last):
  File "craft.py", line 5, in <module>
    craft("gold")
    ~~~~~^^^^^^^^
  File "craft.py", line 2, in craft
    raise Exception("invalid metal bar")
Exception: invalid metal bar
```

`"end"` is never printed. An exception travels up from the function where it happened to the function that called it, then to that function's caller, and so on. If it reaches the top of the program without being handled, the program crashes.

### Handling exceptions with `try` and `except`

A `try` block runs code that might fail, and an `except` block says what to do if it does:

```python
try:
    10 / 0
except Exception:
    print("can't divide by zero")
```

The `try` block runs line by line until it finishes or an exception is raised, whichever comes first. If an exception is raised, Python jumps straight to the `except` block and skips the rest of `try`. If no exception is raised, the `except` block is skipped entirely. Either way, the program continues after the whole `try`/`except`, instead of crashing.

The exception does not have to happen directly in the `try` block. It can happen inside a function called from there, at any depth, and still be caught:

```python
def divide(a, b):
    return a / b

try:
    divide(10, 0)
    print("division complete")
except Exception as e:
    print(e)

print("done")

# division by zero
# done
```

`"division complete"` is skipped, because the line before it raised. Putting code inside a `try`/`except` is called wrapping it.

### Reading the exception with `as`

`except Exception as e` stores the exception in `e`. Printing it shows its message:

```python
try:
    10 / 0
except Exception as e:
    print(e)    # division by zero
```

`print()` shows the string version of whatever it is given, and for an exception that is the message. `e` is an object, not a string, so it can also be returned or stored. `type(e).__name__` gives the type's name, such as `ZeroDivisionError`, and `repr(e)` shows both, as in `ZeroDivisionError('division by zero')`.

The name `e` only exists inside the `except` block. Python deletes it when the block ends, so using `e` after it is a `NameError`.

### Raising your own exceptions

`raise` creates an exception on purpose:

```python
raise Exception("something bad happened")
```

It stops the function right there, just like an exception Python raises itself, and the caller either handles it or crashes. The string is the message that `print(e)` shows later.

A function should raise when it is given something it cannot sensibly handle. This one only knows three metals:

```python
def craft_sword(metal_bar):
    if metal_bar == "bronze":
        return "bronze sword"
    if metal_bar == "iron":
        return "iron sword"
    if metal_bar == "steel":
        return "steel sword"
    raise Exception("invalid metal bar")
```

Gold bars exist in the game, but gold swords do not. Without the `raise`, the function would fall off the end and return `None`, and the caller would carry that `None` forward until something broke far away from the real cause. With it, the problem is reported at the exact point it happened.

The same shape is used for checking inputs. The check comes first, and the normal work comes after it:

```python
def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception("not enough gold")
    return gold_available - price

purchase_item(10, 25)    # 15
purchase_item(25, 25)    # 0
purchase_item(30, 25)    # Exception: not enough gold
```

There is no `else` needed, because `raise` ends the function the same way `return` does.

### Errors are not bugs

An error and a bug are different things. An error is something going wrong, like bad input, a missing database row, or a lost network connection. Every program that runs in production hits errors all the time. A bug is when the program does something its users do not expect.

Raising an error is often how a bug is prevented. A gold sword that should not exist is a bug. `craft_sword("gold")` raising an exception is the function behaving exactly as designed. As long as the error is handled the way users expect, it is not a bug.

### Raise in the function, handle in the caller

As a rule of thumb, a function should not catch an exception that it raised itself:

```python
# don't do this
def craft_sword(metal_bar):
    try:
        if metal_bar == "bronze":
            return "bronze sword"
        raise Exception("invalid metal bar")
    except Exception as e:
        print(f"An error occurred: {e}")
```

This version prints a message and then returns `None`, which is the exact problem the `raise` was supposed to prevent. The function has also decided on its own that printing is the right response.

Instead, the function raises, and the caller wraps the call:

```python
# do this
try:
    craft_sword("gold bar")
except Exception as e:
    print(e)    # invalid metal bar
```

The function knows that something is wrong, but only the caller knows what to do about it. One caller might show the player a message, another might write it to a log, and a third might let the program crash because continuing would be worse.

### Exception types

Exceptions come in types. Some are specific, such as `ZeroDivisionError` from dividing by zero and `IndexError` from an index that is too high or too low. `Exception` is the general one, and almost every exception counts as an `Exception`. Exceptions are objects made from classes, which the object-oriented course covers.

An `except` can name a specific type. Several `except` blocks can follow one `try`, and Python checks them from top to bottom:

```python
try:
    10 / 0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)

# 0 division
# index error
```

An `except` catches the type it names, and every more specific type that belongs under it. It does not catch a more general one. `except Exception` catches a `ZeroDivisionError`, but `except ZeroDivisionError` does not catch a plain `Exception`.

### Specific types first

Python runs the first `except` that matches and ignores the rest. Since `Exception` matches almost everything, putting it first hides every block below it:

```python
try:
    nums = [0, 1]
    print(nums[2])
except Exception:
    print("An error occurred")
except IndexError:
    print("Index error")

# An error occurred
```

`"Index error"` can never print. Python does not warn about this, so the order has to be right: most specific first, `Exception` last.

### Types match, messages do not

`except` looks at the type of the exception, never at its message. This raises a plain `Exception` whose message happens to say "zero division":

```python
try:
    raise Exception("zero division")
except ZeroDivisionError as e:
    print("zero")
except Exception as e:
    print("other")

# other
```

The message is just text. The type is still `Exception`, which is more general than `ZeroDivisionError`, so the first block does not match. Without the second block, the exception would not be caught at all, and the program would crash. In the other direction, a real `10 / 0` caught by `except Exception` prints `"other"`, because a `ZeroDivisionError` is an `Exception`.

This matters when using code from other modules. They document which types they raise, and the type is what a caller catches. The wording of a message can change between versions.

### Handling some errors and returning others

A function that calls risky code can turn different exceptions into different results:

```python
players = ["ana", "ben"]

def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    return players[player_id]

def process_player_record(player_id):
    try:
        return get_player_record(player_id)
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e

process_player_record(1)     # 'ben'
process_player_record(5)     # 'index is too high'
process_player_record(-1)    # Exception('negative ids not allowed')
```

`players[5]` raises an `IndexError` that Python creates, and the first block catches it. The negative id raises a plain `Exception` from `get_player_record`, which only the second block matches. Returning `e` returns the exception object itself, not its message. It prints as the message, but `type()` shows it is an `Exception`. A `return` inside `try` works normally: if nothing goes wrong, the function returns the record and the `except` blocks never run.

`get_player_record` raises for negative ids on purpose. Python would accept `players[-1]` and return the last player, which is a valid index but the wrong answer for a player id.

### More `try` features

This one goes beyond the lessons. A few more pieces of the same syntax come up often:

- **Raising a specific type.** `raise ValueError("price must be positive")` works like `raise Exception(...)`, but lets callers catch it with `except ValueError` without also catching everything else. `ValueError` means the right type with a bad value. `TypeError` means the wrong type.
- **Several types in one block.** `except (IndexError, KeyError) as e:` catches either one. The types go in a tuple.
- **`else`** runs only when the `try` block raised nothing. It keeps the code that should not be protected out of `try`.
- **`finally`** always runs last, whether there was an exception or not. It is for cleanup, like closing a file.

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("no")
else:
    print("else ran")
finally:
    print("finally ran")

# else ran
# finally ran
```

## Analogy

Continuing the kitchen from Chapters 1 to 11: **an exception is a cook calling out a problem instead of quietly serving a bad plate.**

- A syntax error is a recipe card written in nonsense. Nobody starts cooking from it at all.
- An exception is a problem found while cooking from a good recipe: the oven is cold, or the fridge has no eggs.
- `raise` is the line cook shouting "out of eggs!" and stopping that dish right there. It is better than slipping an omelette with no eggs out to the dining room.
- `try` is the head chef saying "start this dish." `except` is the plan for when someone shouts. The chef stops the dish, deals with it, and the rest of the kitchen keeps running.
- Without a plan, the shout goes up to the head chef, then the manager, and if nobody has a plan, the whole kitchen shuts down. That is the traceback.
- Errors are not bugs. Running out of eggs happens on busy nights, and calling it out is the right thing to do. The bug would be a customer getting a plate they did not order.
- A cook should not shout "out of eggs" and then answer themselves with a shrug. They call it out, and the head chef decides whether to send someone to the store, take the dish off the menu, or apologize to the table.
- Exception types are the kind of problem. "The oven is broken" and "out of eggs" get different plans, and "something went wrong" is the general plan that covers anything left over. The specific plans have to be checked first, or the general plan takes every call.
- The plan responds to what kind of problem it is, not the words shouted. A cook yelling "the oven is broken!" about a missing egg is still reporting a missing egg.

## Example

```python
# Catching an exception
try:
    10 / 0
except Exception:
    print("can't divide by zero")      # can't divide by zero

# The rest of try is skipped, the program keeps going
def divide(a, b):
    return a / b

try:
    divide(10, 0)
    print("division complete")         # skipped
except Exception as e:
    print(e)                           # division by zero
print("done")                          # done

try:
    print(divide(10, 2))               # 5.0
except Exception as e:
    print(e)                           # skipped, nothing was raised

# Raising
def craft_sword(metal_bar):
    if metal_bar == "bronze":
        return "bronze sword"
    if metal_bar == "iron":
        return "iron sword"
    if metal_bar == "steel":
        return "steel sword"
    raise Exception("invalid metal bar")

try:
    print(craft_sword("iron"))         # iron sword
    print(craft_sword("gold bar"))     # raises
    print("never printed")
except Exception as e:
    print(e)                           # invalid metal bar

# Catching your own exception hides it and returns None
def craft_sword_bad(metal_bar):
    try:
        if metal_bar == "bronze":
            return "bronze sword"
        raise Exception("invalid metal bar")
    except Exception as e:
        print(f"An error occurred: {e}")

result = craft_sword_bad("gold")       # An error occurred: invalid metal bar
print(result)                          # None

# Validating input
def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception("not enough gold")
    return gold_available - price

print(purchase_item(10, 25))           # 15
print(purchase_item(25, 25))           # 0
try:
    purchase_item(30, 25)
except Exception as e:
    print(e)                           # not enough gold

# Specific types
try:
    10 / 0
except ZeroDivisionError:
    print("0 division")                # 0 division
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")               # index error
except Exception as e:
    print(e)

# General first hides the specific one
try:
    nums = [0, 1]
    print(nums[2])
except Exception:
    print("An error occurred")         # An error occurred
except IndexError:
    print("Index error")               # never reached

# Types match, messages do not
try:
    raise Exception("zero division")
except ZeroDivisionError as e:
    print("zero")
except Exception as e:
    print("other")                     # other

try:
    10 / 0
except Exception as e:
    print("other")                     # other, ZeroDivisionError is an Exception

# Handling some, returning others
players = ["ana", "ben"]

def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    return players[player_id]

def process_player_record(player_id):
    try:
        return get_player_record(player_id)
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e

print(process_player_record(1))        # ben
print(process_player_record(5))        # index is too high
print(process_player_record(-1))       # negative ids not allowed
print(repr(process_player_record(-1)))    # Exception('negative ids not allowed')

# Looking at the exception
try:
    {}["a"]
except Exception as e:
    print(e)                           # 'a'
    print(repr(e))                     # KeyError('a')
    print(type(e).__name__)            # KeyError

# Beyond the lessons
try:
    int("abc")
except ValueError as e:
    print(e)                           # invalid literal for int() with base 10: 'abc'

try:
    [1][5]
except (IndexError, KeyError) as e:
    print(e)                           # list index out of range

try:
    x = 10 / 2
except ZeroDivisionError:
    print("no")
else:
    print("else ran")                  # else ran
finally:
    print("finally ran")               # finally ran
```

Common errors:

```python
raise exception("x")                   # NameError: name 'exception' is not defined. Did you mean: 'Exception'?
raise "oops"                           # TypeError: exceptions must derive from BaseException

try:
    10 / 0
except ZeroDivisionError e:            # SyntaxError: invalid syntax, as is missing
    pass

try:                                   # SyntaxError: expected 'except' or 'finally' block
    10 / 0
print("after")

try:
    raise Exception("zero division")
except ZeroDivisionError:              # does not match, so the program crashes
    print("zero")                      # Exception: zero division

try:
    10 / 0
except ZeroDivisionError as e:
    pass
print(e)                               # NameError: name 'e' is not defined
```

## In other languages

| | Python | JavaScript | Go | Bash |
|---|---|---|---|---|
| Model | Exceptions | Exceptions | Errors as return values | Exit status codes |
| Handle | `try:` / `except Exception as e:` | `try { } catch (e) { }` | `if err != nil { }` | `if ! cmd; then ... fi`, or `cmd \|\| ...` |
| Raise | `raise Exception("msg")` | `throw new Error("msg")` | `return errors.New("msg")` | `echo "msg" >&2; return 1` |
| Read the message | `print(e)` | `e.message` | `err.Error()` | Read stderr |
| Catch by type | `except IndexError:` | One `catch`, then check `e instanceof RangeError` | `errors.Is(err, target)` or `errors.As(err, &t)` | Check the number in `$?` |
| Cleanup | `finally:` | `finally { }` | `defer` | `trap '...' EXIT` |
| Uncaught | Traceback, program stops | Stack trace, program stops (Node) | Error is ignored unless checked | Script keeps going, unless `set -e` |
| Divide by zero | `ZeroDivisionError` | `Infinity`, no error | Integer: panic. Float: `+Inf` | `division by 0` error |
| Index out of range | `IndexError` | `undefined`, no error | Panic | Empty string, no error |
| Crash for real | Uncaught exception | Uncaught exception | `panic("msg")` | `exit 1` |

In C, there are no exceptions at all. Functions report failure through their return value, like `-1` or `NULL`, and often set the global `errno` with the reason, so the caller checks after every call: `if (fp == NULL) { perror("fopen"); }`. Nothing forces that check, so a skipped one fails silently and the program keeps going with bad data. Dividing an integer by zero is not a catchable error either. It is undefined behavior, and on most systems the operating system kills the process. Python's exceptions do the checking automatically: an error cannot be ignored by accident, because it stops the program unless something handles it.

Three ideas carry over to every language:

1. **Errors are values or events, and both work.** Python and JavaScript throw, so an error jumps up to the nearest handler. Go and C return the error, so each caller checks it right there. Throwing keeps the happy path clean, while returning makes every failure point visible in the code.
2. **Fail loudly at the source.** Raising, throwing, or returning an error where the problem is found beats passing a bad value along. JavaScript's `undefined` for a missing index is the opposite, and the bug shows up later, far from the cause.
3. **Handle where you know what to do.** The function that finds a problem reports it. The caller, which knows the context, decides whether to retry, show a message, or stop.

## Interview framing

1. What is the difference between a syntax error and an exception?
2. How does `try`/`except` work? What happens to the code after the line that raised?
3. When should a function raise an exception instead of returning a value like `None`?
4. What is the difference between an error and a bug?
5. Why should a function usually not catch its own exceptions?
6. How does Python decide which `except` block runs, and why does the order matter?
7. Why is a bare `except` or `except Exception: pass` considered bad practice?

## My answer

**1. Syntax error versus exception**

"A syntax error means the code is not valid Python, like a missing colon or a sentence typed as code. Python finds it while reading the file, before anything runs, so the program cannot handle it. It has to be fixed in the source. An exception happens while valid code is running, like dividing by zero, reading a missing key, or a lost network connection. The code before it has already run, and the program can catch the exception with `try`/`except` and keep going. Technically `SyntaxError` is also an exception type, which is why code that runs other code, like `eval()`, can catch one, but in normal code they are not handled."

**2. How `try`/`except` works**

"Python runs the `try` block line by line. If every line finishes, the `except` blocks are skipped. If a line raises, the rest of the `try` block is skipped and Python checks the `except` blocks from top to bottom for one whose type matches. The first match runs, and the program continues after the whole statement. If none match, the exception keeps going up to the caller, and if nothing catches it all the way to the top, the program crashes with a traceback. The exception can come from a function called inside `try`, any number of levels down. `as e` gives me the exception object, which prints as its message. There is also `else`, which runs only if nothing was raised, and `finally`, which always runs."

**3. Raise versus return `None`**

"I raise when the function cannot do what it promised and the caller needs to know. A function like `craft_sword` that returns `None` for an unknown metal pushes the problem onto the caller, who may not check, and the `None` breaks something later, far from the cause. An exception stops at the exact line and cannot be ignored by accident. I return `None` when missing is a normal, expected answer, like a search that finds nothing, and the caller is expected to check for it. Dictionaries show both: `d[key]` raises a `KeyError`, while `d.get(key)` returns `None`, and the right one depends on whether a missing key is a mistake."

**4. Error versus bug**

"An error is something going wrong that the program can detect, like bad input, a missing file, or a timeout. Real programs hit errors constantly, and handling them is part of the job. A bug is when the program behaves in a way its users do not expect, like letting a player buy an item without enough gold. Raising an error is often how a bug is prevented: `purchase_item` raising `not enough gold` is correct behavior, and the bug was the version that let the purchase go through. An error that is handled the way users expect is not a bug. An error that crashes the app when it should have been handled is."

**5. Not catching your own exceptions**

"The function that detects a problem usually does not know the right response. If `craft_sword` catches its own `invalid metal bar` and prints it, it has decided for every caller that printing is the answer, and then it returns `None`, which is the silent failure the raise was meant to prevent. When it raises and lets the caller handle it, a game UI can show a message, a batch job can log and skip, and a test can check that the error happens. Catching inside the same function makes sense only when it can actually fix the problem, like retrying a network call or using a default, and even then I catch a specific type."

**6. Which `except` runs**

"Python checks the `except` blocks from top to bottom and runs the first one whose type matches. A block matches its own type and every type below it, so `except Exception` matches a `ZeroDivisionError` or an `IndexError`. That is why specific types go first. If `except Exception` comes first, it takes everything and the specific blocks below it never run, and Python does not warn about it. The match is only by type, never by the message, so `raise Exception("zero division")` is not caught by `except ZeroDivisionError`, because its type is the general `Exception`. That is also why libraries define their own exception types: callers catch the type, and the message is just for people to read."

**7. Catching too much**

"`except Exception: pass` hides every error, including the ones I did not expect, like a typo that raises a `NameError`. The program keeps running with bad state, and there is no traceback to show where it went wrong. A bare `except:` is worse, because it also catches `KeyboardInterrupt` and `SystemExit`, which are not `Exception` subclasses, so Ctrl+C can stop working. I catch the narrowest type I can actually handle, keep the `try` block small so it only covers the line that can fail, and if I really need a catch-all at the top of a program, I log the full exception instead of throwing it away."

**Points to recall**

- Syntax errors stop the file from running at all. Exceptions happen while valid code runs, and can be handled.
- An uncaught exception goes up through the callers and crashes the program with a traceback.
- `try` runs until it finishes or raises. On a raise, the rest of `try` is skipped and the matching `except` runs.
- After the `try`/`except`, the program continues normally.
- An exception raised inside a function called from `try` is still caught.
- `except Exception as e` stores the exception. `print(e)` shows its message. `e` is deleted after the block.
- `raise Exception("message")` stops the function like `return` does, so no `else` is needed after it.
- Raise when a function cannot do its job, instead of returning `None` and hoping someone checks.
- Errors are not bugs. A bug is behavior users do not expect.
- Raise in the function, handle in the caller. Do not catch your own exception in the same function.
- `except SomeType` catches that type and more specific ones, never more general ones.
- Python runs the first matching `except`. Put specific types first and `Exception` last.
- `except` matches by type, never by message.
- `ZeroDivisionError` from dividing by zero, `IndexError` from a bad list index, `KeyError` from a missing key.

## Follow-up gotchas

**Why can't `try`/`except` catch a syntax error in the same file?**
Python reads and compiles the whole file before running the first line. A syntax error stops that step, so the `try` statement never gets to run. A syntax error can only be caught when it happens later, while the program is already running, such as in code passed to `eval()` or a module imported inside a `try`.

**Why did the program crash even though there was an `except`?**
None of the `except` blocks matched the exception's type. `except ZeroDivisionError` does not catch an `IndexError`, and it does not catch `raise Exception("zero division")` either, because a plain `Exception` is more general. An unmatched exception keeps going up as if the `try` were not there. Adding `except Exception as e` at the end catches whatever the specific blocks miss.

**Why does `print(e)` sometimes show something unhelpful?**
`print(e)` shows only the message. For a `KeyError`, the message is just the key, so it prints `'a'` with no hint that it was a missing key. `Exception()` with no message prints an empty line. `repr(e)` shows the type and message together, like `KeyError('a')`, which is usually what to log.

**Why does the function return `None` after printing the error?**
When a function catches its own exception and only prints, the `except` block ends without a `return`, so the function returns `None`. The caller gets `None` and keeps going as if things worked. That is why the raise belongs in the function and the handling belongs in the caller, who can decide what to return or do.

**Why does `except Exception` not catch Ctrl+C?**
This is the "almost" in "almost all exceptions are an `Exception`." `KeyboardInterrupt` and `SystemExit` sit above `Exception`, under the more basic `BaseException`, so `except Exception` lets them through and the program can still be stopped. A bare `except:` with no type catches them too, which is one reason to avoid it.

**Why not wrap the whole function in one big `try`?**
A large `try` block catches errors from lines that were never expected to fail, and the handler cannot tell which line raised. A typo raising a `NameError` would be reported as "could not load player," and the real cause would be hidden. Keeping the `try` block to the line or two that can actually fail makes the handler's message true.

**Why raise for a negative player id when `players[-1]` works?**
Python accepts negative indexes and counts from the end, so `players[-1]` returns the last player instead of raising. For a list that is a feature, but a player id of `-1` is never valid, and quietly returning someone else's record is a bug. The function checks for that case itself and raises, because Python will not.

**Why did using `e` after the `except` block give a `NameError`?**
Python deletes the `as` name when the `except` block ends, even if a variable with that name existed before. It does this to free the exception and the traceback it holds. To keep the exception for later, assign it to another name inside the block, like `last_error = e`.
