# 01: Introduction

Source: boot.dev Learn Python, Chapter 1, Lessons 1 to 11.

## What it is

### What Python is

Python is a high-level, general-purpose programming language created by Guido van Rossum and first released in 1991. A few traits define it:

- **High-level:** it handles memory management and other low-level details automatically.
- **Readable:** indentation defines code blocks instead of braces, so the structure of the code is visible at a glance.
- **Dynamically typed:** variables do not declare a type. The type belongs to the value and is checked while the program runs.
- **Compiled to bytecode, then interpreted:** the standard implementation, CPython, compiles source code to bytecode and runs it on a virtual machine. There is no separate build step for the developer.

Python is designed to be quick to write and easy to read, which makes it a common first language. Its simplicity does not limit it, and it is widely used in industry.

| Strong fit | Weak fit |
|---|---|
| Backend web services and APIs | Frontend web development, because browsers run JavaScript |
| DevOps, cloud automation, and infrastructure tooling | Mobile apps, which typically use Swift or Kotlin |
| Data analysis and machine learning | Desktop graphical interfaces |
| Scripting and task automation | CPU-intensive or latency-sensitive systems, where Go, Rust, or C++ are more common |

Choosing a language is a tradeoff. Python favors developer speed and a large library ecosystem over raw execution speed.

### Programs run in order

A program is a list of instructions that the computer executes one at a time, from top to bottom. The order is part of the program's meaning. If output appears in the wrong order, the instructions are in the wrong order.

### Output

A program's work is invisible unless it produces output. The simplest form of output is text written to the console, also called standard output. In Python this is done with `print()`. Printing values is also the most basic debugging technique, because it shows what the program holds at a specific point.

### Values and expressions

Programs operate on values. The first two types of values are:

- **Strings:** text enclosed in quotes, such as `"hello"`.
- **Numbers:** written without quotes, such as `42`.

An expression is any piece of code that evaluates to a single value. `40 + 2` is an expression that Python evaluates to `42` before passing it to `print()`. `"40 + 2"` is a string, so it is printed exactly as written.

### Syntax and types of errors

Syntax is the set of rules that defines how valid code is written in a language. Each language has its own syntax, but the underlying ideas are shared.

| Error type | Does the program run? | Example |
|---|---|---|
| Syntax error | No. The code cannot be parsed. | `print("hello)` has an unclosed quote. |
| Logic error | Yes, but the result is wrong. | `health + damage` when `health - damage` was intended. |
| Performance issue | Yes, and the result is correct, but it is too slow. | Scanning a large list item by item when a direct lookup would work. |

Syntax errors are the easiest to fix because the interpreter reports the exact location. Logic errors are harder because nothing fails. The output is simply incorrect, and someone has to notice it.

### Test before deploying

Running code locally costs nothing, while shipping broken code to users does. The habit to build is to run the code and check its output before submitting, merging, or deploying. Automated tests, CI pipelines, and staging environments are formal versions of the same habit.

## Analogy

A program is a recipe, and the computer is a cook that follows instructions literally.

- The cook reads one step at a time, from top to bottom. Changing the order of the steps changes the result.
- The console is the serving window. It is the only place you can see what the kitchen produced.
- A syntax error is a step the cook cannot read, such as "Add 2 cups of". Python reads the entire recipe before starting, so one unreadable step means nothing gets cooked.
- A logic error is a step that is readable but wrong, such as "add salt" when sugar was intended. The cook follows it, and the problem only shows up when someone tastes the dish.
- A performance issue is a recipe that produces the right dish but takes six hours.
- Testing before deploying is tasting the dish before serving it.

## Example

```python
# Instructions run from top to bottom
print("one")
print("two")
print("three")

# Expression versus string
print(40 + 2)       # 42: evaluated first, then printed
print("40 + 2")     # 40 + 2: printed as written

# print() accepts several values and separates them with spaces
print("Score:", 250 + 75)   # Score: 325

# Logic error: the program runs, but the result is wrong
health = 100
damage = 30
health = health + damage    # Bug: should be health - damage
print(health)               # 130
```

The two files below each have a problem on line 2, but they fail at different times.

```python
# syntax.py
print("first line")
print("broken)          # SyntaxError: unterminated string literal

# Output: only the error. "first line" is never printed,
# because Python parses the whole file before running any of it.
```

```python
# typo.py
print("first line")
print(scroe)            # NameError: name 'scroe' is not defined

# Output: "first line", followed by the error.
# The line is grammatically valid, so Python only discovers
# that the name does not exist when it reaches that line.
```

## In other languages

| | Python | JavaScript (Node) | Go | Bash |
|---|---|---|---|---|
| Print a line | `print("hi")` | `console.log("hi")` | `fmt.Println("hi")` | `echo hi` |
| Run a file | `python3 app.py` | `node app.js` | `go run main.go` | `bash script.sh` |
| End of a statement | Newline | Semicolon or newline | Newline | Newline or semicolon |
| String quotes | `"..."` and `'...'` are equivalent | `"..."`, `'...'`, or `` `...` `` | `"..."` only; `'a'` is a single character | `"..."` expands variables; `'...'` does not |
| Syntax error on line 2: does line 1 run? | No | No | No | Yes |
| Misspelled name on line 2: does line 1 run? | Yes, then it fails | Yes, then it fails | No. It is rejected at compile time. | Yes. The name expands to an empty value, usually without an error. |

