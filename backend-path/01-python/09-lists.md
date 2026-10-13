# 09: Lists

Source: boot.dev Learn Python, Chapter 9, Lessons 1 to 12.

## What it is

### Lists

A list stores many values in order under one name. A feed is a list of posts, a store is a list of products, and an inventory is a list of items. Other languages call this an array.

A list is written with square brackets, with commas between the items:

```python
inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]
```

A list can hold values of any type, and the types can be mixed: `["sword", 3, 2.5, True, None]` is a valid list. In practice, most lists hold one kind of thing, since the code that reads them usually treats every item the same way.

A long list can be split across lines. This is only a style choice, and the list is the same either way:

```python
flower_types = [
    "daffodil",
    "rose",
    "chrysanthemum",
]
```

The comma after the last item is allowed. It is a common habit for multi-line lists, because adding a new item later only changes one line.

### Indexes start at 0

Each item has an index, which is its position in the list. The first item is index `0`, not `1`:

```python
names = ["Bob", "Lane", "Alice", "Breanna"]
# index:   0       1        2         3
```

An item is read with the list name followed by the index in square brackets:

```python
best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]
print(best_languages[1])    # Go
```

The index must be an integer. A string or a float, even `1.0`, is a `TypeError`. An index past the end of the list is an `IndexError: list index out of range`.

### Length

`len()` returns the number of items in a list. It works on any iterable, including strings, where it counts the characters:

```python
fruits = ["apple", "banana", "pear"]
len(fruits)                                   # 3
len("supercalifragilisticexpialidocious")     # 34
```

Because indexes start at 0, the last index is always one less than the length. A list of 3 items has indexes 0, 1, and 2. The index of the last item is `len(items) - 1`, and `items[len(items)]` is always an `IndexError`.

### Updating an item

Assigning to an index replaces the item at that position:

```python
inventory = ["Leather", "Iron Ore", "Healing Potion"]
inventory[0] = "Leather Armor"
# ['Leather Armor', 'Iron Ore', 'Healing Potion']
```

This only replaces an existing item. Assigning to an index that does not exist yet is an `IndexError: list assignment index out of range`, so it cannot be used to grow the list.

Reading and updating combine naturally with an `if`:

```python
def smelt_ore(inventory):
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"
    return inventory
```

The function changes the list it was given. The caller's list is the same object, so the caller sees the change too (see Follow-up gotchas).

### Adding with `.append()`

`.append()` adds one value to the end of a list. A common pattern is to start with an empty list and fill it in a loop. It is the accumulator pattern from Chapter 8, with a list as the bowl instead of a number:

```python
def generate_user_list(num_of_users):
    player_ids = []
    for i in range(0, num_of_users):
        player_ids.append(i)
    return player_ids

generate_user_list(4)    # [0, 1, 2, 3]
```

`.append()` is a method: a function that belongs to a value and is called with a dot. It changes the list in place and returns `None`, so `items = items.append(x)` replaces the list with `None`. It takes exactly one argument.

### Removing with `.pop()`

`.pop()` is the opposite of `.append()`. It removes the last item and returns it:

```python
vegetables = ["broccoli", "cabbage", "kale", "tomato"]
last_vegetable = vegetables.pop()
# vegetables: ['broccoli', 'cabbage', 'kale']
# last_vegetable: 'tomato'
```

With an index, `.pop(i)` removes and returns the item at that position instead. `vegetables.pop(1)` removes `"cabbage"`, and every item after it moves down one index.

Popping in a loop takes items off the end one at a time, so they come out in reverse order. Popping from an empty list is an `IndexError: pop from empty list`.

### Looping with an index

To visit every item, loop over the indexes from `0` to `len(items) - 1`. `range(0, len(items))` gives exactly those numbers, because the stop is excluded:

```python
def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0
    for i in range(0, len(items)):
        if items[i] == "Potion":
            potion_count += 1
        elif items[i] == "Bread":
            bread_count += 1
        elif items[i] == "Shortsword":
            shortsword_count += 1
    return potion_count, bread_count, shortsword_count
```

The index form is needed when the index itself matters:

- **To update an item.** `items[i] = ...` needs `i`.
- **To read two lists at the same position.** When two lists are the same length, one index reads from both. This prints the index of every character whose level went up:

