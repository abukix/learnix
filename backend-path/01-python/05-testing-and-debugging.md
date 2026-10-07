# 05: Testing and Debugging

Source: boot.dev Learn Python, Chapter 5, Lessons 1 to 6.

## What it is

### Unit tests

A unit test is a small, automated program that checks one unit of code, usually a single function. It calls the function with known inputs and compares the return value with the expected result. If they match, the test passes. If they do not, the test fails and reports what it got instead.

Tests live in a separate file from the code they check. A common layout is `main.py` for the code and `main_test.py` (or `test_main.py`) for the tests. Python's standard library includes the `unittest` module for writing them:

```python
# main.py
def total_xp(level, xp_to_add):
    return level * 100 + xp_to_add
```

```python
# main_test.py
import unittest

from main import total_xp


class TestMain(unittest.TestCase):
    def test_total_xp(self):
        self.assertEqual(total_xp(1, 100), 200)
        self.assertEqual(total_xp(2, 250), 450)
        self.assertEqual(total_xp(170, 590), 17590)


if __name__ == "__main__":
    unittest.main()
```

Running `python3 main_test.py` runs every method whose name starts with `test` and prints a summary.

There are two ways to check whether code works:

- **Checking output** compares what the program prints to the console with an expected text. It breaks as soon as anything else is printed, including debug prints.
- **Checking return values** calls functions directly and compares what they return. Console output is ignored, so debug prints can stay in while working.

Unit tests check return values. This is one more reason, after `print` versus `return` in Chapter 3, for functions to return their results instead of printing them: a returned value can be tested, while a printed one can only be read.

### Edge cases and hidden tests

A function can pass the tests its author thought of and still fail on inputs nobody tried. Those unusual inputs are called edge cases: zero, negative numbers, empty strings, empty lists, very large values, or a missing value.

The course splits tests into two groups: running the code shows a few tests, and submitting it runs more. This mirrors real work. The tests run locally are the ones the developer wrote, while production is where real users send inputs the developer did not expect. Good tests try to cover those cases before users find them. Before calling a function finished, it is worth asking what happens with the smallest, largest, and emptiest possible inputs.

### Debugging

Debugging is finding and fixing the reasons code does not do what it should. Professional developers run and test their code locally before it is deployed to users, and fixing problems at that stage is cheap compared with fixing them after users are affected.

The simplest debugging tool is `print()`. The loop is:

1. Write a line that calculates a value.
2. `print()` that value.
3. Run the code.
4. If the printed value is not what was expected, fix it.
5. Repeat for the next piece.

The key is to write and check small amounts of code at a time. A bug in three new lines is easy to find, while a bug somewhere in a hundred untested lines is not. Senior engineers work in small steps too.

Two techniques help:

- **Stubbing.** Python does not allow an empty function body. Returning placeholder values, such as `return None, None` for a function that will return two values, makes the code runnable straight away. Each placeholder is then replaced with the real value once it has been checked.
- **Printing intermediate values.** Instead of only checking the final result, print each value along the way. The first value that looks wrong shows where the bug is.

`print()` is not the only option. Python has a built-in debugger: calling `breakpoint()` pauses the program at that line and allows inspecting variables, stepping through lines, and continuing. Editors like VS Code offer the same features with a graphical interface.

### A process for hard problems

The course suggests a repeatable process for solving problems:

1. Read the explanation and understand the examples before writing anything.
2. Read the task and be clear about the goal: the inputs, the expected output, and the rules.
3. Start writing code, a small piece at a time.
4. Print, run, and fix after each piece, until confident it works.
5. Run the full tests.
6. Compare the finished code with another solution to learn other approaches.

When stuck, ask for a hint before looking at a full solution. Looking at answers too often skips the part where the learning happens. If getting stuck is happening all the time, the better move is to go back and redo the earlier material.

### Stack traces

A stack trace, or traceback, is the error report Python prints when something goes wrong. It shows the path the interpreter took through the code to reach the error, and it is the first thing to read when debugging.

A syntax error stops the file before any of it runs, so the trace is short:

```
  File "main.py", line 3
    msg = f"You have {total} stats.
          ^
SyntaxError: unterminated f-string literal (detected at line 3)
```