The main takeaway is that languages differ in how early they catch mistakes. Go checks the most before the program runs. Python and JavaScript check syntax up front but only resolve names at runtime. Bash executes line by line and checks very little. The earlier a language catches a mistake, the fewer mistakes reach users.

## Interview framing

1. What is Python, why use it, and when would you choose a different language?
2. Is Python compiled or interpreted? What happens when you run `python app.py`?
3. What kinds of errors can a program have, and when does Python catch each one?
4. What is the difference between an expression and a statement?
5. How do you make sure code is safe to deploy?
6. How do you debug a problem? When would you use `print`, a logger, or a debugger?

## My answer

**1. What is Python, and when would you choose something else?**

"Python is a high-level, general-purpose language that is dynamically typed and compiled to bytecode before it runs. Its main strengths are readability and its ecosystem. Code is quick to write and easy for others to read, and there are mature libraries for almost everything: Django and FastAPI for web services, boto3 and Ansible for cloud and automation, and pandas and PyTorch for data work. The tradeoffs are speed and concurrency. Python is slower than compiled languages, and in the default CPython build the global interpreter lock prevents threads from running Python code in parallel. For CPU-heavy or latency-sensitive services, or for infrastructure tools that should ship as a single binary, I would consider Go or Rust. For browser frontends the standard is JavaScript or TypeScript, and for mobile it is Swift or Kotlin."

**2. Is Python compiled or interpreted?**

"Both, in a way. When I run `python app.py`, CPython first compiles the source code into bytecode, which is a simpler set of instructions. The Python virtual machine then executes that bytecode one instruction at a time. So the interpreted part is the execution, not the reading of the source file. You can see this in practice: if a file has a syntax error on line 50, line 1 never runs, because the compile step fails before anything executes."

**3. What kinds of errors can a program have?**

"I group them into four. Syntax errors break the language's grammar, and Python catches them at compile time, before any code runs. Runtime errors happen in valid code while it is running, such as a `NameError` from a misspelled variable or a `TypeError` from adding a string to a number. Python only catches those when it reaches the line. Logic errors are the hardest, because the program runs without complaint and simply produces the wrong result. Nothing catches those automatically except tests. Finally, performance issues are cases where the result is correct but the code is too slow."

**4. Expression versus statement?**

"An expression is anything that evaluates to a value, such as `40 + 2`, a string, or a function call. A statement is a complete instruction that performs an action, such as an assignment, an `if` block, or a `return`. Statements often contain expressions. A quick test is whether it can go on the right-hand side of an equals sign. If it can, it is an expression."

**5. How do you make sure code is safe to deploy?**

"By catching problems as early as possible, in layers. Locally, I run the code and the tests before I push. Linters and type checkers such as `ruff` and `mypy` catch mistakes that Python would otherwise only find at runtime. In CI, the same checks run automatically on every pull request, and code review adds a second person. The change then goes to a staging environment that mirrors production. If something still gets through, monitoring and a fast rollback limit the impact."

**6. How do you debug?**

"I use `print` for quick checks while developing, when I only need to see a value. For anything that runs in a real environment I use the `logging` module, because logs have levels and timestamps and can be adjusted without changing the code. For harder problems I use a debugger, such as `pdb` or the one in my editor, so I can pause execution, inspect the state, and step through the code line by line."

**Points to recall**

- Python trades execution speed for readability and ecosystem. It is strong in backend, DevOps, data, and scripting, and weak in frontend, mobile, and CPU-heavy systems.
- Python compiles source code to bytecode, then interprets the bytecode.
- A syntax error stops the entire file. A runtime error stops at the line where it occurs.
- Expressions produce values. Statements perform actions.
- Deploy safely in layers: local tests, linters, CI, code review, staging, monitoring.
- Use `print` for quick checks, `logging` in real environments, and a debugger for difficult problems.

## Follow-up gotchas

**If Python is interpreted, why doesn't line 1 run when line 5 has a syntax error?**
CPython compiles the whole file to bytecode before running it, and syntax is checked during that step. A single syntax error anywhere in the file prevents all of it from running. "Interpreted" describes how the bytecode is executed, not that the source is read one line at a time.

**Does Python catch typos before running?**
Only typos that break the syntax. A misspelled variable name is still valid syntax, so it becomes a runtime error (`NameError`) that only appears if that line runs. A typo inside a rarely used branch can go unnoticed for a long time. This is one reason tests and linters matter more in Python than in a compiled language like Go.

**Which is worse, a syntax error or a logic error?**
A logic error. A syntax error stops the program and points to the exact line. A logic error runs successfully and returns a wrong result that someone has to notice.

**What does `"10" + "20"` return?**
`"1020"`, not `30`. Both values are strings, so `+` joins them as text instead of adding them. This causes real bugs because values from user input, files, and environment variables always arrive as strings. Convert them first: `int("10") + int("20")` returns `30`.

**Why not debug everything with `print`?**
Print statements have to be added and removed by hand, have no levels or timestamps, and cannot be turned off in production. Services use a logger instead, and a debugger allows inspecting state without modifying the code.
