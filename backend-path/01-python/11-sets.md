# 11: Sets

Source: boot.dev Learn Python, Chapter 11, Lessons 1 to 4.

## What it is

### Sets

A set is a collection like a list, with two differences: it is unordered, and every value in it is unique. A set can hold only one of each value, so adding a duplicate does nothing.

A set is written with curly braces like a dictionary, but with plain values instead of `key: value` pairs:

```python
fruits = {"apple", "banana", "grape"}
print(type(fruits))    # <class 'set'>
print(fruits)          # {'banana', 'apple', 'grape'}
```

The printed order is not the order the values were written in. Python arranges a set by the hash of each value, the same way a dictionary arranges its keys, so the order can differ from one run to the next. For strings it does differ, because string hashes are randomized each time Python starts. Code should never depend on the order of a set.

A duplicate in the literal is dropped without an error:

```python
len({"apple", "apple", "banana"})    # 2
```

Like dictionary keys, set values must be hashable, so a list cannot go in a set (see Follow-up gotchas).

### An empty set

`{}` is an empty dictionary, not an empty set, because dictionaries had the curly braces first. An empty set is made with `set()`:

```python
type({})       # <class 'dict'>
type(set())    # <class 'set'>
```

An empty set also prints as `set()`, for the same reason.

### Adding with `.add()`

`.add()` puts one value into a set. It is the set version of a list's `.append()`, though there is no "end" for the value to go on:

```python
fruits = {"apple", "banana", "grape"}
fruits.add("pear")
print(fruits)    # {'pear', 'banana', 'grape', 'apple'}
```

Adding a value that is already in the set raises no error and leaves the set unchanged. Starting with `set()` and adding in a loop is the common way to build one:

```python
fruits = set()
fruits.add("pear")
print(fruits)    # {'pear'}
```

`.add()` changes the set in place and returns `None`, like `.append()`.

### Removing with `.remove()`

`.remove()` takes a value out of the set:

```python
fruits = {"apple", "banana", "grape"}
fruits.remove("apple")
print(fruits)    # {'banana', 'grape'}
```

Removing a value that is not in the set is a `KeyError`, the same error a dictionary gives for a missing key. A set uses a hash table underneath, just like a dictionary's keys.

### Checking with `in`

`in` and `not in` work on a set the same way as on a list, but they are much faster. A set goes straight to the value's slot by its hash, so the check is O(1) on average, while a list scans every item. That speed is the main reason to use a set when the only question is "have I seen this before?"

```python
fruits = {"banana", "grape", "pear"}
"pear" in fruits     # True
"apple" in fruits    # False
```

### Looping over a set

A `for` loop works on a set like on a list:

```python
fruits = {"apple", "banana", "grape"}
for fruit in fruits:
    print(fruit)

# banana
# apple
# grape
```

The order of the loop is the set's internal order, so it is not guaranteed and can differ between runs. There is also no index: `fruits[0]` is a `TypeError`, since there is no first item.

### Converting between lists and sets

`set()` turns a list into a set, dropping the duplicates, and `list()` turns a set back into a list:

```python
fruits = ["apple", "banana", "apple"]
unique_fruits = set(fruits)       # {'banana', 'apple'}
fruits = list(unique_fruits)      # ['banana', 'apple']
```

`set()` takes anything that can be looped over, so `set("banana")` is `{'n', 'b', 'a'}`, the unique letters. The list that comes back from a set is in the set's order, not the original order.

### Removing duplicates from a list

The lesson gives two ways to do it. The first loops over the list with a set of values already seen and a list of results:

```python
def remove_duplicates(spells):
    seen = set()
    unique = []
    for spell in spells:
        if spell not in seen:
            seen.add(spell)
            unique.append(spell)
    return unique

remove_duplicates(["fireball", "heal", "fireball", "shield", "heal"])
# ['fireball', 'heal', 'shield']
```

The set answers "seen it?" quickly, and the list keeps the order each spell first appeared in. Using the list for the check, `if spell not in unique`, gives the same result but scans the list on every step, which makes the function O(n squared) instead of O(n).

The second converts to a set and back:

```python
def remove_duplicates(spells):
    return list(set(spells))
```

It is one line, but the order of the result is not guaranteed. When the order does not matter, it is the plain choice. When it does, use the loop.

### Counting with a set

Sets combine well with a counter. Here the counter adds up every vowel, and the set keeps each different vowel once:

```python
def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    count = 0
    unique_vowels = set()
    for char in text:
        if char in vowels:
            count += 1
            unique_vowels.add(char)
    return count, unique_vowels

count_vowels("Animal Attack")    # (5, {'A', 'a', 'i'}), set order may differ
count_vowels("rhythm")           # (0, set())
```

Two sets do two different jobs here. `vowels` is a fixed lookup table that is never changed, used only for the fast `in` check. `unique_vowels` starts empty and grows. `"A"` and `"a"` are different strings, so both are in the set. The function returns a tuple, as in Chapter 9, so the caller can unpack it with `count, found = count_vowels(text)`.

### Set subtraction

Sets support some of the operations from math. `a - b` is a new set of the values in `a` that are not in `b`:

```python
set1 = {"apple", "banana", "grape"}
set2 = {"apple", "banana"}
set3 = set1 - set2
print(set3)    # {'grape'}
```

Order matters. `{1, 2} - {2, 3}` is `{1}`, while `{2, 3} - {1, 2}` is `{3}`. Values in `b` that are not in `a` are ignored, and neither set is changed.

Subtraction only works between two sets. To compare lists, convert them first:

```python
def find_missing_ids(first_ids, second_ids):
    return set(first_ids) - set(second_ids)

find_missing_ids([1, 2, 3, 4, 4], [2, 4])    # {1, 3}
find_missing_ids([1, 2], [1, 2, 3])          # set()
```

The result is a set, so duplicates are gone automatically. Lists have no `-` at all: `[1, 2] - [1]` is a `TypeError`.

### Union, intersection, and symmetric difference

This one goes beyond the lessons. Subtraction has three companions:

```python
a = {1, 2, 3}
b = {3, 4}
a | b    # {1, 2, 3, 4}, in either (union)
a & b    # {3}, in both (intersection)
a ^ b    # {1, 2, 4}, in exactly one (symmetric difference)
a - b    # {1, 2}, in a but not b (difference)
```

Each one returns a new set. There are also method versions, `a.union(b)`, `a.intersection(b)`, `a.symmetric_difference(b)`, and `a.difference(b)`, which accept a list as the argument without converting it first. `a <= b` checks whether every value of `a` is in `b` (a subset). Two sets are equal when they hold the same values, so `{1, 2} == {2, 1}` is `True`.

## Analogy

Continuing the kitchen from Chapters 1 to 10: **a set is the pantry checklist taped inside the cupboard door.**

- The list shelf from Chapter 9 can hold three jars of salt in a row. The checklist has one line for salt, no matter how many times someone writes it down.
- The checklist has no numbered lines. Asking for "item 0" makes no sense, and reading it top to bottom gives whatever order the lines happen to be in.
- `checklist.add("salt")` writes salt down if it is not there yet. If it is, nothing changes.
- `checklist.remove("salt")` crosses salt off. Crossing off something that was never on the list is a `KeyError`.
- `"salt" in checklist` is glancing at the checklist instead of opening every jar on the shelf. That is why a set is the tool for "do we have this?"
- `set(shelf)` reads the shelf and writes each ingredient on the checklist once, which is how duplicates disappear.
- Subtraction is the shopping list: `recipe - pantry` is everything the recipe needs that the pantry does not have.
- An empty checklist needs `set()`, because `{}` is already the empty spice rack from Chapter 10.

## Example