- `File "main.py", line 3` is where the problem was found.
- The next line is the code itself, with a `^` marker pointing at the spot.
- The last line is the error type and a description. This is the most important line, so read it first.

The reported line is where Python noticed the problem, which is not always where the mistake is. An inconsistent indentation on line 2 can be reported on line 3, because Python only notices the mismatch when the next line does not line up. If the reported line looks correct, check the lines just above it. Indentation mistakes are reported as `IndentationError`, which is a kind of `SyntaxError`. Standard Python indentation is 4 spaces per level.

An error that happens while the program is running, called a runtime error or exception, gives a longer trace that lists every function call that led to the error:

```
Traceback (most recent call last):
  File "main.py", line 15, in <module>
    main()
  File "main.py", line 12, in main
    print(report([]))
  File "main.py", line 6, in report
    average = get_average(sum(scores), len(scores))
  File "main.py", line 2, in get_average
    return total / count
ZeroDivisionError: division by zero
```

"Most recent call last" means the trace reads from the outside in: the top entry is where the program started, and the bottom entry is where it failed. The reading order is the opposite:

1. Read the last line for the error type and message: dividing by zero.
2. Read the entry just above it for where it happened: `get_average`, line 2.
3. Read upward through the calls to find where the bad value came from: `main` passed an empty list to `report`, which passed a count of `0` to `get_average`.

The line that crashed is often fine. The fix belongs where the bad value was created or should have been handled, here in `report` or `main`.

## Analogy

Continuing the kitchen from Chapters 1 to 4: **testing and debugging are tasting the food before it leaves the kitchen.**

- A unit test is a taste test for a single recipe card. Make the sauce with known ingredients, taste it, and compare it with how it should taste. It does not care what the cook said while cooking, only what ended up in the pot.
- Checking console output is judging the dish by what the cook announces. Any extra chatter spoils the result.
- Edge cases are the unusual orders: no salt, a double portion, a customer with an allergy. The kitchen's own tasting covers the usual orders, but the dining room (production) sends whatever it wants.
- Debugging with `print()` is tasting at every step: after the onions, after the tomatoes, after the spices. If it only gets tasted at the end, nobody knows which step went wrong.
- Stubbing is putting an empty plate on the pass so service can be rehearsed before the dish exists.
- A stack trace is the kitchen's incident report: "The dish was sent back. Dessert station, step 2, burnt sugar. Dessert was ordered by the head chef, who was filling table 4's order." Read the problem first, then follow the chain back to find who sent the bad ingredients.

## Example

```python
# main.py: the code under test
def total_xp(level, xp_to_add):
    return level * 100 + xp_to_add


def take_magic_damage(health, resist, amp, spell_power):
    damage = spell_power * amp - resist
    return health - damage


def unlock_achievement(before_xp, ach_xp, ach_name):
    after_xp = before_xp + ach_xp
    alert = f"Achievement Unlocked: {ach_name}"
    return after_xp, alert
```

```python
# main_test.py: checks return values, not printed output
import unittest

from main import total_xp, take_magic_damage, unlock_achievement


class TestMain(unittest.TestCase):
    def test_total_xp(self):
        self.assertEqual(total_xp(1, 100), 200)
        self.assertEqual(total_xp(2, 250), 450)
        self.assertEqual(total_xp(170, 590), 17590)

    def test_total_xp_level_zero(self):         # an edge case
        self.assertEqual(total_xp(0, 0), 0)

    def test_take_magic_damage(self):
        self.assertEqual(take_magic_damage(100, 5, 2, 10), 85)

    def test_unlock_achievement(self):
        self.assertEqual(
            unlock_achievement(10, 5, "First Blood"),
            (15, "Achievement Unlocked: First Blood"),
        )


if __name__ == "__main__":
    unittest.main()
```

Running `python3 main_test.py -v`:

```
test_take_magic_damage (__main__.TestMain.test_take_magic_damage) ... ok
test_total_xp (__main__.TestMain.test_total_xp) ... ok
test_total_xp_level_zero (__main__.TestMain.test_total_xp_level_zero) ... ok
test_unlock_achievement (__main__.TestMain.test_unlock_achievement) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

If `unlock_achievement` had a bug, such as `before_xp - ach_xp`, the failing test reports both values:

```
AssertionError: Tuples differ: (5, 'Achievement Unlocked: First Blood') != (15, 'Achievement Unlocked: First Blood')

First differing element 0:
5
15
```

A quick check without a test framework uses `assert`, which raises an `AssertionError` when the condition is false:

```python
from main import total_xp

assert total_xp(1, 100) == 200
assert total_xp(1, 100) == 300, "level 1 plus 100 xp"   # AssertionError: level 1 plus 100 xp
```

Building a function in small, checked steps:

```python
# Step 1: a stub, so the code runs at all
def unlock_achievement(before_xp, ach_xp, ach_name):
    return None, None

# Step 2: calculate one value and print it to check it
def unlock_achievement(before_xp, ach_xp, ach_name):
    after_xp = before_xp + ach_xp
    print("After xp:", after_xp)
    return after_xp, None

# Step 3: the next value, checked the same way
def unlock_achievement(before_xp, ach_xp, ach_name):
    after_xp = before_xp + ach_xp
    alert = f"Achievement Unlocked: {ach_name}"
    return after_xp, alert
```

Common errors:

```python
def unlock_achievement(before_xp, ach_xp, ach_name):

print(1)            # IndentationError: expected an indented block after function definition on line 1

def get_msg(strength, wisdom, dexterity):
      total = strength + wisdom + dexterity     # 6 spaces: the actual mistake
    msg = f"total {total}"                      # IndentationError: unindent does not match any outer indentation level
    return msg

