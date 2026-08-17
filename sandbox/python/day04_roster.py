"""
Day 4 — Roster loop (loops & lists)

Build party: list[dict] of 3-4 characters (reuse create_character from Day 2).

Write print_roster(party) that loops over the party and prints each
member via describe_character.
"""

from day02_functions import create_character, describe_character


def print_roster(party):
    for members in party:
        print(describe_character(members))

if __name__ == "__main__":
    party = [
        create_character("Kael", 42, 3, 1.5),
        create_character("Wren", 30, 2, 1.0),
        create_character("John", 32, 5, 1.4),
    ]
    print_roster(party)
