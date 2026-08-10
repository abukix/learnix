"""
Day 2 — Functions

Wrap Day 1 into two functions:
    create_character(name, hp, level, luck) -> dict
    describe_character(character: dict) -> str

describe_character must NOT print — it returns the formatted line;
the caller prints it.
"""


def create_character(name, hp, level, luck):
    # TODO: build and return the character dict
    pass


def describe_character(character):
    # TODO: return the formatted status line
    pass


if __name__ == "__main__":
    kael = create_character("Kael", 42, 3, 1.5)
    print(describe_character(kael))
