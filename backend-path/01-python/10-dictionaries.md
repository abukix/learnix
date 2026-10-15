# 10: Dictionaries

Source: boot.dev Learn Python, Chapter 10, Lessons 1 to 11.

## What it is

### Dictionaries

A dictionary stores values under names instead of positions. Each entry is a key-value pair: the key is the name used to look something up, and the value is what is stored under it. A list answers "what is in spot 2?", while a dictionary answers "what is the model?"

A dictionary is written with curly braces, with a colon between each key and its value and commas between the pairs:

```python
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2019,
}
```

The keys here are `"brand"`, `"model"`, and `"year"`, and their values are `"Toyota"`, `"Camry"`, and `2019`. Like a list, a dictionary can be written on one line or across several, and the comma after the last pair is allowed. `{}` is an empty dictionary.

Values can be any type, including lists and other dictionaries. Keys are usually strings, but numbers and tuples work too. A key must be a value that cannot change, so a list cannot be a key (see Follow-up gotchas).

A dictionary is a natural way to group the facts about one thing. A function can build one and return it directly, without a variable:

```python
def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }

get_character_record("bloodwarrior123", "server1", 5, "Grunt")
# {'name': 'bloodwarrior123', 'server': 'server1', 'level': 5, 'rank': 'Grunt', 'id': 'bloodwarrior123#server1'}
```

A value can be computed from other inputs, like `id` here, which joins the name and server so two characters with the same name on different servers still get different ids.

### Keys are unique

A dictionary cannot hold the same key twice. If a key appears twice in the same literal, Python does not raise an error. The later value silently replaces the earlier one:

```python
d = {"a": 1, "b": 2, "a": 3}
# {'a': 3, 'b': 2}
len(d)    # 2
```

Because there is no error, a duplicated key is an easy bug to miss. It usually comes from copying a line and forgetting to change the key, which quietly loses one of the values.

### Reading a value

A value is read with its key in square brackets. It looks like indexing a list, but the thing in the brackets is a key, not a position:

```python
car = {"make": "Toyota", "model": "Camry"}
print(car["make"])    # Toyota
```

Reading a key that does not exist is a `KeyError`, the dictionary version of a list's `IndexError`. There is no position to fall back on, so `car[0]` is also a `KeyError: 0` unless `0` is actually one of the keys.

### Adding and updating

Assigning to a key uses the same square brackets with `=`. If the key does not exist yet, it is added. Unlike a list, which cannot grow by assigning to a new index, a dictionary grows this way:

```python
planets = {}
planets["Earth"] = True
planets["Pluto"] = False
print(planets["Pluto"])    # False
```

Starting with an empty dictionary and filling it in a loop is common. Here each full name is split into its two words, and the first name becomes the key:

```python
full_names = ["jack bronson", "jill mcarty", "john denver"]

names_dict = {}
for full_name in full_names:
    name_parts = full_name.split()
    names_dict[name_parts[0]] = name_parts[1]

print(names_dict)
# {'jack': 'bronson', 'jill': 'mcarty', 'john': 'denver'}
```

If the key already exists, the same assignment replaces its value. With two people named Jack, the second one wins:

```python
full_names = ["jack bronson", "james mcarty", "jack denver"]
# same loop as above
# {'jack': 'denver', 'james': 'mcarty'}
```

`"denver"` replaced `"bronson"`, and `jack` stayed in its original spot. So `d[key] = value` means "add or replace," and the code does not say which one happened. When the difference matters, check with `in` first.

### Deleting with `del`

`del` removes a key and its value:

```python
names_dict = {"jack": "bronson", "jill": "mcarty", "joe": "denver"}
del names_dict["joe"]
# {'jack': 'bronson', 'jill': 'mcarty'}
```

Deleting a key that does not exist is a `KeyError`, the same as reading one.

### Checking for a key with `in`

`in` checks whether a key exists, and `not in` checks that it does not. Both return a boolean:

```python
cars = {"ford": "f150", "toyota": "camry"}
"ford" in cars        # True
"gmc" in cars         # False
"gmc" not in cars     # True
"f150" in cars        # False
```

