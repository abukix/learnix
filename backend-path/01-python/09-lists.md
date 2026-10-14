# 09: Lists

Source: boot.dev Learn Python, Chapter 9, Lessons 1 to 24.

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

### Negative indexes

A negative index counts from the end of the list. `-1` is the last item, `-2` is the second to last, and so on:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[-1]    # 9
numbers[-2]    # 8
```

`items[-1]` is the short way to write `items[len(items) - 1]`. A negative index that reaches past the start, such as `[1][-2]`, is still an `IndexError`.

### Slicing

A slice takes a section of a list and returns it as a new list. The syntax has three parts separated by colons:

```python
my_list[start:stop:step]
```

- `start` is the first index included.
- `stop` is the first index **not** included, the same rule as `range`.
- `step` is how far to move each time. `2` takes every other item.

```python
scores = [50, 70, 30, 20, 90, 10, 50]
scores[1:5:2]    # [70, 20], indexes 1 and 3
```

Every part is optional. A missing `start` means the beginning, a missing `stop` means the end, and a missing `step` means `1`:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[:3]      # [0, 1, 2], everything before index 3
numbers[3:]      # [3, 4, 5, 6, 7, 8, 9], index 3 to the end
numbers[::2]     # [0, 2, 4, 6, 8], even indexes
numbers[1::2]    # [1, 3, 5, 7, 9], odd indexes
numbers[-3:]     # [7, 8, 9], the last three
numbers[:-1]     # [0, 1, 2, 3, 4, 5, 6, 7, 8], all but the last
numbers[::-1]    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], reversed
numbers[:]       # a full copy
```

`[:3]` and `[3:]` split a list cleanly into two parts with no overlap, because the stop of one is the start of the other.

Slicing never raises an `IndexError`. A stop past the end is cut down to the end, and a range with nothing in it gives an empty list: `numbers[5:100]` is `[5, 6, 7, 8, 9]` and `numbers[8:3]` is `[]`.

Because a slice is a new list, changing the slice does not change the original. `numbers[:]` is a common way to copy a list.

### Concatenating with `+`

`+` joins two lists into a new list, the same way it joins two strings:

```python
total = [1, 2, 3] + [4, 5, 6]
# [1, 2, 3, 4, 5, 6]
```

Both lists are left unchanged, and the order of the result follows the order of the operands. Both sides must be lists: `[1, 2] + 3` is a `TypeError: can only concatenate list (not "int") to list`, so a single value has to be wrapped first, `[1, 2] + [3]`.

### Checking membership with `in`

`in` checks whether a value is in a list and returns a boolean. `not in` checks that it is absent:

```python
fruits = ["apple", "orange", "banana"]
"banana" in fruits        # True
"banana" not in fruits    # False
```

It replaces the "found" flag loop from earlier in a single expression, and reads well inside an `if`:

```python
def is_top_weapon(weapon):
    top_weapons = ["sword of justice", "axe of fire", "hammer of thunder"]
    return weapon in top_weapons
```

`in` compares with `==`, so the match must be exact, including case. On a string, `in` checks for a substring instead: `"an" in "banana"` is `True`.

### Deleting with `del`

`del` removes an item by index, or a whole slice, from a list in place:

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[3]      # [1, 2, 3, 5, 6, 7, 8, 9]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]    # [1, 4, 5, 6, 7, 8, 9]

del nums[:]      # [], the list still exists but is empty
```

Combined with negative indexes, it trims either end of a list:

```python
def trim_strongholds(strongholds):
    del strongholds[0]      # the first
    del strongholds[-2:]    # the last two
    return strongholds