msg = f"You have {total} stats.                 # SyntaxError: unterminated f-string literal
```

## In other languages

| | Python | JavaScript | Go | Bash |
|---|---|---|---|---|
| Built-in test tool | `unittest` module | `node:test` module, run with `node --test` | `testing` package, run with `go test` | None |
| Popular alternative | pytest | Jest, Vitest | testify | bats |
| Test file naming | `test_*.py` or `*_test.py` | `*.test.js` | `*_test.go`, required | `*.bats` |
| Assert a value | `self.assertEqual(a, b)` or `assert a == b` | `assert.equal(a, b)` | `if got != want { t.Errorf(...) }` | `[[ "$a" == "$b" ]]` |
| Print debugging | `print()` | `console.log()` | `fmt.Println()` | `echo`, or `set -x` to print every command as it runs |
| Built-in debugger | `breakpoint()` (pdb) | `debugger;` with `node inspect` | Delve (`dlv`) | None |
| Error trace order | Most recent call last: read from the bottom | Error first, then calls from innermost to outermost: read from the top | Panic message first, then goroutine stack, innermost first | No trace by default. `${FUNCNAME[@]}` and `$LINENO` can be printed manually |
| Syntax errors | Caught before the file runs | Caught before the file runs | Caught at compile time | Often found only when that line is reached |

Two ideas carry over to every language:

1. **Test return values, not output.** Every test framework works by calling code and comparing what comes back. Code that computes a value and returns it is easy to test in any language. Code that only prints is not.
2. **Find the error line, then the cause.** Every language reports where the program failed, but the order varies. Python puts the failing line at the bottom, while JavaScript and Go put it at the top. In all of them, the crash location and the real cause are often different places.

## Interview framing

1. What is a unit test, and why write them?
2. What makes a good unit test?
3. What are edge cases? Give examples.
4. How do you approach debugging a problem?
5. How do you read a Python traceback?
6. What is the difference between a syntax error and a runtime error?

## My answer

**1. What is a unit test?**

"A unit test is automated code that checks one small unit, usually a single function, in isolation. It calls the function with known inputs and asserts that the result matches the expected value. Tests catch bugs before users do, they let me refactor safely because a change that breaks behavior fails a test right away, and they document how a function is meant to be used. In Python, I would use `unittest` from the standard library or pytest."

**2. A good unit test**

"A good unit test checks one behavior and has a name that says which one, so a failure tells me what broke without reading the code. It is fast and deterministic, meaning it gives the same result every time and does not depend on the network, the clock, or other tests. It tests through the function's inputs and return value rather than its internal details, and it covers edge cases, not only the normal case. A common structure is arrange, act, assert: set up the inputs, call the function, and check the result."

**3. Edge cases**

"Edge cases are inputs at the limits of what a function handles, where bugs are most likely. For numbers, that means zero, negatives, and very large values. For strings and lists, it means empty values and single items. In general, it means missing values like `None` and inputs at the exact boundary of a condition, such as when a value is exactly equal to a limit. A function that averages a list works for `[90, 80]` but crashes with `ZeroDivisionError` on an empty list, and that is exactly the kind of case a test should cover."

**4. Approaching debugging**

"First, I reproduce the bug reliably, ideally as a failing test. Then I read the error message and traceback carefully, starting from the error type at the bottom. To narrow it down, I check intermediate values with prints or a debugger, `breakpoint()` in Python, until I find the first value that is wrong. Once I understand the cause, I fix it, confirm the test passes, and keep the test so the bug cannot come back. While writing new code, I avoid most of this by working in small steps and checking each one."

**5. Reading a traceback**

"I start at the last line, which gives the error type and message, such as `ZeroDivisionError: division by zero`. The entry just above it shows the file, line, and function where the error happened. Then I read upward through the call chain to see how the program got there. The line that crashed often just received a bad value, so the real fix is usually further up, where that value was created or should have been checked. The traceback is ordered most recent call last, so the top is the program's entry point."

**6. Syntax errors versus runtime errors**

"A syntax error means the code is not valid Python, such as a missing quote or inconsistent indentation. Python finds it while reading the file, before running anything, so none of the file runs. A runtime error, or exception, happens while valid code is running, such as dividing by zero or using an undefined name, and the code before it has already run. Syntax errors are reported where Python noticed the problem, which can be a line after the real mistake."

**Points to recall**

- A unit test calls a function with known inputs and checks the return value.
- Tests check return values, so debug prints do not affect them.
- Edge cases are the limits: zero, negatives, empty values, `None`, and exact boundaries.
- Write code in small steps, and print or test each one before moving on.
- Stub a function with placeholder return values to make it runnable early.
- `breakpoint()` opens Python's built-in debugger.
- Read a traceback from the bottom: error type first, then where, then how it got there.
- The reported line is where the error was noticed, not always where the mistake is.
- Syntax errors stop the whole file before it runs. Runtime errors happen partway through.

## Follow-up gotchas

**Why is the error reported on line 3 when the mistake is on line 2?**
Python reports where it noticed the problem. With bad indentation, it only realizes the indentation is inconsistent when the next line does not line up with any earlier level. With an unclosed quote or bracket, the error may appear even further down. If the reported line looks fine, check the lines above it.

**Should you use `assert` in production code?**
Not for checking user input or anything that must always run. Running Python with the `-O` flag removes `assert` statements entirely, so a check written with `assert` can silently disappear. Use `assert` in tests and for internal sanity checks, and raise a proper exception, such as `ValueError`, for input validation.

**If all the tests pass, is the code correct?**
No. Passing tests only prove that the code works for the cases that were tested. The hidden tests in the course show the same idea: code that passes the visible tests can still fail on inputs nobody checked. Tests reduce risk, but they do not prove the absence of bugs.

**Why not leave debug prints in the code?**
In code that is tested by return values, they do not break anything, but they clutter the output and can leak sensitive data into logs. Remove them once the bug is found. For messages that should stay, use the `logging` module, which can be turned up or down without changing the code.

**What is the difference between a unit test and an integration test?**
A unit test checks one function in isolation. An integration test checks that several parts work together, such as code that talks to a real database. Unit tests are fast and pinpoint failures. Integration tests are slower but catch problems that only show up when the parts are combined. A healthy project has many unit tests and fewer integration tests.

**Why is `IndentationError` reported when the course says `SyntaxError`?**
`IndentationError` is a subclass of `SyntaxError`, so both descriptions are correct. Recent Python versions report the more specific name. Catching or reasoning about `SyntaxError` also covers indentation problems.
