# Beginner

Small, self-contained scripts. Each one should be completable in a sitting and target one concept or a tight cluster of them (variables/types, functions, loops, lists, dicts, ...) — no dependency on any other exercise here.

## Ideas

- [x] Calculator — arithmetic operators, functions, input parsing
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

## Suggested order

Matches these drills to the course chapter that teaches what each one needs, so review and practice stay paired instead of piling up at the end. Cross-reference: [`topics/python/notes/python-basics.md`](../../../topics/python/notes/python-basics.md).

| After reviewing... | Build |
|---|---|
| CH1-3 (Intro, Variables/Types, Functions) | Calculator |
| CH5 (Testing and Debugging) | Bug Hunt — also covers CH4 (Scope) via the planted `UnboundLocalError` bug |
| CH6-7 (Computing, Comparisons) | Number guessing game |
| CH8 (Loops) | reinforced by Number guessing game — no new build |
| CH9 (Lists, incl. Tuples) | Quiz game, Tic-tac-toe, then Coordinate distance calculator for the tuples subsection |
| CH10 (Dictionaries) | reinforced by Quiz game/Tic-tac-toe if built dict-based — no new build |
| CH11 (Sets) | Hangman |
| CH12 (Errors) | Safe calculator / input validator |
| CH13 (Type Hints) | Type hint retrofit |
| CH14 (Practice) | Test harness practice — the `test_cases.py` pattern is worked out concretely in 14.7/14.8, so it lands better here than right after CH5 |
| Anytime, low priority | Weather CLI — needs an external API, beyond the course notes |
