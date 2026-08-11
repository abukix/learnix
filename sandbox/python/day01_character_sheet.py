"""
Day 1 — Character sheet (variables & types, f-strings)

Create variables for a character:
    name: str, hp: int, level: int, is_alive: bool, luck: float

Print a formatted status line using an f-string, e.g.:
    "Kael | Lvl 3 | HP: 42 | Luck: 1.5 | Alive: True"
"""

def main() -> str:
    name: str = "JC"
    hp: int = 100
    level: int = 32
    is_alive: bool = True
    luck: float = 26.08

    return f"{name} | Lvl {level} | HP: {hp} | Luck: {luck} | Alive: {is_alive}"

if __name__ == "__main__":
    char_stats = main()
    print(char_stats)