```python
def check_character_levels(old_character_levels, new_character_levels):
    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] < new_character_levels[i]:
            print(i)

check_character_levels([2, 5, 3, 7, 5], [2, 5, 19, 7, 8])    # 2, 4
```

### Looping without an index

When only the values matter, Python loops over the list directly:

```python
trees = ["oak", "pine", "maple"]
for tree in trees:
    print(tree)    # oak, pine, maple
```

`tree` holds the value itself, not its index. There is no `range`, no `len`, and no `trees[i]`, so there is no chance of an off by one error. This is the preferred form whenever the loop only reads the items.

Searching a list is a common use:

```python
def contains_leather_scraps(items):
    found = False
    for item in items:
        if item == "Leather Scraps":
            found = True
    return found
```

The flag starts as `False` before the loop and only becomes `True` on a match, so an empty list or a list with no match returns `False`. Adding `break` after `found = True` stops the search at the first match, as in Chapter 8.

The rule for choosing:

- Read only: `for item in items`.
- Update items, or use the position: `for i in range(0, len(items))`.

## Analogy

Continuing the kitchen from Chapters 1 to 8: **a list is a numbered row of jars on a shelf.**

- The shelf holds the jars in a fixed order, and each spot has a number painted under it. The first spot is painted `0`, which is the part that trips up every new cook.
- `shelf[2]` is "hand me the jar in spot 2." Asking for a spot past the end of the shelf gets nothing but an error.
- `len(shelf)` is counting the jars. Six jars means the last spot is painted `5`.
- `shelf[1] = "Iron Bar"` is swapping out the jar in spot 1. It only works on a spot that already exists. The shelf does not grow by pointing at empty wall.
- `.append()` is putting a new jar at the end of the row, and `.pop()` is taking the last jar off and handing it over. Taking jars off the end one by one gives them back in reverse order.
- `for jar in shelf` is walking along the shelf reading each label. `for i in range(len(shelf))` is walking along reading the painted numbers, which is needed when a jar has to be swapped or compared with the jar in the same spot on another shelf.

## Example

```python
# Creating and indexing
inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]
print(inventory[0])                     # Iron Breastplate
print(inventory[2])                     # Leather Scraps
print(len(inventory))                   # 3
print(len(inventory) - 1)               # 2, the last index
print(len("supercalifragilisticexpialidocious"))   # 34

mixed = ["sword", 3, 2.5, True, None]   # any types, mixed

player_ages = [
    23,
    18,
    31,
]                                       # same list as [23, 18, 31]

# Updating
inventory = ["Leather", "Iron Ore", "Healing Potion"]
inventory[0] = "Leather Armor"
print(inventory)                        # ['Leather Armor', 'Iron Ore', 'Healing Potion']

def smelt_ore(inventory):
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"
    return inventory

print(smelt_ore(["Sword", "Iron Ore"])) # ['Sword', 'Iron Bar']

# Appending
cards = []
cards.append("nvidia")
cards.append("amd")
print(cards)                            # ['nvidia', 'amd']

def generate_user_list(num_of_users):
    player_ids = []
    for i in range(0, num_of_users):
        player_ids.append(i)
    return player_ids

print(generate_user_list(4))            # [0, 1, 2, 3]

# Popping
vegetables = ["broccoli", "cabbage", "kale", "tomato"]
print(vegetables.pop())                 # tomato
print(vegetables)                       # ['broccoli', 'cabbage', 'kale']
print(vegetables.pop(1))                # cabbage
print(vegetables)                       # ['broccoli', 'kale']

items = ["Shortsword", "Potion", "Bread"]
while len(items) > 0:
    print(items.pop())                  # Bread, Potion, Shortsword
print(items)                            # []

# Looping with an index
def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0
    for i in range(0, len(items)):
        if items[i] == "Potion":
            potion_count += 1
        elif items[i] == "Bread":
            bread_count += 1
        elif items[i] == "Shortsword":
            shortsword_count += 1
    return potion_count, bread_count, shortsword_count

print(get_item_counts(["Potion", "Bread", "Potion", "Shortsword", "Potion"]))   # (3, 1, 1)

def check_character_levels(old_character_levels, new_character_levels):
    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] < new_character_levels[i]:
            print(i)

check_character_levels([2, 5, 3, 7, 5], [2, 5, 19, 7, 8])   # 2, 4

# Looping without an index
for tree in ["oak", "pine", "maple"]:
    print(tree)                         # oak, pine, maple

def contains_leather_scraps(items):
    found = False
    for item in items:
        if item == "Leather Scraps":
            found = True
    return found

print(contains_leather_scraps(["Potion", "Leather Scraps"]))   # True
print(contains_leather_scraps([]))      # False

# Changing the loop variable does not change the list
nums = [1, 2, 3]
for n in nums:
    n *= 10
print(nums)                             # [1, 2, 3]

for i in range(len(nums)):
    nums[i] *= 10
print(nums)                             # [10, 20, 30]

# Both the index and the value
for i, name in enumerate(["Bob", "Lane"]):
    print(i, name)                      # 0 Bob, 1 Lane

# Two names, one list
a = [1, 2]
b = a
b.append(3)
print(a)                                # [1, 2, 3]
```