`in` only looks at the keys. `"f150"` is a value, so it is not found. Checking with `in` before reading or deleting is the plain way to avoid a `KeyError`.

### Counting with a dictionary

Counting how many times each item appears in a list is the classic dictionary pattern. The keys are the items, and the values are their counts. The first time an item is seen, its key does not exist yet, so `counts[name] += 1` on its own is a `KeyError`. The fix is to check first:

```python
def count_enemies(enemy_names):
    counts = {}
    for name in enemy_names:
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
    return counts

count_enemies(["jackal", "kobold", "jackal", "soldier", "jackal"])
# {'jackal': 3, 'kobold': 1, 'soldier': 1}
```

It is the accumulator pattern again, with one counter per key instead of one counter in total. The keys come out in the order each item was first seen.

### Looping over a dictionary

`for key in d` loops over the keys, using the same syntax as looping over the values of a list. The value is read with the key inside the loop:

```python
fruit_sizes = {"apple": "small", "banana": "large", "grape": "tiny"}

for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")

# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny
```

The loop variable can have any name. `name` describes these keys, while `key` or `k` are common in general code.

Adding or deleting keys while looping over the same dictionary is a `RuntimeError: dictionary changed size during iteration`. Changing the value of an existing key is fine, since the size stays the same.

### Order

Since Python 3.7, dictionaries keep insertion order. Looping always gives the keys in the order they were first added, and printing shows them in that order too. Before 3.7, the order was not guaranteed and could differ between runs.

A few details follow from that:

- Updating an existing key keeps it in its original position.
- Deleting a key and adding it again moves it to the end.
- Order does not affect equality. `{"a": 1, "b": 2} == {"b": 2, "a": 1}` is `True`.

Insertion order is not the same as sorted order. A dictionary keeps keys in the order they arrived, not alphabetically or by value.

### Nested dictionaries

A value can itself be a dictionary, which gives a structure inside a structure:

```python
progress = {
    "character_name": "Kaladin",
    "quests": {
        "bridge_run": {
            "status": "In Progress",
        },
        "talk_to_syl": {
            "status": "Completed",
        },
    },
}
```

Each lookup returns a value, and if that value is a dictionary, another key can be put right after it. The brackets chain from left to right, one level at a time:

```python
progress["quests"]["bridge_run"]["status"]    # In Progress
```

`progress["quests"]` is the inner dictionary of quests, `["bridge_run"]` picks one quest from it, and `["status"]` reads that quest's status. When the same inner dictionary is used several times, giving it a name keeps the lines short:

```python
quests = progress["quests"]
quests["talk_to_syl"]["status"]    # Completed
```

If any key along the chain is missing, the whole lookup fails with a `KeyError` that names the missing key, which shows how far it got.

### Common dictionary patterns

**Finding the key with the largest value.** It is the running maximum from Chapter 9, but the result is the key, not the number. Two variables track the best count so far and the key it belongs to. The count starts at `float("-inf")` so any real count beats it, and the key starts at `None` so an empty dictionary returns `None`:

```python
def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    most_common = None
    for name in enemies_dict:
        if enemies_dict[name] > max_so_far:
            max_so_far = enemies_dict[name]
            most_common = name
    return most_common

get_most_common_enemy({"jackal": 1, "kobold": 2, "soldier": 3, "gremlin": 5})    # gremlin
get_most_common_enemy({"jackal": 3, "kobold": 3})    # jackal
get_most_common_enemy({})                            # None
```

The comparison is `>`, not `>=`, so on a tie the first key found keeps the lead. With `>=`, the last one would win.

**Merging two dictionaries.** Copy every pair from the first dictionary into a new one, then every pair from the second. A key in both ends up with the second dictionary's value, because the second assignment replaces the first:

```python
def merge(dict1, dict2):
    merged = {}
    for key in dict1:
        merged[key] = dict1[key]
    for key in dict2:
        merged[key] = dict2[key]
    return merged

two_towers = {"Frodo": 56, "Aragorn": 10}
rotk = {"Aragorn": 100, "Gandalf": 809}
merge(two_towers, rotk)
# {'Frodo': 56, 'Aragorn': 100, 'Gandalf': 809}
```

