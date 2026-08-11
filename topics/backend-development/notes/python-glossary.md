---
topic: Backend Development
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

### `__name__`

A variable Python automatically sets on every module the instant it's loaded, before any of that module's own code runs. Its value is `"__main__"` if the file was executed directly, or the module's filename (no extension, no dunders) if it was imported by another file. You never assign it yourself.

### `if __name__ == "__main__":`

A guard that lets a file behave as both a standalone script and a safely-importable module. Code inside the block only runs when the file is executed directly — not when another file imports it — because it's just a plain string comparison against a value Python already set before this line was reached. It doesn't set or cause anything; it only reads.

### `__pycache__/`

A directory Python creates automatically on import to store compiled bytecode (`.pyc` files), so later imports of an unchanged file skip recompiling from source. Unrelated to `__name__` despite the similar dunder-style naming — it's a disk-level build artifact for import performance, not a runtime variable. Standard practice: add it to `.gitignore`, never commit it.

### `import X` vs `from X import Y` vs `from X import *`

Two real choices for pulling code from one module into another, plus one to avoid:

- `import X` — access everything through `X.thing`. Preferred when importing several things from a module, or when names would otherwise collide (e.g. multiple modules each defining their own `main()`).
- `from X import Y` — pulls `Y` in directly, shorter calls. Preferred for a small number of distinct names. Risk: two `from` imports that grab a same-named thing silently overwrite each other.
- `from X import *` — wildcard, imports everything invisibly. Avoided in practice; makes collisions and origins hard to trace.

Which to use isn't a fixed rule — it depends on whether the names in play would collide.

### Return type hints (`-> T`)

A function's return type hint describes only what the `return` statement actually sends back — not the types of variables used internally. A function that builds an f-string out of `int`, `bool`, and `float` values still returns a plain `str`, since f-strings always produce a string regardless of what's interpolated into them.