```python
# Creating, duplicates dropped
fruits = {"apple", "banana", "grape"}
print(type(fruits))                     # <class 'set'>
print(len({"apple", "apple", "banana"}))    # 2

# Empty set versus empty dictionary
print(type({}))                         # <class 'dict'>
print(type(set()))                      # <class 'set'>
print(set())                            # set()

# Adding and removing
fruits.add("pear")
fruits.add("pear")                      # already there, no change
print(len(fruits))                      # 4
fruits.remove("apple")
print(sorted(fruits))                   # ['banana', 'grape', 'pear']

# Checking
print("pear" in fruits)                 # True
print("apple" in fruits)                # False

# Looping, order not guaranteed
for fruit in fruits:
    print(fruit)
# banana
# grape
# pear

# Converting
print(sorted(set(["apple", "banana", "apple"])))    # ['apple', 'banana']
print(sorted(set("banana")))            # ['a', 'b', 'n']

# Removing duplicates, keeping order
def remove_duplicates(spells):
    seen = set()
    unique = []
    for spell in spells:
        if spell not in seen:
            seen.add(spell)
            unique.append(spell)
    return unique

print(remove_duplicates(["fireball", "heal", "fireball", "shield", "heal"]))
# ['fireball', 'heal', 'shield']

# Removing duplicates, order not kept
def remove_duplicates_set(spells):
    return list(set(spells))

print(sorted(remove_duplicates_set(["fireball", "heal", "fireball", "shield", "heal"])))
# ['fireball', 'heal', 'shield']

# Counting vowels
def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    count = 0
    unique_vowels = set()
    for char in text:
        if char in vowels:
            count += 1
            unique_vowels.add(char)
    return count, unique_vowels

count, found = count_vowels("Hello World")
print(count, sorted(found))             # 3 ['e', 'o']
count, found = count_vowels("Animal Attack")
print(count, sorted(found))             # 5 ['A', 'a', 'i']
print(count_vowels("rhythm"))           # (0, set())

# Subtraction
print({"apple", "banana", "grape"} - {"apple", "banana"})    # {'grape'}
print({1, 2} - {2, 3})                  # {1}
print({2, 3} - {1, 2})                  # {3}

def find_missing_ids(first_ids, second_ids):
    return set(first_ids) - set(second_ids)

print(find_missing_ids([1, 2, 3, 4, 4], [2, 4]))    # {1, 3}
print(find_missing_ids([1, 2], [1, 2, 3]))          # set()

# The other operations
a = {1, 2, 3}
b = {3, 4}
print(a | b)                            # {1, 2, 3, 4}
print(a & b)                            # {3}
print(a ^ b)                            # {1, 2, 4}
print({1, 2} == {2, 1})                 # True
print({1} <= {1, 2})                    # True
```

`sorted()` is used on string sets above so the printed output is the same every run. It returns a list, not a set.

Common errors:

```python
fruits = {"apple", "banana"}
fruits.remove("pear")                   # KeyError: 'pear'
fruits[0]                               # TypeError: 'set' object is not subscriptable
fruits.append("pear")                   # AttributeError: 'set' object has no attribute 'append'
fruits.add("pear", "kiwi")              # TypeError: set.add() takes exactly one argument (2 given)

empty = {}
empty.add("pear")                       # AttributeError: 'dict' object has no attribute 'add'

{1} + {2}                               # TypeError: unsupported operand type(s) for +: 'set' and 'set'
[1, 2] - [1]                            # TypeError: unsupported operand type(s) for -: 'list' and 'list'
{1, 2} - [1]                            # TypeError: unsupported operand type(s) for -: 'set' and 'list'
set(1, 2)                               # TypeError: set expected at most 1 argument, got 2

{[1, 2]}                                # TypeError: cannot use 'list' as a set element (unhashable type: 'list')

nums = {1, 2}
for n in nums:
    nums.add(n + 10)                    # RuntimeError: Set changed size during iteration
```

Python versions before 3.14 word the list error as `TypeError: unhashable type: 'list'`.

## In other languages

| | Python | JavaScript | Go | Bash |
|---|---|---|---|---|
| Built in | Yes, `set` | Yes, `Set` | No, use a map | No, use an associative array |
| Create | `s = {"a", "b"}` | `const s = new Set(["a", "b"]);` | `s := map[string]bool{"a": true, "b": true}` | `declare -A s=([a]=1 [b]=1)` |
| Empty | `s = set()` | `const s = new Set();` | `s := map[string]bool{}` | `declare -A s` |
| Add | `s.add("c")` | `s.add("c")` | `s["c"] = true` | `s[c]=1` |
| Remove | `s.remove("c")` | `s.delete("c")` | `delete(s, "c")` | `unset 's[c]'` |
| Remove missing value | `KeyError` | No error, returns `false` | No error | No error |
| Contains | `"a" in s` | `s.has("a")` | `s["a"]`, or `_, ok := s["a"]` | `[[ -v s[a] ]]` |
| Size | `len(s)` | `s.size` | `len(s)` | `${#s[@]}` |
| Loop | `for x in s:` | `for (const x of s) { }` | `for x := range s { }` | `for x in "${!s[@]}"; do ... done` |
| Loop order | Not guaranteed | Insertion order | Random on purpose | Not guaranteed |
| From a list | `set(lst)` | `new Set(arr)` | Loop and add | Loop and add |
| Back to a list | `list(s)` | `[...s]` | Loop and append | `"${!s[@]}"` |
| Difference | `a - b` | `a.difference(b)` (ES2025) | Loop and check | Loop and check |

