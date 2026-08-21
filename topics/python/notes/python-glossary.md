---
topic: Python
source: Party Manager challenge (self-designed)
date: 2026-08-11
status: growing
---

# Python glossary — interview prep

Quick-recall definitions built while working through the Party Manager project (`sandbox/python/`). Written to be *answerable out loud*, not just recognized.

## Day 1 — Character sheet

### Variable

A named reference to a value stored in memory, created the moment you assign something to it (`name = "JC"`). Python is dynamically typed, so a variable isn't locked to the type it started with — the same name can be reassigned to a completely different type later, though doing so on purpose is usually a sign something's off.

### Type hint (annotation)

Optional syntax (`name: str = "JC"`, or `-> str` on a function) that documents the intended type of a variable, parameter, or return value. Not enforced by Python at runtime — the program will still run even if you assign a mismatched value — but tools like mypy or your editor read hints to catch type mismatches before the code ever executes.

### f-string

A string literal prefixed with `f` (`f"{name} | Lvl {level}"`) that lets you embed expressions directly inside `{}` braces; each one is evaluated and converted to text inline when the string is built. Whatever type the expression is (`int`, `bool`, `float`, ...), the result of the whole f-string is always a plain `str` — which is exactly why a function returning one should be type-hinted `-> str`, not a union of every type used inside it.

> `__name__`, the `if __name__ == "__main__":` guard, `__pycache__/`, and the `import X` vs. `from X import Y` vs. `from X import *` choice all moved to [python-cheatsheet.md](python-cheatsheet.md)'s "Beyond the course notes" section on 2026-08-21 — same content, one home instead of two.

### Return type hints (`-> T`)

A function's return type hint describes only what the `return` statement actually sends back — not the types of variables used internally. A function that builds an f-string out of `int`, `bool`, and `float` values still returns a plain `str`, since f-strings always produce a string regardless of what's interpolated into them.

## Day 2 — Functions

### Parameters vs. hardcoded values

A function's parameters are placeholders that receive whatever values are passed in at call time — they don't reach out and grab data from anywhere else. Writing `create_character(name, hp, level, luck)` and then ignoring `name`/`hp`/`level`/`luck` inside the body (e.g. calling some other hardcoded function instead) means the arguments passed in are silently discarded; the function's output stops depending on its inputs at all.

### `return` vs. `print`

`return` hands a value back to whatever called the function, so the caller decides what to do with it (print it, store it, pass it on). `print` just writes text to the screen and gives the caller `None` back. A function documented to *return* a formatted string must not print it internally — printing is the caller's job, done separately after the call.

> The dict literal keys-vs-values mistake (`{name: str}` vs. `{"name": name}`) moved to [python-cheatsheet.md](python-cheatsheet.md)'s CH10 Dictionaries section on 2026-08-21.

### Dict key access (`d["key"]`)

Square-bracket indexing on a dict looks up the value stored under that exact key, e.g. `character["hp"]` retrieves whatever was stored at `"hp"` when the dict was built. It's the mirror image of building the dict in the first place — construction uses `{"key": value}`, retrieval uses `d["key"]`.

### Tuple-by-comma inside an f-string placeholder

Inside an f-string's `{}`, a comma-separated list of expressions isn't several separate values — it's a single tuple. `f"{a, b, c}"` interpolates one thing: the tuple `(a, b, c)`, printed with its parens and commas intact. To interpolate several values with custom text between them, each one needs its own `{}` placeholder, with the literal separator text typed outside the braces: `f"{a} | {b} | {c}"`.

### Nested quotes inside f-strings (PEP 701, Python 3.12+)

Historically, an f-string couldn't reuse its own quote character inside its `{}` expressions (`f"{d["key"]}"` was a `SyntaxError`) — the string literal parsing and the expression parsing weren't independent. PEP 701 (Python 3.12+) removed that restriction, so `f"{d["key"]}"` is now valid: the same quote character can appear both as the string's delimiter and inside the embedded expression. Code relying on this isn't portable to pre-3.12 interpreters.

## Day 3 — Scope

> The full Day 3 scope writeup (local vs. global, compile-time local-variable detection, `UnboundLocalError`, compound assignment, `global`, return-and-reassign vs. in-place mutation) moved to [python-cheatsheet.md](python-cheatsheet.md)'s CH4 Scope card on 2026-08-21, with the `PARTY_GOLD` trace inlined there directly. That card's example previously pointed at `sandbox/python/day03_scope.py`, which no longer exists after the sandbox reset — the cheat sheet's version is self-contained and doesn't depend on that file.
