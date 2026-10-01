# 01: Introduction

> Source: boot.dev Learn Python, Ch. 1, L1–L8

## What it is

### A program is an ordered list of instructions
Code is a list of instructions the computer carries out one at a time, **from the top down**. Order is part of the meaning: the same lines in a different order make a different program. Nothing runs "all at once" — when output comes out in the wrong order, the instructions are in the wrong order.

### Output is how a program talks back
A program's work is invisible unless it shows you something. The simplest way is to write text to the **console** (the terminal, standard output). In Python that's `print()`. Printing is also the first debugging tool anyone uses: "what does the program think this value is right now?"

### Values and expressions
Programs work with **values**. The first two kinds you meet:

- **Strings** — text, wrapped in quotes: `"hello"`
- **Numbers** — no quotes: `42`

The quotes matter. `40 + 2` is an **expression** — something Python calculates down to a single value (`42`) *before* using it. `"40 + 2"` is just text, printed exactly as written.

### Syntax, and the three kinds of problems
**Syntax** is the grammar of a language: the rules for how code has to be written so the language can read it. Every language has its own grammar, but the ideas are the same everywhere.

Code can go wrong in three broad ways:

| Problem | Does it run? | Example |
|---|---|---|
| **Syntax error** | No — the language can't even read it | `print("hello)` — unclosed quote |
| **Logic error (bug)** | Yes, but does the wrong thing | `health + damage` where you meant `health - damage` |
| **Performance problem** | Yes, does the right thing, but too slowly | Checking every item in a huge list when a lookup would do |

Syntax errors are the cheapest kind: the language tells you exactly where they are. Logic errors are the expensive kind: nothing complains, the output is just wrong, and you have to notice.

### Run before you ship
Running code to see what it does is free. Shipping it to users is not. So the habit is: run it, check the output, *then* submit, merge, or deploy. This is the seed of everything later — tests, CI, staging environments — which are all just "run it before real users do," automated.

## Analogy
**Code is a recipe; the computer is a very literal cook.**

- The cook reads the recipe **one step at a time, top to bottom**, and does exactly what each step says. Swap two steps and you get a different dish.
- **The console** is the serving window — the only way you see what came out of the kitchen.
- **A syntax error** is a step the cook can't read at all ("Add 2 cups of"). Python's cook reads the *whole* recipe before starting, refuses an unreadable one, and cooks nothing.
- **A logic error** is a step that's perfectly readable but wrong ("add salt" where you meant sugar). The cook follows it happily; you only find out when you taste the dish.
- **A performance problem** is a recipe that works but takes six hours.
- **Run before submit** is tasting before you serve.

## Example
```python
# Instructions run top to bottom
print("one")
print("two")
print("three")

# Expression vs text: the quotes change everything
print(40 + 2)       # 42      -- calculated first, then printed
print("40 + 2")     # 40 + 2  -- just text

# print() accepts several values, separated by spaces in the output
print("Score:", 250 + 75)   # Score: 325

# Logic error: runs fine, wrong answer
health = 100
damage = 30
health = health + damage    # bug: should be health - damage
print(health)               # 130 -- no error, just wrong
```

And the difference in *when* errors show up — two files, both with a problem on line 2:

```python
# syntax.py
print("first line")
print("broken)          # SyntaxError: unterminated string literal
# Output: only the error. "first line" never prints —
# Python reads the whole file before running any of it.
```

```python
# typo.py
print("first line")
print(scroe)            # NameError: name 'scroe' is not defined
# Output: "first line", then the error.
# This is valid grammar — Python only finds out the name doesn't exist
# when it reaches that line.
```

## In other languages

| | Python | JavaScript (Node) | Go | Bash |
|---|---|---|---|---|
| Print a line | `print("hi")` | `console.log("hi")` | `fmt.Println("hi")` | `echo hi` |
| Run a file | `python3 app.py` | `node app.js` | `go run main.go` | `bash script.sh` |
| End of a statement | Newline | `;` or newline | Newline | Newline or `;` |
| Text in quotes | `"…"` or `'…'`, same thing | `"…"`, `'…'`, or `` `…` `` | `"…"` only (`'a'` is a single character) | `"…"` fills in variables, `'…'` doesn't |
| Syntax error on line 2 — does line 1 run? | No | No | No | **Yes** |
| Misspelled name on line 2 — does line 1 run? | Yes, then crashes | Yes, then crashes | **No** — rejected before running | Yes (empty value, often no error) |

The last two rows are the transferable idea: **languages differ in how early they catch mistakes.** Go checks the most up front; Python and JavaScript catch grammar early but names late; Bash runs line by line and catches very little. The earlier a language catches a mistake, the fewer reach users.

## Interview framing
- "Is Python compiled or interpreted? What actually happens when you run `python app.py`?"
- "What kinds of errors can a program have? When does Python catch each one?"
- "What's the difference between an expression and a statement?"
- "How do you make sure code is safe to deploy?"
- "How do you debug something? When would you use `print` vs a logger vs a debugger?"

## My answer
> _To write: say each of the interview questions above out loud, then write the version I'd actually give._

## Follow-up gotchas
- **"If Python is interpreted, why doesn't line 1 run when line 5 has a syntax error?"** — CPython first compiles the whole file to bytecode, then runs the bytecode. Grammar is checked during that compile step, so one syntax error anywhere stops the whole file. "Interpreted" describes how the bytecode is run, not that it reads source one line at a time.
- **"So does Python catch typos before running?"** — Only grammar typos. A misspelled variable name is valid grammar, so it's a runtime error (`NameError`) that only appears if that line actually runs. A typo in a branch that rarely runs can hide for months — one reason tests and linters (`ruff`, `mypy`) matter in Python more than in Go.
- **"Which is worse, a syntax error or a logic error?"** — A logic error. A syntax error stops the program and points at the line. A logic error runs successfully and returns a wrong answer that someone has to notice.
- **"Why not just debug with `print`?"** — It's fine for quick checks, but prints have to be added and removed by hand, have no levels or timestamps, and can't be switched off in production. Real services use a logger (`logging`), and a debugger lets you pause and inspect without changing the code.