Common errors:

```python
names = ["Bob", "Lane", "Alice"]
names[3]                                # IndexError: list index out of range
names[3] = "Breanna"                    # IndexError: list assignment index out of range
names["0"]                              # TypeError: list indices must be integers or slices, not str
names[1.0]                              # TypeError: list indices must be integers or slices, not float

[].pop()                                # IndexError: pop from empty list
names.pop(5)                            # IndexError: pop index out of range
names.append("Breanna", "Carl")         # TypeError: list.append() takes exactly one argument (2 given)

names = names.append("Breanna")
print(names)                            # None, append returns None
```

## In other languages

| | Python | JavaScript | Go | Bash |
|---|---|---|---|---|
| Name | List | Array | Slice, built on a fixed-size array | Indexed array |
| Create | `x = [1, 2, 3]` | `const x = [1, 2, 3];` | `x := []int{1, 2, 3}` | `x=(1 2 3)` |
| Empty | `x = []` | `const x = [];` | `var x []int` | `x=()` |
| Read | `x[0]` | `x[0]` | `x[0]` | `${x[0]}` |
| Update | `x[0] = 9` | `x[0] = 9` | `x[0] = 9` | `x[0]=9` |
| Length | `len(x)` | `x.length` | `len(x)` | `${#x[@]}` |
| Add to end | `x.append(4)` | `x.push(4)` | `x = append(x, 4)` | `x+=(4)` |
| Remove last | `x.pop()` | `x.pop()` | `x = x[:len(x)-1]` | `unset 'x[-1]'` |
| Out of range read | `IndexError` | `undefined`, no error | Panic: index out of range | Empty string, no error |
| Loop over values | `for v in x:` | `for (const v of x) { }` | `for _, v := range x { }` | `for v in "${x[@]}"; do ... done` |
| Loop over indexes | `for i in range(len(x)):` | `for (let i = 0; i < x.length; i++) { }` | `for i := range x { }` | `for i in "${!x[@]}"; do ... done` |
| Mixed types | Yes | Yes | No, one element type | Everything is a string |

In C, an array has a fixed size set when it is declared, `int x[3] = {1, 2, 3};`, and every element has the same type. There is no `len()`: `sizeof(x) / sizeof(x[0])` works only where the array was declared, and once it is passed to a function it decays to a pointer and the length must be passed separately. Reading past the end is not an error at all. It is undefined behavior that reads whatever memory sits there. A Python list is closer to a growable array of pointers: it tracks its own length, resizes itself on `append`, and checks every index.

Two ideas carry over to every language:

1. **Indexes start at 0, so the last index is the length minus 1.** Almost every off by one bug with arrays comes from forgetting this, either by stopping one short or by reading one past the end.
2. **Know what happens on a bad index.** Python and Go stop with an error, which is easy to debug. JavaScript and Bash quietly return nothing, and C reads garbage memory, so the bug shows up somewhere else later.

## Interview framing

1. What is a list in Python, and how is it different from an array in C?
2. What is the time cost of indexing, `append`, and `pop`?
3. When would you loop with `range(len(items))` and when with `for item in items`?
4. What does `append` return, and why does that matter?
5. If a function changes a list it was passed, does the caller see the change?