Building a new dictionary leaves both inputs unchanged. `Aragorn` keeps the position it had in the first dictionary, with the updated value from the second.

## Analogy

Continuing the kitchen from Chapters 1 to 9: **a dictionary is a spice rack where every jar has a name label instead of a painted number.**

- The list shelf from Chapter 9 is found by position: "the jar in spot 2." The spice rack is found by name: "the paprika." Nobody needs to know where paprika sits to ask for it.
- The label is the key and what is inside the jar is the value. `rack["paprika"]` is "hand me the paprika."
- Asking for a jar that has no label on the rack is a `KeyError`. There is no spot number to fall back on.
- `rack["cumin"] = "ground"` either puts a new cumin jar on the rack or refills the existing one. The rack never holds two jars with the same label, so a second jar labeled cumin replaces the first.
- `del rack["cumin"]` takes the cumin jar off for good, and asking to remove a jar that is not there is a `KeyError` too.
- `"cumin" in rack` is reading the labels, not tasting the contents. It finds a label, never a value.
- The counting pattern is a tally sheet on the fridge: the first time a spice is used it gets a new line with `1`, and after that its line goes up by one.
- `for label in rack` is reading every label in the order the jars were put up, then reaching for each jar by its label.
- A nested dictionary is a labeled box on the rack that holds its own labeled jars. `pantry["baking"]["sugar"]` is "open the baking box and hand me the sugar."
- Merging is combining two racks onto a new one. When both racks have the same label, the jar from the second rack is the one kept.

## Example

```python
# Creating and reading
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2019,
}
print(car["model"])                     # Camry
print(len(car))                         # 3

def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }

print(get_character_record("bloodwarrior123", "server1", 5, "Grunt")["id"])
# bloodwarrior123#server1

# Duplicate keys, the last one wins
d = {"a": 1, "b": 2, "a": 3}
print(d)                                # {'a': 3, 'b': 2}

# Adding to an empty dictionary
planets = {}
planets["Earth"] = True
planets["Pluto"] = False
print(planets)                          # {'Earth': True, 'Pluto': False}

# Filling from a list, a repeated key is replaced
full_names = ["jack bronson", "james mcarty", "jack denver"]
names_dict = {}
for full_name in full_names:
    names = full_name.split()
    names_dict[names[0]] = names[1]
print(names_dict)                       # {'jack': 'denver', 'james': 'mcarty'}

# Deleting
names_dict = {"jack": "bronson", "jill": "mcarty", "joe": "denver"}
del names_dict["joe"]
print(names_dict)                       # {'jack': 'bronson', 'jill': 'mcarty'}

# Checking for a key
cars = {"ford": "f150", "toyota": "camry"}
print("ford" in cars)                   # True
print("gmc" in cars)                    # False
print("f150" in cars)                   # False, in checks keys only

# Counting
def count_enemies(enemy_names):
    counts = {}
    for name in enemy_names:
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
    return counts

print(count_enemies(["jackal", "kobold", "jackal", "soldier", "jackal"]))
# {'jackal': 3, 'kobold': 1, 'soldier': 1}
print(count_enemies([]))                # {}

# Looping over keys
fruit_sizes = {"apple": "small", "banana": "large", "grape": "tiny"}
for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")
# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny

# Order
o = {"a": 1, "b": 2, "c": 3}
o["a"] = 9
print(o)                                # {'a': 9, 'b': 2, 'c': 3}, same spot
del o["a"]
o["a"] = 1
print(o)                                # {'b': 2, 'c': 3, 'a': 1}, moved to the end
print({"a": 1, "b": 2} == {"b": 2, "a": 1})    # True

# Nested
progress = {
    "character_name": "Kaladin",
    "quests": {
        "bridge_run": {"status": "In Progress"},
        "talk_to_syl": {"status": "Completed"},
    },
}
print(progress["quests"]["bridge_run"]["status"])    # In Progress
quests = progress["quests"]
print(quests["talk_to_syl"]["status"])  # Completed

# Key with the largest value
def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    most_common = None
    for name in enemies_dict:
        if enemies_dict[name] > max_so_far:
            max_so_far = enemies_dict[name]
            most_common = name
    return most_common

print(get_most_common_enemy({"jackal": 1, "kobold": 2, "soldier": 3, "gremlin": 5}))    # gremlin
print(get_most_common_enemy({"jackal": 3, "kobold": 3}))    # jackal, first one wins a tie
print(get_most_common_enemy({}))        # None

# Merging
def merge(dict1, dict2):
    merged = {}
    for key in dict1:
        merged[key] = dict1[key]
    for key in dict2:
        merged[key] = dict2[key]
    return merged

two_towers = {"Frodo": 56, "Aragorn": 10}
rotk = {"Aragorn": 100, "Gandalf": 809}
print(merge(two_towers, rotk))          # {'Frodo': 56, 'Aragorn': 100, 'Gandalf': 809}
print(two_towers)                       # {'Frodo': 56, 'Aragorn': 10}, unchanged
```