In C, there is no built-in set either. For small whole numbers, a boolean array works: `seen[42] = true` marks 42 as present, and checking is one index lookup. For a handful of flags, the bits of a single integer do the same job, and `a & ~b` is set subtraction in one instruction. For strings or large values, C needs a hash table again, like the one under a Python dictionary but storing only keys. That is what a Python set is: a dictionary's key table with no values attached.

Three ideas carry over to every language:

1. **A set is a map with no values.** Go and Bash have no set type, and the usual workaround is a map whose values are ignored. Python's set is built the same way underneath, which is why its errors and rules (hashable values, `KeyError`) match a dictionary's keys.
2. **Use a set for membership.** Checking whether something is in a set is fast in every language, while checking a list or array means scanning it. Any loop that asks "have I seen this?" on a list is a candidate for a set.
3. **Do not depend on set order.** Python and Bash do not guarantee it and Go randomizes it. JavaScript is the exception and keeps insertion order. When order matters, sort the result or keep a separate list.

## Interview framing

1. What is a set, and how is it different from a list?
2. How would you remove duplicates from a list? Does your answer keep the order?
3. Why is checking `in` on a set faster than on a list?
4. How do you create an empty set, and why not `{}`?
5. What can go in a set?
6. How would you find the items in one list that are not in another?
7. What is the difference between `.remove()` and `.discard()`?

## My answer

**1. Set versus list**

"A set is an unordered collection of unique values. A list keeps order, allows duplicates, and can be indexed, while a set has no order, no index, and holds each value once. Underneath, a set is a hash table like a dictionary's keys, so adding, removing, and checking a value with `in` are O(1) on average, where `in` on a list is O(n). I use a list when order or duplicates matter, like a playlist. I use a set when I only care whether something is present, like the ids of users who already voted, or when I need to compare two groups with operations like difference and intersection."

**2. Removing duplicates**

"The short way is `list(set(items))`, but it loses the original order, because a set has none. To keep the order, I loop once with an empty `seen` set and an empty result list. For each item, if it is not in `seen`, I add it to both. That is O(n), because each `in` check on the set is O(1). If I did the check against the result list instead, it would still work but become O(n squared). Another order-keeping one-liner is `list(dict.fromkeys(items))`, since dictionaries keep insertion order and their keys are unique. All of these need the items to be hashable."

**3. Why `in` is fast on a set**

"When a value goes into a set, Python hashes it and stores it in the slot that hash points to. To check `x in s`, it hashes `x`, goes straight to that slot, and compares with `==`. It does not look at the other values, so the time does not grow with the size of the set, which is O(1) on average. A list has no such index, so `x in lst` compares against each item until it finds a match or reaches the end, which is O(n). The tradeoff is memory, since a hash table keeps empty slots, and the rule that values must be hashable."

**4. Empty set**

"`set()`. Curly braces were already used for dictionaries before sets got literal syntax, so `{}` is an empty dictionary. That is also why an empty set prints as `set()`. The mistake shows up when someone writes `seen = {}` and then calls `seen.add(x)`, which fails with `AttributeError: 'dict' object has no attribute 'add'`."

**5. What can go in a set**

"Only hashable values, the same rule as dictionary keys: strings, numbers, booleans, `None`, and tuples of hashable values. Lists, dictionaries, and other sets cannot go in, because they can change, and a changed value would no longer be in the slot its hash pointed to. Trying gives a `TypeError`. When I need a set of pairs, I use tuples, like a set of `(x, y)` coordinates. When I need a set inside a set, there is `frozenset`, which is an immutable set and is hashable. Values that are equal and hash the same count as one, so `{1, 1.0, True}` is just `{1}`."

**6. Items in one list but not another**

"I convert both lists to sets and subtract: `set(a) - set(b)`. That gives the values in `a` that are not in `b`, with no duplicates, in O(len(a) + len(b)) time. Subtraction is not symmetric, so `set(b) - set(a)` is a different answer, and if I want the values in exactly one of the two, that is `set(a) ^ set(b)`. If the result has to keep the order of `a`, or keep duplicates, I make a set from `b` only and loop over `a`, keeping each item that is not in that set. Checking `x not in b` on the list itself would make that O(n times m)."