## My answer

**1. List versus a C array**

"A Python list is an ordered, mutable collection that can grow and shrink. Under the hood it is a dynamic array: a block of memory holding references to the items, plus a length. Compared with a C array, it does not have a fixed size, it can hold items of different types because it stores references, it tracks its own length so `len` is instant, and it checks every index, raising an `IndexError` instead of reading past the end."

**2. Time cost**

"Indexing and updating by index are O(1), because the list can jump straight to a position in memory. `append` is amortized O(1). The list keeps some spare capacity, and when it runs out it allocates a bigger block and copies everything over, but that happens rarely enough that the average stays constant. `pop()` from the end is O(1). `pop(0)` or `pop(i)` near the front is O(n), because every item after it has to shift down one spot. If I need to remove from the front often, I use `collections.deque`."

**3. Index loop versus value loop**

"I use `for item in items` by default, because it is shorter and cannot go out of range. I switch to an index when I need the position: to update `items[i]`, to read the same position in a second list, or to compare an item with its neighbor. When I need both the index and the value, I use `enumerate`, and for walking two lists side by side, `zip`."

**4. `append` returns `None`**

"`append` changes the list in place and returns `None`. That is a Python convention for methods that mutate: they return `None` so it is clear they did not make a new object. The common bug is writing `items = items.append(x)`, which throws the list away and leaves `items` as `None`. The fix is to call `items.append(x)` on its own line."

**5. Mutating a passed list**

"Yes. Passing a list to a function passes a reference to the same list object, not a copy. If the function calls `append`, `pop`, or assigns to an index, the caller's list changes. If the function assigns a whole new list to its parameter, that only rebinds the local name, and the caller is unaffected. When a function should not change its input, I copy it first with `items.copy()` or `list(items)`, or build and return a new list."

**Points to recall**

- Lists use square brackets and commas, and can hold any types.
- Multi-line lists are only a style choice. A trailing comma is allowed.
- Indexes start at `0`. The last index is `len(items) - 1`.
- Indexes must be integers. A bad index is an `IndexError`.
- `items[i] = value` replaces an existing item. It cannot add a new one.
- `.append(x)` adds one item to the end and returns `None`.
- `.pop()` removes and returns the last item. `.pop(i)` removes the item at index `i`.
- Popping from an empty list is an `IndexError`.
- `range(0, len(items))` gives every valid index.
- `for item in items` for reading. Use an index to update or to read two lists together.
- Changing the loop variable in `for item in items` does not change the list.

## Follow-up gotchas

**Why does `for n in nums: n *= 10` leave the list unchanged?**
`n` is a separate name that points at each item in turn. `n *= 10` makes `n` point at a new number, and the list still holds the old ones. Integers and strings cannot be changed in place, so the only way to change the list is to assign through it: `nums[i] = nums[i] * 10`, with an index loop. The same thing happens in JavaScript with `for (let n of nums)` and in Go with `for _, n := range nums`, where `n` is a copy.

**Why did changing `b` change `a`?**
`b = a` does not copy the list. It gives the same list a second name, so `b.append(3)` and `a.append(3)` do exactly the same thing. To get an independent list, copy it: `b = a.copy()` or `b = list(a)`. The copy is shallow, so a list inside the list is still shared. `copy.deepcopy(a)` copies all the way down.

**Is it safe to remove items from a list while looping over it?**
No. `for item in items` walks the list by position, so removing an item shifts the rest down one spot and the next item gets skipped. Either loop over a copy, `for item in items.copy()`, build a new list of the items to keep, or loop backward with an index so the shifts only affect items already visited.

**What is a cleaner way to write the "found" search?**
`return "Leather Scraps" in items`. The `in` operator checks every item and stops at the first match. The manual loop is still worth knowing, because it is the same pattern used when the check is more than a simple equality, such as finding the first item over a price limit.

**Why does `range(0, len(items))` never go out of range?**
`range` excludes its stop, so the last value is `len(items) - 1`, which is exactly the last valid index. For an empty list, it is `range(0, 0)`, the body never runs, and nothing is indexed. Writing `range(0, len(items) + 1)` or `range(1, len(items) + 1)` with `items[i]` is the classic off by one, and it fails with an `IndexError` on the last iteration.