Common errors:

```python
car = {"make": "Toyota", "model": "Camry"}
car["year"]                             # KeyError: 'year'
car[0]                                  # KeyError: 0
del car["year"]                         # KeyError: 'year'
car.make                                # AttributeError: 'dict' object has no attribute 'make'

counts = {}
counts["jackal"] += 1                   # KeyError: 'jackal'

{[1, 2]: "x"}                           # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')

for key in car:
    car["year"] = 2019                  # RuntimeError: dictionary changed size during iteration

progress = {"quests": {}}
progress["quests"]["bridge_run"]["status"]    # KeyError: 'bridge_run'

d = {"a": {"b": 1}}
d["a"]["b"]["c"]                        # TypeError: 'int' object is not subscriptable
```

Python versions before 3.14 word the list key error as `TypeError: unhashable type: 'list'`.

## In other languages

| | Python | JavaScript | Go | Bash |
|---|---|---|---|---|
| Name | Dictionary, `dict` | Object, or `Map` | Map | Associative array |
| Create | `d = {"a": 1}` | `const d = {a: 1};` | `d := map[string]int{"a": 1}` | `declare -A d=([a]=1)` |
| Empty | `d = {}` | `const d = {};` or `new Map()` | `d := map[string]int{}` | `declare -A d` |
| Read | `d["a"]` | `d.a` or `d["a"]`, `m.get("a")` | `d["a"]` | `${d[a]}` |
| Add or update | `d["a"] = 2` | `d.a = 2`, `m.set("a", 2)` | `d["a"] = 2` | `d[a]=2` |
| Missing key read | `KeyError` | `undefined`, no error | Zero value, such as `0` or `""` | Empty string, no error |
| Contains | `"a" in d` | `"a" in d`, `m.has("a")` | `_, ok := d["a"]` | `[[ -v d[a] ]]` |
| Delete | `del d["a"]` | `delete d.a`, `m.delete("a")` | `delete(d, "a")` | `unset 'd[a]'` |
| Delete missing key | `KeyError` | No error | No error | No error |
| Length | `len(d)` | `Object.keys(d).length`, `m.size` | `len(d)` | `${#d[@]}` |
| Loop over keys | `for k in d:` | `for (const k in d) { }` | `for k := range d { }` | `for k in "${!d[@]}"; do ... done` |
| Loop order | Insertion order | Insertion order, except integer-like keys come first in an object | Random on purpose | Not guaranteed |
| Duplicate key in a literal | Last one wins | Last one wins | Compile error | Last one wins |
| Nested read | `d["a"]["b"]` | `d.a.b` | `d["a"]["b"]` | Not supported, values are strings |

In C, there is no built-in dictionary. When the keys are known ahead of time, a `struct` is the closest match: `car.brand` is like `car["brand"]`, except the field names are fixed at compile time and cannot be added or looped over. For keys that arrive at run time, C needs a hash table, either written by hand or taken from a library. A hash table is an array of buckets: the key is run through a hash function to get a number, that number picks a bucket, and the key and value are stored there. That is exactly what a Python dictionary does underneath, along with resizing itself as it fills up and handling two keys that land in the same bucket.

Three ideas carry over to every language:

1. **Know what a missing key does.** Python raises a `KeyError`. JavaScript, Go, and Bash all hand back an empty value, so a typo in a key gives `undefined`, `0`, or `""` instead of an error, and the bug shows up somewhere else. Go's `v, ok := d["a"]` exists so the difference between "missing" and "stored as zero" can be checked.
2. **Know whether order is guaranteed.** Python keeps insertion order. Go deliberately randomizes it, so code that depends on map order breaks. When order matters in Go or Bash, sort the keys first.
3. **Lookup by key is fast.** In every language, these are hash tables, so finding a key does not scan every entry the way `in` does on a list.

## Interview framing

1. What is a dictionary, and when would you use one instead of a list?
2. How does a dictionary find a value so fast?
3. What happens when you read, assign, or delete a key that does not exist?
4. What can be used as a dictionary key, and why can't a list be one?
5. Are dictionaries ordered?
6. How would you count how many times each word appears in a list?
7. How would you merge two dictionaries, and what happens to keys that appear in both?

## My answer

**1. Dictionary versus list**

"A dictionary maps keys to values. It is mutable, keeps insertion order, and every key is unique. I use a list when I have a sequence of the same kind of thing and care about position or order, like a feed of posts. I use a dictionary when I need to look things up by a name or an id, like a user by username, or when I am describing one thing with named fields, like a character's name, level, and rank. The question I ask is whether I will find items by position or by key. Looking up by key in a dictionary is O(1) on average, while finding a value in a list with `in` is O(n)."

**2. How lookup works**

"A dictionary is a hash table. When I store a key, Python calls `hash()` on it to get a number, uses that number to pick a slot in an internal array, and stores the key and value there. To look the key up, it hashes it again, goes straight to that slot, and checks with `==` that the key really matches. So the cost does not depend on how many entries there are, which makes lookup, insert, and delete O(1) on average. Two different keys can land on the same slot, which is a collision, and Python then probes other slots. With a terrible hash function everything could collide and lookups would degrade to O(n), but with built-in types that does not happen in practice. Python also grows the table when it gets too full, which, like a list's `append`, is rare enough that adding stays O(1) on average."

**3. Missing keys**

"Reading a missing key with square brackets raises a `KeyError`, and so does deleting one with `del`. Assigning to a missing key does not raise anything. It just adds the key, which is how dictionaries are built up in a loop. Assigning to a key that already exists replaces its value, so assignment means add or replace. To read safely, I check with `key in d` first. In the counting pattern, that check is what turns the first `+= 1` from a `KeyError` into setting the count to `1`."

**4. What can be a key**

"A key has to be hashable, which in practice means immutable: strings, numbers, booleans, `None`, and tuples that only contain hashable values. A list cannot be a key because it can change. If a list key were changed after being stored, its hash would change, and the dictionary would look for it in the wrong slot, so the entry would be lost. Python prevents that by refusing mutable keys with a `TypeError`. When I need a compound key, like a coordinate, I use a tuple such as `(x, y)`. One surprise is that `1`, `1.0`, and `True` are equal and have the same hash, so they count as the same key."

**5. Ordering**

"Since Python 3.7, dictionaries are guaranteed to keep insertion order. Looping, printing, and building a list from the keys all follow the order in which keys were first added. Updating a key keeps its position, and deleting and re-adding it moves it to the end. Insertion order is not sorted order, and equality ignores order, so two dictionaries with the same pairs in a different order are equal. In 3.6 the order was kept as an implementation detail, and before that it was not kept at all, so very old code may not rely on it. Other languages differ: Go randomizes map order on purpose."

**6. Counting words**

"I loop over the words once with an empty dictionary. For each word, if it is already a key, I add one to its count, and otherwise I set its count to `1`. That is O(n) time, and the space is the number of distinct words. The `in` check matters, because `counts[word] += 1` on a word seen for the first time is a `KeyError`. If I need the most common word afterward, I loop over the counts with a running maximum, keeping both the best count and the word it belongs to."

**7. Merging**

"I create a new empty dictionary, loop over the first one copying every key and value in, then do the same with the second. When a key is in both, the second assignment replaces the first, so the second dictionary wins, and the key keeps the position from where it first appeared. Building a new dictionary leaves both inputs unchanged. If I wrote the second loop into the first dictionary instead, I would be changing the caller's data, since dictionaries are passed by reference like lists."

