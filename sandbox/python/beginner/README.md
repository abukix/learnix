# Beginner

Small, self-contained scripts. Each one should be completable in a sitting and target one concept or a tight cluster of them (variables/types, functions, loops, lists, dicts, ...) — no dependency on any other exercise here.

## Ideas

- [ ] Calculator — arithmetic operators, functions, input parsing
- [ ] Quiz game — lists/dicts of questions, loops, score tracking
- [ ] Tic-tac-toe — 2D state (list of lists or dict), win-condition logic, loops
- [ ] Weather CLI — functions, f-strings, (later) working with an external API
- [ ] Hangman — sets (guessed letters), string indexing, loops
- [ ] Number guessing game — loops, comparisons, `while`; needs the `random` module, which isn't in the course notes yet — small, self-explanatory addition (`random.randint()`), not a gap worth a detour
- [ ] Coordinate distance calculator — `(x, y)` tuples, tuple unpacking, a `distance()` function; isolated rehearsal of what Party Manager Day 7 will ask for
- [ ] Safe calculator / input validator — `try`/`except` around bad input (`ZeroDivisionError`, invalid values), one custom exception; isolated rehearsal of error handling before it's bundled into a bigger project
- [ ] Bug hunt — a short script with 3-5 deliberately planted bugs (off-by-one in a `range`, `=` instead of `==`, an unwanted mutation, a `PARTY_GOLD`-style `UnboundLocalError` from a compound-assignment scope bug, ...) to find and fix via print-statement debugging, not by being told where they are; rehearses CH5's debugging process, and folds in CH4 (Scope) since nothing else here drills it
- [ ] Test harness practice — pick 2-3 already-written functions from the drills above and write a hand-rolled `test_cases.py`-style harness for them (list of input/expected-output pairs, looped, PASS/FAIL) — same TDD flow as Party Manager Day 11, rehearsed early on a small scale
- [ ] Type hint retrofit — pick 2-3 already-written functions from the drills above that don't have type hints yet and add them (parameter types, return type, container types, `| None` where it applies) — same move as Party Manager Day 10, rehearsed early on a couple of functions instead of nine at once
