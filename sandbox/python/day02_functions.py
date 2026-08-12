"""
Day 2 — Functions

Wrap Day 1 into two functions:
    create_character(name, hp, level, luck) -> dict
    describe_character(character: dict) -> str

describe_character must NOT print — it returns the formatted line;
the caller prints it.
"""
def create_character(name, hp, level, luck) -> dict:
    return {"name": name, "hp": hp, "level": level, "luck": luck}


def describe_character(character) -> str:
    return f"{character["name"]} | Lvl {character["level"]} | HP: {character["hp"]} | Luck: {character["luck"]}"


if __name__ == "__main__":
    kael = create_character("Kael", 42, 3, 1.5)
    print(describe_character(kael))
