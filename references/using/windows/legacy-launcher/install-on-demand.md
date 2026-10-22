# 4.12.7. Install on demand

### 4.12.7. Install on demand

Setting the environment variable `PYLAUNCHER_ALLOW_INSTALL` (to any value), where the requested Python version is missing but obtainable from the Microsoft Store, makes the launcher try to install it. Completing that may call for user interaction, and you might need to issue the command once more.

A further `PYLAUNCHER_ALWAYS_INSTALL` variable drives the launcher to always attempt to install Python, even when it is already detected. That is meant mostly for testing (and is best paired with `PYLAUNCHER_DRYRUN`).

[Subject index](INDEX.md) · [Previous source section](dry-run.md) · [Following source section](return-codes.md)