```

`del` is a statement, not a function, and it returns nothing. Compared with `.pop(i)`, it does not hand back the removed item, but it can remove a slice in one step. To remove by value instead of by index, use `.remove(x)`, which deletes the first match and raises a `ValueError` if there is none.

### Tuples

A tuple is an ordered collection like a list, but it cannot be changed after it is created. It is written with round brackets:

```python
my_tuple = ("this is a tuple", 45, True)
my_tuple[0]    # 'this is a tuple'
my_tuple[1]    # 45
```

Indexing, slicing, `len()`, `in`, and `for` loops all work the same as on a list. Changing anything does not: assigning to an index is a `TypeError`, and there is no `.append()` or `.pop()`.

Tuples are used for small, fixed groups of related values, usually two or three, where each position has its own meaning. Mixing types is normal here, because the position tells the reader what each value is:

```python
dog = ("Fido", 4)    # name, age
```

A single-item tuple needs a trailing comma. Without it, the brackets are just grouping, and `("Fido")` is the string `"Fido"`:

```python
dog = ("Fido",)    # a tuple with one item
```

It is the comma that makes a tuple, not the brackets. `t = 1, 2` is also a tuple.

A list of tuples is a common way to store records. The first index picks the tuple, and the second picks the value inside it:

```python
heroes = [
    ("Glorfindel", 2093, True),
    ("Gandalf", 1000, False),
]
heroes[0][0]    # 'Glorfindel'
heroes[1][2]    # False
```

**Unpacking** assigns each value in a tuple to its own name, by position:

```python
dog_name, dog_age = dog
```

This is the same unpacking used for multiple return values in Chapter 3. `return a, b` builds a tuple, and `x, y = f()` unpacks it. Unpacking also works in a `for` loop over a list of tuples, which reads much better than indexing:

```python
for name, age, is_elf in heroes:
    print(name, age, is_elf)
```

The number of names must match the number of values, or it is a `ValueError`.

### Splitting and joining strings

Two string methods convert between a sentence and a list of words.

`.split()` is called on a string and returns a list. With no argument, it splits on any run of whitespace and ignores whitespace at the ends. With an argument, it splits on exactly that text:

```python
"hello there sam".split()      # ['hello', 'there', 'sam']
"  lots   of   space ".split() # ['lots', 'of', 'space']
"a,b,,c".split(",")            # ['a', 'b', '', 'c']
```

`.join()` goes the other way. It is called on the separator, and takes the list of strings to put it between:

```python
" ".join(["hello", "there", "sam"])    # 'hello there sam'
"-".join(["x", "y"])                   # 'x-y'
```

The separator coming first looks backward at first, but it is because `join` is a string method. Every item in the list must already be a string, or it is a `TypeError`.

Together they turn text processing into list processing: split the string, work on the list of words, then join it back.

### Common list patterns

The last lessons of the chapter combine everything above into a few patterns that come up constantly.

**Guarding against an empty list.** Before reading `items[0]`, check the length, or the function crashes on an empty list:

```python
def get_first_item(items):
    if len(items) == 0:
        return "ERROR"
    return items[0]
```

**Finding the largest value.** Keep a running best, and replace it whenever an item beats it. The starting value matters. `0` gives the wrong answer for a list of negative numbers, so start at negative infinity, which every number is greater than:

```python
def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far

find_max([100, 10, 22])    # 100
find_max([-5, -2, -9])     # -2
find_max([])               # -inf
```

`float("-inf")` and `float("inf")` are real float values for negative and positive infinity. For finding a minimum, the same pattern starts at `float("inf")` and uses `<`. Python has the built-ins `max()` and `min()` for this, but writing the loop once shows how they work.

**Filtering with a condition.** Loop, test each item, and append the ones that pass to a new list. The modulo operator from Chapter 6 is a common test: a number is odd when `n % 2 != 0`, because dividing an odd number by 2 always leaves 1:

```python
def get_odd_numbers(num):
    odd_numbers = []
    for i in range(0, num):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers

get_odd_numbers(10)    # [1, 3, 5, 7, 9]
```

**Reversing with a loop.** `range` can count down with a negative step. To visit every index from last to first, start at `len(items) - 1` and stop at `-1`, since the stop is excluded and index `0` must be included:

```python
def reverse_list(items):
    reversed_items = []
    for i in range(len(items) - 1, -1, -1):
        reversed_items.append(items[i])
    return reversed_items

reverse_list([1, 2, 3])    # [3, 2, 1]
```

The shortcuts are `items[::-1]` for a reversed copy and `list(reversed(items))`.

**Splitting into two groups with a step.** Slicing with a step of 2 takes every other item. Starting at `0` gives the even indexes, and starting at `1` gives the odd ones:

```python
def get_even_and_odd_teams(players):
    return players[::2], players[1::2]
