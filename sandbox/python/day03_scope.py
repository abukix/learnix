"""
Day 3 — Scope

Add a module-level PARTY_GOLD = 100.

First write spend_gold_broken(amount) that tries to subtract from
PARTY_GOLD directly inside the function body (no `global`) — run it
and see what actually happens.

Then write spend_gold(amount) that fixes it properly: either using
`global`, or (better) by returning the new value and reassigning at
the call site.

Write one sentence (as a comment) explaining why the broken version
didn't work the way you'd expect.
"""

from day02_functions import create_character, describe_character  # noqa: F401

PARTY_GOLD = 100


def spend_gold_broken(amount):
    PARTY_GOLD -= amount
    return PARTY_GOLD


def spend_gold(amount):
    return PARTY_GOLD - amount

# PARTY_GOLD -= amount assigns to PARTY_GOLD, so Python treats it as a local
# variable for the whole function — and the read on that same line happens
# before the assignment completes, so it crashes on an empty local slot
# instead of falling through to the global.

if __name__ == "__main__":
    print(f"Starting gold: {PARTY_GOLD}")
    PARTY_GOLD = spend_gold(10)
    print(f"After spending: {PARTY_GOLD}")
