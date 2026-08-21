"""
Calculator

Build a simple calculator using functions — one function per operation.

Requirements:
- add(a, b), subtract(a, b), multiply(a, b), divide(a, b) — each takes two
  numbers and returns the result. No printing inside these; they only
  calculate and return.
- Division by zero: don't worry about it yet. Handling that gracefully is
  what the later "Safe calculator / input validator" drill is for.
  try/except hasn't been covered yet (that's CH12) — this Calculator
  intentionally lets a bad divide crash for now, on purpose.
- main(): call each function above with a couple of example numbers, and
  print each result with an f-string.

Concepts this exercises: variables & types, arithmetic operators, functions,
f-strings (CH1-3).

Stretch (optional, beyond the course notes so far): instead of hardcoding
the two numbers, read them from the user with input(). input() always
returns a string, so you'll need int() or float() to convert it before
doing math with it.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def main():
    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))
    add_result = add(a, b)
    subtract_result = subtract(a, b)
    multiply_result = multiply(a, b)
    divide_result = divide(a, b)
    print("----------------------------------------------------------------")
    print(f"The sum of {a} and {b} is equal to {add_result}")
    print(f"The subtraction of {a} and {b} is equal to {subtract_result}")
    print(f"The multiplication of {a} and {b} is equal to {multiply_result}")
    print(f"The division of {a} and {b} is equal to {divide_result}")

if __name__ == "__main__":
    main()