**7. `.remove()` versus `.discard()`**

"Both take a value out of a set. The difference is when the value is not there: `.remove()` raises a `KeyError`, and `.discard()` does nothing. It is the same choice as `d[key]` versus `d.get(key)` on a dictionary. I use `.remove()` when the value must be there and a missing one would be a bug, and `.discard()` when it may or may not be there and either is fine. The lessons only cover `.remove()`, but `.discard()` saves writing an `in` check first."

**Points to recall**

- Sets use curly braces with plain values: `{"a", "b"}`. They are unordered and every value is unique.
- `{}` is an empty dictionary. An empty set is `set()`, and it prints as `set()`.
- Duplicates are dropped silently, both in the literal and with `.add()`.
- `.add(x)` adds one value and returns `None`. Adding a value already there changes nothing.
- `.remove(x)` removes a value. A missing value is a `KeyError`.
- `x in s` and `x not in s` are O(1) on average, compared with O(n) on a list.
- `for x in s` works, but the order is not guaranteed. There is no indexing.
- `set(lst)` drops duplicates. `list(s)` converts back, in no particular order.
- Removing duplicates while keeping order: loop with a `seen` set and a result list.
- `a - b` is the values in `a` not in `b`. Both sides must be sets, and order matters.
- `|` union, `&` intersection, `^` symmetric difference. Each returns a new set.
- Set values must be hashable, so lists cannot go in a set.
- Use `sorted(s)` when a set needs to be printed or compared in a fixed order.
- Do not add or remove values while looping over the same set.

## Follow-up gotchas

**Why does the set print in a different order than I wrote it?**
A set stores each value in the slot chosen by its hash, not in the order it arrived. Printing and looping walk those slots in order. String hashes are also randomized every time Python starts, as a security measure, so a set of strings can print in a different order on every run. Small integers hash to themselves, which is why `{3, 1, 2}` often prints as `{1, 2, 3}`, but that is a side effect and not a promise. Unlike dictionaries, which have kept insertion order since 3.7, sets never made that guarantee.

**Why does `{}` not make an empty set?**
Dictionaries came first and already owned `{}`. When set literals were added in Python 2.7 and 3.0, `{}` stayed a dictionary so old code would not break. `{1}` is a set because it has a value without a colon. Only the empty case is ambiguous, so it belongs to the dictionary.

**Why did `list(set(items))` scramble my list?**
The set has no order, so the list built from it comes out in the set's internal order. Nothing is lost, but the original order is gone. When the order matters, use the loop with a `seen` set, or `list(dict.fromkeys(items))`, which keeps the first appearance of each item.

**Why is `.remove()` a `KeyError` and not a `ValueError` like on a list?**
A list's `.remove()` searches for a value, and not finding it is a `ValueError`. A set is a hash table of keys with no values, so a missing value is a missing key, and Python uses the same `KeyError` a dictionary would. `s.discard(x)` removes a value without raising when it is missing. To avoid the error with `.remove()`, check with `in` first.

**Why can't a list go in a set?**
The set puts each value in the slot chosen by its hash. If a list could go in and was changed afterward, its hash would change, and the set would look for it in the wrong slot. Python prevents that by allowing only hashable values, which raises `TypeError: cannot use 'list' as a set element`. Convert the list to a tuple first, `s.add(tuple(lst))`, if a fixed version of it is what is needed.

**Why does `{1, 1.0, True}` have only one value?**
`1 == 1.0 == True`, and all three have the same hash, so the set treats them as one value and keeps the first one written. It is the same rule that gives a dictionary one key for them. The set `{0, False}` has one value for the same reason.

**Why does subtraction give a different answer when the sides are swapped?**
`a - b` keeps what is in `a` and removes anything also in `b`. Values that are only in `b` play no part. So `{1, 2} - {2, 3}` is `{1}` and `{2, 3} - {1, 2}` is `{3}`. The direction should read as "what `a` has that `b` does not." When the question is "what is different between the two," the answer is `a ^ b`.

**Why does changing a set inside a loop over it crash?**
Like a dictionary, a set can rearrange its table when it grows or shrinks, so the loop would skip or repeat values. Python stops with `RuntimeError: Set changed size during iteration` instead. Loop over a copy, `for x in list(s):`, or collect the changes in a second set and apply them after the loop.
