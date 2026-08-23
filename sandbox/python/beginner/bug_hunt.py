"""
Bug Hunt

This script is supposed to run a short "clear the dungeon" simulation:
- announce every monster in the encounter list, in order
- track the party's gold total as loot comes in from each monster
- report whether the final boss was defeated
- print a sorted copy of the monster names for the summary, without
  touching the original list/order

It has 4 deliberately planted bugs. None of them are pointed out below —
find them the way CH5 describes: run the script, read whatever error or
traceback shows up (or the wrong output, if it runs without crashing), add
print() statements to check what a variable actually holds at each step,
and narrow it down before fixing anything. Fix and rerun one bug at a
time — some bugs are hiding behind earlier ones and won't show up until
the one before it is fixed.

Expected output once every bug is fixed and it runs start to finish:

    Encounter: Goblin
    Encounter: Skeleton
    Encounter: Slime
    Encounter: Dragon
    Gold after Goblin: 10
    Gold after Skeleton: 25
    Gold after Slime: 30
    Gold after Dragon: 80
    Final boss defeated: True
    Sorted copy: ['Dragon', 'Goblin', 'Skeleton', 'Slime']
    Original order preserved: ['Goblin', 'Skeleton', 'Slime', 'Dragon']

One of the bugs is a scope issue shaped like CH4's PARTY_GOLD example —
same kind of mistake, different code.

Concepts this exercises: CH5 (debugging process), CH4 (scope).
"""

GOLD = 0
MONSTERS = ["Goblin", "Skeleton", "Slime", "Dragon"]
LOOT = [10, 15, 5, 50]


def announce_encounters(monsters):
    for i in range(len(monsters) - 1):
        print(f"Encounter: {monsters[i]}")


def add_gold(amount):
    GOLD += amount
    return GOLD


def boss_defeated(boss_name):
    if boss_name = "Dragon":
        return True
    return False


def sorted_copy(monsters):
    monsters.sort()
    return monsters


def main():
    announce_encounters(MONSTERS)

    for name, loot in zip(MONSTERS, LOOT):
        total = add_gold(loot)
        print(f"Gold after {name}: {total}")

    print(f"Final boss defeated: {boss_defeated(MONSTERS[-1])}")

    summary = sorted_copy(MONSTERS)
    print(f"Sorted copy: {summary}")
    print(f"Original order preserved: {MONSTERS}")


if __name__ == "__main__":
    main()
