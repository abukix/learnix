# Intermediate

One smaller real project — chains a handful of concepts together, built in one continuous push rather than day-by-day like the advanced tier.

## Bank Account Simulator

A command-line bank account manager: create accounts, deposit, withdraw, check balances, and view transaction history — all in memory, no file persistence yet.

- Accounts as `dict[str, dict]` (account number → account info)
- `deposit()` / `withdraw()` functions, raising a custom `InsufficientFundsError` on overdraft attempts
- A running transaction log (`list[dict]`) per account, printed on request
- Type hints throughout

Concepts exercised: functions, dictionaries, lists, custom exceptions, comparisons, type hints.
