"""
Day 9 — Custom exceptions (errors & exception handling)

Define:
    class InsufficientGoldError(Exception)
    class ItemNotFoundError(Exception)

Write buy_item(party_gold, inventory, item, cost) -> int
    raises the right exception instead of silently failing.

At the call site, wrap it in a try/except block that prints a
friendly message per exception type.
"""


class InsufficientGoldError(Exception):
    pass


class ItemNotFoundError(Exception):
    pass


def buy_item(party_gold, inventory, item, cost):
    # TODO: raise InsufficientGoldError / ItemNotFoundError as appropriate,
    # otherwise deduct cost and return the new gold total
    pass


if __name__ == "__main__":
    # TODO: try/except around a buy_item call, print a friendly message
    # per exception type
    pass