```

**Building two result lists at once.** A loop can fill more than one list. Each list starts empty before the loop and gets one entry per item, so the results stay lined up by index. This filters a word out of chat messages and counts how many were removed, with a nested loop over the words in each message:

```python
def filter_messages(messages):
    filtered_messages = []
    dang_counts = []
    for message in messages:
        words = message.split()
        good_words = []
        dang_count = 0
        for word in words:
            if word == "dang":
                dang_count += 1
            else:
                good_words.append(word)
        filtered_messages.append(" ".join(good_words))
        dang_counts.append(dang_count)
    return filtered_messages, dang_counts

filter_messages(["dang it bobby!", "look at it go"])
# (['it bobby!', 'look at it go'], [1, 0])
```

The per-message variables, `good_words` and `dang_count`, are created inside the outer loop so each message starts fresh. Creating them once before the outer loop would carry words and counts from one message into the next.

**Comparing two lists.** `not in` inside a loop finds what one list has that another lacks. The count of matches then gives a percentage:

```python
def check_ingredient_match(recipe, inventory):
    missing = []
    for ingredient in recipe:
        if ingredient not in inventory:
            missing.append(ingredient)
    have = len(recipe) - len(missing)
    return have / len(recipe) * 100, missing

recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
inventory = ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]
check_ingredient_match(recipe, inventory)    # (75.0, ['Unicorn Hair'])
```

`/` always returns a float, so the percentage is `75.0` even when it divides evenly.

## Analogy

Continuing the kitchen from Chapters 1 to 8: **a list is a numbered row of jars on a shelf.**

- The shelf holds the jars in a fixed order, and each spot has a number painted under it. The first spot is painted `0`, which is the part that trips up every new cook.
- `shelf[2]` is "hand me the jar in spot 2." Asking for a spot past the end of the shelf gets nothing but an error.
- `len(shelf)` is counting the jars. Six jars means the last spot is painted `5`.
- `shelf[1] = "Iron Bar"` is swapping out the jar in spot 1. It only works on a spot that already exists. The shelf does not grow by pointing at empty wall.
- `.append()` is putting a new jar at the end of the row, and `.pop()` is taking the last jar off and handing it over. Taking jars off the end one by one gives them back in reverse order.
- `for jar in shelf` is walking along the shelf reading each label. `for i in range(len(shelf))` is walking along reading the painted numbers, which is needed when a jar has to be swapped or compared with the jar in the same spot on another shelf.
- A negative index is counting from the right end of the shelf: `shelf[-1]` is the jar nearest the end, whatever its painted number.
- A slice is copying a stretch of the shelf onto a new tray. `shelf[2:5]` takes spots 2, 3, and 4, and the original shelf keeps all its jars.
- `+` is pushing two shelves together into one long new shelf.
- `"salt" in shelf` is scanning the labels for salt without caring where it sits.
- `del shelf[0]` is throwing a jar away and sliding the rest down to close the gap.
- A tuple is a sealed spice kit: a fixed set of jars in fixed slots, like name, age, and elf status. Nothing can be swapped in or out, and unpacking is opening the kit and setting each jar on its own spot on the counter.
- `.split()` is chopping a sentence into a row of word jars, and `" ".join()` is lining them back up with a space between each.

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

# Negative indexes and slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[-1], numbers[-2])         # 9 8
print(numbers[1:5:2])                   # [1, 3]
print(numbers[:3])                      # [0, 1, 2]
print(numbers[3:])                      # [3, 4, 5, 6, 7, 8, 9]
print(numbers[::2])                     # [0, 2, 4, 6, 8]
print(numbers[1::2])                    # [1, 3, 5, 7, 9]
print(numbers[-3:])                     # [7, 8, 9]
print(numbers[:-1])                     # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[::-1])                    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[5:100], numbers[8:3])     # [5, 6, 7, 8, 9] []

copy = numbers[:]
print(copy == numbers, copy is numbers) # True False

def get_champion_slices(champions):
    return champions[2:], champions[:-1], champions[::2]

print(get_champion_slices(["Frodo", "Aragorn", "Legolas", "Gimli", "Sam"]))
# (['Legolas', 'Gimli', 'Sam'], ['Frodo', 'Aragorn', 'Legolas', 'Gimli'], ['Frodo', 'Legolas', 'Sam'])

# Concatenating
print([1, 2, 3] + [4, 5, 6])            # [1, 2, 3, 4, 5, 6]
a = [1, 2]
b = a + [3]
print(a, b)                             # [1, 2] [1, 2, 3], a is unchanged

# Membership
fruits = ["apple", "orange", "banana"]
print("banana" in fruits)               # True
print("banana" not in fruits)           # False
print("an" in "banana")                 # True, substring check on strings

# Deleting
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[3]
print(nums)                             # [1, 2, 3, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)                             # [1, 5, 6, 7, 8, 9]
del nums[:]
print(nums)                             # []

def trim_strongholds(strongholds):
    del strongholds[0]
    del strongholds[-2:]
    return strongholds

print(trim_strongholds(["a", "b", "c", "d", "e"]))   # ['b', 'c']

items = ["sword", "shield", "potion"]
items.remove("shield")
print(items)                            # ['sword', 'potion']

# Tuples
dog = ("Fido", 4)
print(dog[0])                           # Fido
print(type(("Fido",)), type(("Fido")))  # <class 'tuple'> <class 'str'>
dog_name, dog_age = dog
print(dog_name, dog_age)                # Fido 4

heroes = [
    ("Glorfindel", 2093, True),
    ("Gandalf", 1000, False),
]
print(heroes[0][0], heroes[1][2])       # Glorfindel False
for name, age, is_elf in heroes:
    print(name, age, is_elf)            # Glorfindel 2093 True, Gandalf 1000 False

# Splitting and joining
words = "hello there sam".split()
print(words)                            # ['hello', 'there', 'sam']
print(" ".join(words))                  # hello there sam
print("a,b,,c".split(","))              # ['a', 'b', '', 'c']

# Guarding against an empty list
def get_first_item(items):
    if len(items) == 0:
        return "ERROR"
    return items[0]

print(get_first_item([]))               # ERROR

# Finding the max
def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far

print(find_max([100, 10, 22]))          # 100
print(find_max([-5, -2, -9]))           # -2
print(find_max([]))                     # -inf

# Filtering with modulo
def get_odd_numbers(num):
    odd_numbers = []
    for i in range(0, num):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers

print(get_odd_numbers(10))              # [1, 3, 5, 7, 9]

# Reversing with a loop
def reverse_list(items):
    reversed_items = []
    for i in range(len(items) - 1, -1, -1):
        reversed_items.append(items[i])
    return reversed_items

print(reverse_list(["a", "b", "c", "d"]))   # ['d', 'c', 'b', 'a']
print(reverse_list([]))                 # []

# Two teams with a step
def get_even_and_odd_teams(players):
    return players[::2], players[1::2]

print(get_even_and_odd_teams(["Frodo", "Aragorn", "Legolas", "Gimli", "Sam"]))
# (['Frodo', 'Legolas', 'Sam'], ['Aragorn', 'Gimli'])

# Two result lists, nested loop
def filter_messages(messages):
    filtered_messages = []
    dang_counts = []
    for message in messages:
        words = message.split()
        good_words = []
        dang_count = 0
        for word in words:
            if word == "dang":
                dang_count += 1
            else:
                good_words.append(word)
        filtered_messages.append(" ".join(good_words))
        dang_counts.append(dang_count)
    return filtered_messages, dang_counts

print(filter_messages(["dang it bobby!", "look at it go"]))
# (['it bobby!', 'look at it go'], [1, 0])

# Comparing two lists
def check_ingredient_match(recipe, inventory):
    missing = []
    for ingredient in recipe:
        if ingredient not in inventory:
            missing.append(ingredient)
    have = len(recipe) - len(missing)
    return have / len(recipe) * 100, missing

recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
inventory = ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]
print(check_ingredient_match(recipe, inventory))    # (75.0, ['Unicorn Hair'])
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

[1][-2]                                 # IndexError: list index out of range
[1, 2] + 3                              # TypeError: can only concatenate list (not "int") to list
[1, 2].remove(5)                        # ValueError: list.remove(x): x not in list
max([])                                 # ValueError: max() iterable argument is empty

dog = ("Fido", 4)
dog[0] = "Rex"                          # TypeError: 'tuple' object does not support item assignment
dog.append(1)                           # AttributeError: 'tuple' object has no attribute 'append'
a, b = ("x", "y", "z")                  # ValueError: too many values to unpack (expected 2, got 3)

" ".join(["a", 1])                      # TypeError: sequence item 1: expected str instance, int found
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
| Last item | `x[-1]` | `x.at(-1)`, since `x[-1]` is `undefined` | `x[len(x)-1]` | `${x[-1]}` |
| Slice | `x[1:3]`, a copy | `x.slice(1, 3)`, a copy | `x[1:3]`, shares memory | `"${x[@]:1:2}"`, offset and count |
| Concatenate | `a + b` | `[...a, ...b]` or `a.concat(b)` | `append(a, b...)` | `c=("${a[@]}" "${b[@]}")` |
| Contains | `v in x` | `x.includes(v)` | `slices.Contains(x, v)` | Loop and compare |
| Delete at index | `del x[i]` | `x.splice(i, 1)` | `x = slices.Delete(x, i, i+1)` | `unset 'x[i]'`, leaves a gap |
| Fixed group | Tuple `("Fido", 4)` | Array or object | Struct, or multiple return values | None |
| Split words | `s.split()` | `s.split(" ")` | `strings.Fields(s)` | `read -ra x <<< "$s"` |
| Join words | `" ".join(x)` | `x.join(" ")` | `strings.Join(x, " ")` | `"${x[*]}"`, joined with the first character of `IFS` |

In C, an array has a fixed size set when it is declared, `int x[3] = {1, 2, 3};`, and every element has the same type. There is no `len()`: `sizeof(x) / sizeof(x[0])` works only where the array was declared, and once it is passed to a function it decays to a pointer and the length must be passed separately. Reading past the end is not an error at all. It is undefined behavior that reads whatever memory sits there. A Python list is closer to a growable array of pointers: it tracks its own length, resizes itself on `append`, and checks every index. C has no slicing, no `in`, and no `+` for arrays either: each is a loop, or a call like `memcpy`, written by hand. The closest thing to a tuple in C is a small `struct`, except that a struct's fields have names instead of positions. `float("-inf")` is the same IEEE 754 value as `-INFINITY` from `<math.h>`.

Two ideas carry over to every language:

1. **Indexes start at 0, so the last index is the length minus 1.** Almost every off by one bug with arrays comes from forgetting this, either by stopping one short or by reading one past the end.
2. **Know what happens on a bad index.** Python and Go stop with an error, which is easy to debug. JavaScript and Bash quietly return nothing, and C reads garbage memory, so the bug shows up somewhere else later.
3. **Know whether a slice is a copy.** Python and JavaScript slices are new lists. A Go slice of a slice shares the same underlying array, so writing to one changes the other.

## Interview framing

1. What is a list in Python, and how is it different from an array in C?
2. What is the time cost of indexing, `append`, and `pop`?
3. When would you loop with `range(len(items))` and when with `for item in items`?
4. What does `append` return, and why does that matter?
5. If a function changes a list it was passed, does the caller see the change?
6. What is the difference between a list and a tuple, and when would you use each?
7. How does slicing work, and what does `items[::-1]` do?
8. What is the time cost of `in` on a list, and what would you use for many lookups?
9. How would you find the largest number in a list without `max()`?

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

**6. List versus tuple**

"Both are ordered and support indexing, slicing, `len`, `in`, and looping. A list is mutable: it can grow, shrink, and have items replaced. A tuple is immutable once created. I use a list for a collection of the same kind of thing whose size changes, like an inventory. I use a tuple for a small fixed record where each position has a meaning, like a name and an age, or a pair of coordinates. Because a tuple cannot change, it can be used as a dictionary key or stored in a set, and returning one from a function makes it clear the caller gets a fixed group of values. One syntax detail: a single-item tuple needs a trailing comma, `(x,)`."

**7. Slicing**

"A slice is `items[start:stop:step]`. It includes `start`, excludes `stop`, and moves by `step`, and it returns a new list. Every part is optional: start defaults to the beginning, stop to the end, and step to 1. Negative values count from the end, so `items[-3:]` is the last three and `items[:-1]` is everything but the last. A negative step walks backward, so `items[::-1]` is a reversed copy. Slicing never raises an `IndexError`. Out of range bounds are clipped, so the worst case is an empty list. Since it copies, slicing is O(k) in the size of the slice."

**8. Cost of `in`**

"`in` on a list is a linear scan, O(n). It compares each item with `==` until it finds a match or reaches the end. That is fine for a short list or a single check, but inside a loop it becomes O(n times m). For example, checking every recipe ingredient against a long inventory list. When I need many lookups, I convert the list to a set once, `set(inventory)`, which makes each `in` check O(1) on average. The trade-off is that a set loses order and duplicates, and its items must be hashable."

**9. Largest number without `max()`**

"I keep a running maximum and loop once. I start it at `float('-inf')`, which is smaller than every number, so the first item always replaces it. Starting at `0` is a common bug, because a list of all negative numbers would return `0`, which is not even in the list. Then for each number, if it is greater than the current maximum, I replace the maximum. It is O(n) time and O(1) space. For an empty list, the function returns negative infinity, while the built-in `max([])` raises a `ValueError` unless I pass a `default`. Another option is to start with `nums[0]` after checking the list is not empty, which keeps the result the same type as the items."

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
- `items[-1]` is the last item, `items[-2]` the second to last.
- `items[start:stop:step]` returns a new list. `stop` is excluded, and every part is optional.
- `[:n]` is the first `n` items, `[n:]` is the rest, `[::2]` is even indexes, `[1::2]` is odd indexes, `[::-1]` is reversed.
- Slicing never raises an `IndexError`.
- `a + b` makes a new list. Both sides must be lists.
- `x in items` and `x not in items` return a boolean. On a string, `in` checks for a substring.
- `del items[i]` and `del items[a:b]` remove by position. `.remove(x)` removes by value.
- A tuple is an ordered, unchangeable group, written `(a, b)`. One item needs a comma: `(a,)`.
- `a, b = pair` unpacks by position, and works in `for` loops too.
- `s.split()` turns a string into a list of words. `" ".join(words)` turns it back.
- Check `len(items) == 0` before reading `items[0]`.
- A running maximum starts at `float("-inf")`. A running minimum starts at `float("inf")`.
- `n % 2 != 0` means `n` is odd.
- `range(len(items) - 1, -1, -1)` visits the indexes backward, down to `0`.

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

**Why does `range(len(items) - 1, 0, -1)` skip the first item?**
The stop is excluded, so counting down to `0` stops at `1`. To include index `0`, the stop has to be one past it in the direction of travel, which is `-1`. This is the same off by one as counting up, mirrored. `items[::-1]` avoids the arithmetic entirely.

**Are `a = a + b` and `a += b` the same for lists?**
Not quite. `a + b` builds a new list and rebinds `a` to it, so any other name pointing at the old list still sees the old contents. `a += b` extends the existing list in place, the same as `a.extend(b)`, so every name pointing at it sees the change. With `b = a` first, `a = a + [3]` leaves `b` as `[1, 2]`, while `a += [3]` makes `b` `[1, 2, 3]` too.

**Is a tuple that holds a list really unchangeable?**
The tuple itself is: it always holds the same objects in the same slots. But a list stored inside it is still a list, so `t = ("x", [1])` followed by `t[1].append(2)` gives `("x", [1, 2])`. What cannot happen is replacing the slot, `t[1] = [9]`. This is also why a tuple containing a list cannot be used as a dictionary key.

**Why does `"a  b".split(" ")` give an empty string in the middle?**
With an explicit separator, `split` cuts at every single occurrence, so two spaces in a row leave an empty string between them, and a trailing space leaves one at the end. With no argument, `split()` treats any run of whitespace as one separator and drops empties at the ends. For splitting text into words, use `split()` with no argument.

**Is `n % 2 == 1` a safe odd check?**
In Python, yes, because `%` takes the sign of the divisor, so `-3 % 2` is `1`. In C, Go, and JavaScript, `-3 % 2` is `-1`, so `n % 2 == 1` misses negative odd numbers. `n % 2 != 0` works in every language, which makes it the habit worth keeping.