**Points to recall**

- Dictionaries use curly braces with `key: value` pairs separated by commas. `{}` is empty.
- Values can be any type. Keys must be hashable, so a list cannot be a key.
- Keys are unique. A duplicate key in a literal is not an error, the last value wins.
- `d[key]` reads a value. A missing key is a `KeyError`.
- `d[key] = value` adds a new key or replaces an existing value.
- `del d[key]` removes a key. A missing key is a `KeyError`.
- `key in d` and `key not in d` check keys only, never values.
- Counting: `if key in counts: counts[key] += 1`, `else: counts[key] = 1`.
- `for key in d` loops over keys. Read the value with `d[key]`.
- Do not add or delete keys while looping over the same dictionary.
- Insertion order is kept since Python 3.7. Updating keeps the position, delete and re-add moves to the end.
- Equality ignores order.
- Nested lookups chain: `d["outer"]["inner"]`.
- Key with the largest value: start at `float("-inf")` and `None`, and use `>` so the first key wins a tie.
- Merging with loops: copy the first, then the second. The second wins on shared keys.
- `b = d` does not copy a dictionary. Both names point at the same one.

## Follow-up gotchas

**Why is a duplicate key not an error?**
A dictionary literal is built one pair at a time from left to right, as if each pair were `d[key] = value`. The second `"a"` is just an update to a key that already exists. Python checks nothing extra, so the earlier value is silently lost. Go is stricter and refuses to compile a map literal with a duplicate constant key. A linter like Ruff or Pylint flags it in Python.

**Why does `"f150" in cars` return `False` when `"f150"` is right there?**
`in` on a dictionary only checks the keys, because that is the fast lookup a hash table provides. Checking the values would mean scanning every entry. A value check needs a loop over the keys comparing `cars[key] == "f150"`, and it is O(n), the same as `in` on a list.

**Why does `{1: "a", True: "b"}` have only one key?**
`True == 1` and `hash(True) == hash(1)`, and `1.0` matches both as well. A dictionary treats keys that are equal and hash the same as one key, so the later value replaces the earlier one, and the key keeps the first spelling: `{1: "a", 1.0: "b", True: "c"}` is `{1: 'c'}`. It rarely matters in practice, but it explains a dictionary that seems to have lost an entry.

**Why did changing the dictionary inside a function change the caller's dictionary?**
Like a list, a dictionary is passed by reference to the same object. `d["x"] = 1` or `del d["x"]` inside a function changes the dictionary the caller holds. The same goes for `b = d` outside a function: both names point at one dictionary. To get an independent one, copy it with `d.copy()` or `dict(d)`. The copy is shallow, so nested dictionaries are still shared, and `copy.deepcopy(d)` copies all the way down. The merge function builds a new dictionary for this reason.

**Why does deleting keys inside `for key in d` crash?**
The loop walks the dictionary's internal table. Adding or removing a key can change the table's size or rearrange it, so Python stops with `RuntimeError: dictionary changed size during iteration` instead of skipping or repeating keys. The fix is to loop over a copy of the keys, `for key in list(d):`, or to build a new dictionary with only the keys to keep. Changing the value of an existing key during the loop is fine.

**Why `float("-inf")` and `None` for the starting values, and why `>` instead of `>=`?**
`-inf` is lower than any count, so the first key always takes the lead, even if every count is negative. Starting at `0` would return `None` for a dictionary of all negative values. `None` for the key means an empty dictionary returns `None`, which is clearly "no answer" rather than a fake name. Using `>` means a later key has to beat the leader strictly, so the first key found wins a tie. With `>=`, the last tied key would win instead.

**What happens if a nested key is missing?**
The chain stops at the first missing key with a `KeyError` naming that key, such as `KeyError: 'bridge_run'`. If a key exists but its value is not a dictionary, the next bracket fails differently, with `TypeError: 'int' object is not subscriptable`, or `'str'` for a string. When the shape of the data is not guaranteed, check each level with `in` before going deeper.
